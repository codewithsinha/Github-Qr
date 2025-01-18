import qrcode 
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 60,
    border = 5
)

data = "https://github.com/codewithsinha"

qr.add_data(data)
qr.make(fit = True )
img = qr.make_image(fill="black", back_color = "white")
img.save("test.png")