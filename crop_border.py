from PIL import Image
import os
cases = ['empty','socialanx','impostor','numb','meaning']
base = r'C:\Users\HP\Desktop\心理html\assets\cases'
for c in cases:
    p = os.path.join(base, c+'.jpg')
    im = Image.open(p)
    w,h = im.size
    crop = im.crop((int(w*0.03), int(h*0.03), int(w*0.97), int(h*0.97)))
    crop.save(p, quality=92)
    print(c, im.size, '->', crop.size)
