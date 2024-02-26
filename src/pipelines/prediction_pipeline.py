import sys
import os

import pandas as pd

from src.exception import CustomError
from src.utils import load_object


class PredictionPipeline:
    def __init__(self):
        pass
    try:
        def predict(self,input):
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            transformed_input = preprocessor.transform(input)
            output = model.predict(transformed_input)

            return output
        
    except Exception as e:
        raise CustomError(e,sys)

class InputData:
    def __init__(
            self,
            credit_score:str,
            geography:str,
            gender:str,
            age:int,
            tenure:int,
            balance:int,
            num_of_products:int,
            has_cr_card:int,
            is_active_member:int,
            estimated_salary:int,
            complain:int,
            satisfaction_score:int,
            card_type:int,
            point_earned:int

    ):
        self.credit_score= credit_score
        self.geography = geography
        self.gender= gender
        self.age = age
        self.tenure = tenure
        self.balance = balance
        self.num_of_products = num_of_products
        self.has_cr_card = has_cr_card
        self.is_active_member = is_active_member
        self.estimated_salary = estimated_salary
        self.complain = complain
        self.satisfaction_score = satisfaction_score
        self.card_type = card_type
        self.point_earned = point_earned


    
    def get_input_as_dataframe(self):
        try:
            input_dict = {
                'CreditScore':[self.credit_score],
                'Geography':[self.geography],
                'Gender':[self.gender],
                'Age':[self.age],
                'Tenure':[self.age],
                'Balance':[self.balance],
                'NumOfProducts': [self.num_of_products], 
                'HasCrCard' : [self.has_cr_card], 
                'IsActiveMember' : [self.is_active_member], 
                'EstimatedSalary' : [self.estimated_salary],
                'Complain' : [self.complain], 
                'Satisfaction Score' : [self.satisfaction_score], 
                'Card Type' : [self.card_type],
                'Point Earned':[self.point_earned]

            }

        except Exception as e:
            raise CustomError(e,sys)