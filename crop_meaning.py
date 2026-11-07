from PIL import Image
import os
base = r'C:\Users\HP\Desktop\心理html\assets\cases'
p = os.path.join(base, 'meaning.jpg')
im = Image.open(p)
w,h = im.size
# 右边多裁一点
crop = im.crop((int(w*0.03), int(h*0.03), int(w*0.93), int(h*0.97)))
crop.save(p, quality=92)
print('meaning', im.size, '->', crop.size)
