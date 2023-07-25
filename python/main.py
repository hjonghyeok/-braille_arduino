import serial
import time
from PIL import Image
import cv2
import pytesseract as pt
from hanspell import spell_checker
import re

ser = serial.Serial('/dev/ttyACM0', 9600)


# while True:
if ser.readable():
    img = Image.open('test2.png')
    text = pt.image_to_string(img, lang='kor')
    text = re.sub(r"\s", "", text)
    spelled_sent = spell_checker.check(text)
    val = spelled_sent.checked
    # val = input("입력 : ")
    count = 0
    if len(val) <= 30:
        print(val)
        val = val.encode('utf-8')
        ser.write(val)
    else:
        for i in range(0, len(val), 30):
            print(val[i-30:i])
            vall = val[i-30 : i]
            vall = vall.encode('utf-8')
            ser.write(vall)
            a = input("dd : ")
            count = i
        val = val[count:]
        print(val)
        val = val.encode('utf-8')
        ser.write(val)
    # print("동작")
    # break