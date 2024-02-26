import sys
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from src.exception import CustomError


app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/')
async def home(request:Request):
    return templates.TemplateResponse('index.html',{'request':request})

@app.route('/predict',methods=['GET','POST'])
async def prediction(request:Request):
    try:
        if request.method == 'GET':
            return templates.TemplateResponse('form.html',{'request':request})

        else:
            pass

    except Exception as e:
        raise CustomError(e,sys)