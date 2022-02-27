import qrcode

dataName = input("Enter a link for your QR Code: ")
image = qrcode.make(dataName) #QR Code stored in "image" variable with data inside brackets

type(image)
image.save("QRCode.png")
