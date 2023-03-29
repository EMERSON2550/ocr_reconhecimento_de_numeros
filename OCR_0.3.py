import numpy as np


import cv2
import pytesseract
img = cv2.imread('Curso_OCR/Aluas/116d7b41fff92f0a671320d0d0a3b80d.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
erosao = cv2.erode(gray, np.ones((5, 5), np.uint8))
val, thresh = cv2.threshold(erosao, 180, 255, cv2.THRESH_BINARY_INV)
config_tesseract = '--tessdata-dir tessdata --psm 7 -c tessedit_char_whitelist=0123456789'
resultado = pytesseract.image_to_string(thresh, lang="por", config=config_tesseract)
print(resultado)
