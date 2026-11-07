from PIL import Image
import os
base = r'C:\Users\HP\Desktop\心理html\assets\cases'
# 原始尺寸
originals = {
    'empty': (1582, 1170),
    'socialanx': (2040, 1756),
    'impostor': (1582, 1218),
    'numb': (2170, 1732),
    'meaning': (2394, 1664),
}
for name, size in originals.items():
    p = os.path.join(base, name + '.jpg')
    im = Image.open(p)
    print(name, 'current', im.size, '-> restore', size)
    im2 = im.resize(size, Image.LANCZOS)
    im2.save(p, quality=92)
