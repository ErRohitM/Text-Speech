import gtts
import os
from translate import Translator

def text_to_speech(text: str, lang: str):
    if text:
        os.remove('app/static/speak.mp3')
    tts = gtts.gTTS(text, lang = lang)
    tts.save('app/static/speak.mp3')

    
    
def lang_converter(text, lang):
    translator= Translator(to_lang=lang)
    translation = translator.translate(text)
    return translation
            

            