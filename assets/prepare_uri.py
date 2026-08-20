from PIL import Image
# nav logo: square D mark at 40px display (downscale to 128 for crispness/byte size)
sym = Image.open('chatgpt-logo.png').convert('RGBA')
w, h = sym.size
sym = sym.crop((0, 0, int(w * 0.38), h)).resize((160, 160), Image.LANCZOS)
sym.save('/tmp/nav-mark.png', optimize=True)
# favicon 48
fav = Image.open('/tmp/nav-mark.png').resize((48, 48), Image.LANCZOS)
fav.save('/tmp/favicon-48.png', optimize=True)
import base64
for path, name in [('/tmp/nav-mark.png','NAV'), ('/tmp/favicon-48.png','FAV')]:
    with open(path,'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    print(f"{name}_datauri_len={len(b64)}")
    open(f'/tmp/{name}.b64','w').write(b64)
print("bytes:", __import__('os').path.getsize('/tmp/nav-mark.png'), __import__('os').path.getsize('/tmp/favicon-48.png'))