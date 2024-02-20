import sys
import os
from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier

from src.exception import CustomError
from src.logger import logging
from src.utils import evaluate_models, save_object


@dataclass
class ModelTrainerConfig:
    model_obj_path:str = os.path.join('artifacts','model.pkl')
    model_report_path:str = os.path.join('artifacts','report.csv')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_arr, test_arr):
        try:
            logging.info("Model training initiated")
            X_train, X_test, y_train, y_test = (
                train_arr[:,:-1],
                test_arr[:,:-1],
                
                train_arr[:,-1],
                test_arr[:,-1]
            )

            models_dict ={
                'logistic_regression':LogisticRegression(),
                'decision_tree':DecisionTreeClassifier(),
                'random_forest':RandomForestClassifier(),
                'svm':SVC(),
                'KNN':KNeighborsClassifier(),
                'gradient_boosting':GradientBoostingClassifier(),
                'xgboost':XGBClassifier()
            }

            report = evaluate_models(X_train, X_test, y_train, y_test,models_dict)
            report.to_csv(self.model_trainer_config.model_report_path, index=False)
            logging.info("Models report generated")

            model= models_dict['gradient_boosting']

            save_object(
                obj=model,
                obj_file_path=self.model_trainer_config.model_obj_path
            )
            logging.info("Best Model saved as pkl file")
            
            
        except Exception as e:
            raise CustomError(e,sys)