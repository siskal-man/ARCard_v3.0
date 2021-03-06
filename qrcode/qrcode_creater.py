import pyqrcode
from PIL import Image

# Generate the qr code and save as png
qrobj = pyqrcode.create('https://codirovshik.github.io/ARCard/index.html')
with open('test.png', 'wb') as f:
    qrobj.png(f, scale=15)

# Now open that png image to put the logo
img = Image.open('./qrcode/test.png')
img = img.convert("RGBA")

width, height = img.size

# How big the logo we want to put in the qr code png
logo_size = 220

# Open the logo image

img.show()
img.save(fp="./qrcode/qrcode.png")
