from PIL import Image
import os
base = r'C:\Users\HP\Desktop\心理html\assets\cases'
p = os.path.join(base, 'meaning.jpg')
# 重新从原图裁：原图2394x1664，只裁右边1.5%
# 先恢复：用之前裁过3%的图作为基础，右边少裁一点
im = Image.open(p)
w,h = im.size
print('current', im.size)
# 当前是2026x1472，已经裁太多了。重新从原始豆包图复制
