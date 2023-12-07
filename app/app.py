from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates # Jinja2-Templates
from app.utils import text_to_speech, lang_converter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get('/')
def Home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/', response_class=HTMLResponse)
def Convert(request: Request, text: str = Form(...), lang: str= Form(...)):
    if not text or not lang:
        return templates.TemplateResponse('error.html', {'request': request}, status_code=400)
    try:
        lang = lang[0:2]
        if lang == 'kn':
            text_to_speech(lang_converter(text, lang), lang)
            return templates.TemplateResponse("index.html", {"request": request})
        elif lang == 'hi':
            text_to_speech(lang_converter(text, lang), lang)
            return templates.TemplateResponse("index.html", {"request": request})
        elif lang == 'mr':
            text_to_speech(lang_converter(text, lang), lang)
            return templates.TemplateResponse("index.html", {"request": request})
        else:
            lang == 'en'
            text_to_speech(text, lang)
            return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        print(e)
        return templates.TemplateResponse('error.html', {'request': request}, status_code=500)
    
    
