from PIL import Image
import os

dirs = [
    r'C:\Users\HP\Desktop\心理html\assets\stop',
    r'C:\Users\HP\Desktop\心理html\assets\cases',
    r'C:\Users\HP\Desktop\心理html\assets\tabs',
    r'C:\Users\HP\Desktop\心理html\assets\books',
    r'C:\Users\HP\Desktop\心理html\assets\frames',
    r'C:\Users\HP\Desktop\心理html\assets\game',
]

for d in dirs:
    if not os.path.isdir(d):
        continue
    for f in os.listdir(d):
        if not f.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        p = os.path.join(d, f)
        im = Image.open(p)
        w, h = im.size
        # 长边限制到 1200
        if max(w, h) > 1200:
            scale = 1200 / max(w, h)
            im = im.resize((int(w*scale), int(h*scale)), Image.LANCZOS)
        # 如果是png且有透明，保留png；否则转jpg
        if f.lower().endswith('.png'):
            im.save(p, optimize=True)
        else:
            rgb = im.convert('RGB')
            rgb.save(p, quality=72, optimize=True)
        print(f, os.path.getsize(p)//1024, 'KB')
