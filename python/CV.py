import serial
import time
from PIL import Image
import cv2
import pytesseract as pt
from hanspell import spell_checker
import re
 
ser = serial.Serial('/dev/ttyACM0', 9600)
 
cap = cv2.VideoCapture("test.mp4")
 

if cap.isOpened():
# 만약 카메라가 실행되고 있다면,
    ret, a = cap.read()
    # ret: True False value입니다.
    # a: 영상 프레임을 읽어옵니다.
 
    while ret:
    # 제대로 카메라를 불러왔다면~ 반복문을 실행합니다. 
        ret, a = cap.read()
        cv2.imshow("camera", a)
        # 이미지를 보여주는 방식과 같습니다.
        key = cv2.waitKey(1)

        if key == 27:
            break
        elif key == ord('x'):
            while 1:
                if ser.readable():
                    # img = Image.open(a)
                    text = pt.image_to_string(a, lang='kor')
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
                    break
        
 
cap.release()
cv2.destroyAllWindows()