
# OCR reading will be done in this part
# Created by Ramazan AYDINLI

import easyocr

reader = easyocr.Reader(["ur"])
result = reader.readtext("C:\\Users\\METE\\Desktop\\image.png", detail=0)
sentence = ' '.join(result)
print(sentence)