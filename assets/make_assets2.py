from PIL import Image
import base64, os

im = Image.open('/root/discountedtokens-marketing/assets/chatgpt-logo.png').convert('RGBA')
# Exact D symbol bbox found via blue-density scan: x 96-292, y 276-463
sym = im.crop((90, 270, 300, 470))
print('symbol raw size:', sym.size)

# Make it a clean square with padding
w, h = sym.size
side = max(w, h) + 40  # some breathing room
canvas = Image.new('RGBA', (side, side), (0, 0, 0, 0))
canvas.paste(sym, ((side - w) // 2, (side - h) // 2), sym)

# 512 master (nav uses ~26 display)
m = canvas.resize((512, 512), Image.LANCZOS)
m.save('/tmp/dmark-512.png', optimize=True)
# nav mark 160 (crisp downscale from 512)
nav = m.resize((160, 160), Image.LANCZOS)
nav.save('/tmp/nav-mark.png', optimize=True)
# favicon 48
fav = m.resize((48, 48), Image.LANCZOS)
fav.save('/tmp/favicon-48.png', optimize=True)

def b64(p):
    return base64.b64encode(open(p, 'rb').read()).decode()

js = f'''/**
 * DiscountedTokens brand assets (base64-inlined so the worker needs no R2/bucket).
 * D-symbol cropped from "ChatGPT Image Aug 20 2026" logo on 2026-08-20.
 */
export const LOGO_NAV = "data:image/png;base64,{b64('/tmp/nav-mark.png')}";
export const LOGO_FAVICON = "data:image/png;base64,{b64('/tmp/favicon-48.png')}";
'''
open('/root/reseller/src/assets.js', 'w').write(js)
print('assets.js bytes:', os.path.getsize('/root/reseller/src/assets.js'))
print('nav bytes:', os.path.getsize('/tmp/nav-mark.png'), 'fav bytes:', os.path.getsize('/tmp/favicon-48.png'))

# also generate the wide og-banner (full lockup on bg)
og = Image.new('RGB', (1600, 630), (245, 247, 251))
lc = im.convert('RGBA').resize((1200, 450), Image.LANCZOS)
og.paste(lc, ((1600 - 1200) // 2, (630 - 450) // 2), lc)
og.save('/tmp/og-banner.jpg', quality=88)
print('og-banner:', os.path.getsize('/tmp/og-banner.jpg'))