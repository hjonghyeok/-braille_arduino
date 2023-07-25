import numpy as np
import pytesseract as pt
import cv2
from PIL import Image
from hanspell import spell_checker
import re
# filename = 'test2.png'

# os.path.isfile(filename)

# image = cv2.imread(filename)
# rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# text = pytesseract.image_to_string(rgb_image, lang='kor')
# print(text)

img = Image.open('test2.png')
text = pt.image_to_string(img, lang='kor')

text = re.sub(r"\s", "", text)

spelled_sent = spell_checker.check(text)
hanspell_sent = spelled_sent.checked
#text = pt.image_to_string(image, config="-l kor")
print(hanspell_sent)
