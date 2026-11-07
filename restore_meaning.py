from PIL import Image
import os
base = r'C:\Users\HP\Desktop\心理html\assets\cases'
p = os.path.join(base, 'meaning.jpg')
im = Image.open(p)
print('current', im.size)
# 恢复到第一次裁后的 2251x1565
im2 = im.resize((2251, 1565), Image.LANCZOS)
im2.save(p, quality=92)
print('restored', im2.size)
