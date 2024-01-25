import os
from PIL import Image
from PIL import ImageColor

os.chdir('/Users/chanlim/Desktop')

cat = Image.open('zophie.png')
print(cat.size)
w, h = cat.size

print(w, h)

print(cat.filename)
print(cat.format)
print(cat.format_description)
cat.save('zophie.jpg')

im = Image.new('RGBA',(100,200), 'violet')
im.save('violet.png')
im2 = Image.new('RGBA', (20,20))
im2.save('transparent.png')

cropped = cat.crop((335,345,565,560))
cropped.save('cropped.png')

catcopy = cat.copy()
catcopy.paste(cropped, (0,0))
catcopy.paste(cropped, (336,344))

facew, faceh = cropped.size
copycat = cat.copy()

for left in range(0, w, facew):
    for top in range(0,h,faceh):
        print(left, top)
        copycat.paste(cropped,(left,top))

copycat.save('copycat.png')


quartersize = cat.resize((w//2, h+1000)).rotate(90, expand=True).transpose(Image.FLIP_TOP_BOTTOM)

quartersize.save('quarter.png')

im = Image.new('RGBA', (808,768))

for x in range(808):
    for y in range(384):
        im.putpixel((x,y),(255,0,0,255))
        im.putpixel((x,y+384),ImageColor.getcolor('blue', 'RGBA'))

im.save('putpixel.png')

bgd = Image.open('putpixel.png')
logo = Image.open('catlogo.png')

w,h = logo.size

print(w,h,type(x),type(y))

for x in range(w):
    for y in range(h):
        print(logo.getpixel((x,y)))
        if logo.getpixel((x,y)) == (0,0,0,255):
            bgd.putpixel((x,y),ImageColor.getcolor('black','RGBA'))

bgd.save('logo_added.png')

