from flask import Flask, render_template, url_for, redirect, request
import os
import cv2
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/encoder")
def encoder():
    return render_template("encoder.html")

@app.route('/encoded', methods=["GET", "POST"])
def encoded():
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
        error_correction=qrcode.constants.ERROR_CORRECT_H,
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

    type(image)
    image.save("static/QRCode.jpg")
    return render_template('encoded.html')


@app.route("/decoder", methods=["GET", "POST"])
def decoder():
    data = None     #Argument gets passed, needs to be defined before if statements

    if request.method == "POST":    #If we are trying to post

        if request.files != None:           #More specifically, if we are trying to input files

            image = request.files["image"]
            if image.filename != "":        #Makes sure that a file is saved
                image.save('static/' + image.filename) #Saves image in current directory

                print(image)    #Test purposes

                image = cv2.imread('static/' + image.filename)      #Using the CV2 library, read image
                detector = cv2.QRCodeDetector()                      #Initalizing CV2 QRCode Detector to ensure image quality
                data, vertices_array, binary_qrcode = detector.detectAndDecode(image)   #Using the detector's Detect and Decode function

                if vertices_array is not None:  
                    print("QRCode Data: ", data)
                else:
                    data = "Image wasn't detected as QR Code"   #To fix error screen
                    print("Image wasn't detected as QR Code")

    return render_template("decoder.html", link=data)

if __name__ == "__main__":
    app.run(debug=True)