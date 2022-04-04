from flask import Flask, render_template, request
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]
    cv = request.form["color"]
    ec = request.form["EC"]    

    if ec == "L":
        qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        )
        print('l')
    elif ec == "M":
        qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        )
        print('m')
    elif ec == "Q":
        qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        )
        print('q')
    elif ec == "H":
        qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        )
        print('h')
    else:
        qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        )
        print('default')

    qr.clear()
    qr.add_data(name)

    if cv == "Default":
        image = qr.make_image(fill_color="Black", back_color="White")
        print('Default')
    elif cv == "Color":
        image = qr.make_image(fill_color=request.form["picker"], back_color="White")
        print("color picker:" + request.form["picker"])
    elif cv == "GS":
        image = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
        print('GS')
    elif cv == "C":
        image = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
        print('C')
    elif cv == "R":
        image = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        print('R')
    elif cv == "VB":
        image = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
        print('VB')
    elif cv == "HB":
        image = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
        print('HB')
    else:
        image = qr.make_image(fill_color="Black", back_color="White")
        print('else')

    #image = qr.make_image()
    #image = qrcode.make(name) #QR Code stored in "image" variable with data inside brackets

    type(image)
    image.save("static/QRCode.jpg")
    return render_template("QR.html")

if __name__ == '__main__':
    app.run(debug = True,port=5001)