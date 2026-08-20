from PIL import Image
im = Image.open('chatgpt-logo.png').convert('RGBA')
w, h = im.size
print('orig', im.size)
# square symbol (left D mark) -> 512 favicon source
sym = im.crop((0, 0, int(w * 0.40), h)).resize((512, 512), Image.LANCZOS)
sym.save('/tmp/logo-sym.png')
fav = sym.resize((64, 64), Image.LANCZOS)
fav.save('/tmp/favicon.png')
# wide OG banner (whole lockup) on the site's slate background
bg = Image.new('RGB', (1600, 630), (245, 247, 251))
logo = im.convert('RGBA').resize((1200, 450), Image.LANCZOS)
bg.paste(logo, ((1600 - 1200) // 2, (630 - 450) // 2), logo)
bg.save('/tmp/og-banner.jpg', quality=90)
print('done: sym favicon og-banner')