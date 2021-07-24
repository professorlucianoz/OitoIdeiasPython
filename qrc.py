import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data("google.com")
qr.make()

img = qr.make_image()
img.save("qr.jpg")