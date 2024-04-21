import gtts
import os
from translate import Translator
# from PIL import Image
# import pytesseract
# import numpy as np
# import cv2

def text_to_speech(text: str, lang: str):
    if text:
        os.remove('app/static/speak.mp3')
    tts = gtts.gTTS(text, lang = lang)
    tts.save('app/static/speak.mp3')

    
    
def lang_converter(text, lang):
    translator= Translator(to_lang=lang)
    translation = translator.translate(text)
    return translation

def image_to_txt(*args, **kwargs):
    filename = 'img1.jpeg'
    img = np.array(Image.open(filename))

    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)
    # img1 = np.array(Image.open(filename))
    # img = cv2.imread('ff.png', cv2.IMREAD_GRAYSCALE)
    # norm_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    # return norm_img

    text = pytesseract.image_to_string(img)
    return text

            

            