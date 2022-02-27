import cv2

fileName = "QRCode.png"         #Name of the image that should be a QR Code
image = cv2.imread(fileName)    #Using the CV2 library, read image
detector = cv2.QRCodeDetector() #Initalizing CV2 QRCode Detector to ensure image quality
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)   #Using the detectors Detect and Decode function

if vertices_array is not None:  
    print("QRCode Data: ", data)
else:
    print("Image wasn't detected as QR Code")