from PIL import Image
import os
base = r'C:\Users\HP\Desktop\心理html\assets\cases'
p = os.path.join(base, 'meaning.jpg')
im = Image.open(p)
print('current', im.size)
# 当前2026x1472，放大回2251x1565（第一次裁后的尺寸）
im2 = im.resize((2251, 1565), Image.LANCZOS)
# 只裁右边1.5%去掉黑边
w,h = im2.size
crop = im2.crop((0, 0, int(w*0.985), h))
crop.save(p, quality=92)
print('saved', crop.size)
