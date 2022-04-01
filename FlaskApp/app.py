from flask import Flask, render_template, request
import qrcode
import time

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST', "GET"])
#@app.route("/home", methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]

    #print(name)
    #dataName = input("Enter a link for your QR Code: ")
    image = qrcode.make(name) #QR Code stored in "image" variable with data inside brackets

    type(image)
    image.save("static/QRCode.jpg")

    #time.sleep(3)
    
    return render_template("QR.html")
    #return render_template("index.html")
    #return render_template("index.html", name = name)




if __name__ == '__main__':
    app.run(debug = True,port=5001)