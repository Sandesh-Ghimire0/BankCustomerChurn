import sys
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from BankChurn import BankChurn

from src.exception import CustomError
from src.pipelines.prediction_pipeline import InputData, PredictionPipeline


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
            data = await request.form()

            input_data = InputData(
                credit_score = data['credit_score'],
                geography = data['geography'],
                gender = data['gender'],
                age = data['age'],
                tenure = data['tenure'],
                balance = data['balance'],
                num_of_products = data['num_of_products'],
                has_cr_card = data['has_cr_card'],
                is_active_member = data['is_active_member'],
                estimated_salary = data['estimated_salary'],
                complain = data['complain'],
                satisfaction_score = data['satisfaction_score'],
                card_type = data['card_type'],
                point_earned = data['point_earned']
            )

            pred_df = input_data.get_input_as_dataframe()

            prediction_pipeline = PredictionPipeline()
            result = prediction_pipeline.predict(pred_df)
            if result == 1.0:
                result = "Exit"
            else:
                result = "not Exit"

            return templates.TemplateResponse('form.html',{'request':request,'result':result})



    except Exception as e:
        raise CustomError(e,sys)
    

if __name__ =="__main__":
    uvicorn.run()