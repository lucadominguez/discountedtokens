from PIL import Image
import base64, io, struct, os

src = '/root/discountedtokens-marketing/assets/chatgpt-logo.png'
im = Image.open(src).convert('RGBA')
w, h = im.size

# D symbol (blue): x90-470 bounds found earlier
sym = im.crop((90, 270, 300, 470))
sw, sh = sym.size
side = max(sw, sh) + 40
canvas = Image.new('RGBA', (side, side), (0, 0, 0, 0))
canvas.paste(sym, ((side - sw) // 2, (side - sh) // 2), sym)
master = canvas.resize((512, 512), Image.LANCZOS)

def png_data_uri(pimg):
    buf = io.BytesIO()
    pimg.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()

fav48 = master.resize((48, 48), Image.LANCZOS)
nav160 = master.resize((160, 160), Image.LANCZOS)
touch180 = master.resize((180, 180), Image.LANCZOS)

# favicon.ico container (32 + 16)
def png_to_ico(png_bytes, sizes=[(32, 32), (16, 16)]):
    im2 = Image.open(io.BytesIO(png_bytes))
    entries = b''
    datas = b''
    for ww, hh in sizes:
        r = im2.resize((ww, hh), Image.LANCZOS).convert('RGBA')
        b = io.BytesIO(); r.save(b, 'PNG'); png = b.getvalue()
        entries += struct.pack('<BBBBHHII', ww, hh, 0, 0, 1, 32, len(png), 6 + 16 * len(sizes) + len(datas))
        datas += png
    return struct.pack('<HHH', 0, 1, len(sizes)) + entries + datas

fav_b64 = base64.b64encode(fav48.load) if False else base64.b64encode(fav48.tobytes())
favbuf = io.BytesIO(); fav48.save(favbuf, 'PNG', optimize=True)
favico = png_to_ico(favbuf.getvalue())

# OG banner (wide lockup)
og = Image.new('RGB', (1600, 630), (245, 247, 251))
lc = im.convert('RGBA').resize((1200, 450), Image.LANCZOS)
og.paste(lc, ((1600 - 1200) // 2, (630 - 450) // 2), lc)
ogbuf = io.BytesIO(); og.save(ogbuf, 'JPEG', quality=88)

favico_datauri = 'data:image/x-icon;base64,' + base64.b64encode(favico).decode()
og_datauri = 'data:image/jpeg;base64,' + base64.b64encode(ogbuf.getvalue()).decode()

js = f'''/**
 * DiscountedTokens icon + OG assets (base64-inlined).
 * Served at /favicon.ico /apple-touch-icon.png /og-image.png by the worker.
 */
export const FAVICON_ICO = "{favico_datauri}";
export const APPLE_TOUCH = "{png_data_uri(touch180)}";
export const OG_IMAGE = "{og_datauri}";
'''
open('/root/reseller/src/icons.js', 'w').write(js)
print('icons.js bytes:', os.path.getsize('/root/reseller/src/icons.js'))
print('og jpeg bytes:', len(ogbuf.getvalue()))
# real files for direct fetch test
open('/tmp/favicon.ico', 'wb').write(favico)
open('/tmp/og-image.jpg', 'wb').write(ogbuf.getvalue())
