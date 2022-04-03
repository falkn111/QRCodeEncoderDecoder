from flask import Flask, render_template, url_for, redirect, request
import os
import cv2
import qrcode

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

    image = qrcode.make(name) #QR Code stored in "image" variable with data inside brackets
    type(image)
    image.save("static/QRCode.jpg")
    return render_template('encoded.html')


@app.route("/decoder", methods=["GET", "POST"])
def decoder():
    data = None     #Argument gets passed, needs to be defined before if statements

    if request.method == "POST":    #If we are trying to post

        if request.files:           #More specifically, if we are trying to input files

            image = request.files["image"]
            image.save('static/' +  image.filename) #Saves image in current directory

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
    app.run(debug=False)
