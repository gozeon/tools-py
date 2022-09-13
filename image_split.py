from PIL import Image

im = Image.open("2022-09-09_112659.png")
width, height = im.size

copies = 6
step  = height // copies
alist = []

# 垂直切割
for n in range(copies):
    top = n * step
    bottom = (n + 1) * step
    if n == copies-1 and bottom != height:
        bottom = height
    newIm = im.crop((0, top, width, bottom))
    newIm.save("{}.png".format(n+1))

