import os
import sys

import numpy as np 
import pandas as pd 

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


from src.logger import logging
from src.exception import CustomError
from dataclasses import dataclass
from src.utils import save_object


@dataclass
class DataTranformerConfig:
    preprocessor_obj_path:str = os.path.join('artifacts','preprocessor.pkl')


class DataTransformer:
    try:
        def __init__(self):
            self.data_transformer_config = DataTranformerConfig()

        
        def get_preprocessor_object(self):
            num_pipeline_scaling = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='mean')),
                ('scaler',StandardScaler())
            ])
        
            cat_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoding',OneHotEncoder(sparse_output=False)),
                ('scaler',StandardScaler())
            ])
        
            num_pipeline_missing = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('scaler',StandardScaler())
            ])
            
        
            num_columns_scaling = ['CreditScore','Age','Balance','EstimatedSalary']
            num_columns_missing = ['Tenure','NumOfProducts','HasCrCard','IsActiveMember','Complain','EstimatedSalary','Satisfaction Score']
            cat_columns = ['Geography','Gender','Card Type']
            
            
            preprocessor = ColumnTransformer(
                [
                    ('num_columns_missing',num_pipeline_missing, num_columns_missing),
                    ('num_columns_scaling',num_pipeline_scaling,num_columns_scaling),
                    ('cat_columns',cat_pipeline, cat_columns)
                ]
            )
            logging.info("preprocessor object created")
        
            return preprocessor
    
    except Exception as e:
        raise CustomError(e,sys)

    
    def get_transformed_data(self,train_path, test_path):
        try:
            logging.info("Data transformation initiated")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            train_input_features = train_df.drop(columns=['Exited'])
            test_input_features = test_df.drop(columns=['Exited'])
            
            
            preprocessor = self.get_preprocessor_object()
            
            train_input_features_arr = preprocessor.fit_transform(train_input_features)
            test_input_features_arr = preprocessor.transform(test_input_features)
            logging.info("Train and test data transformed")

            save_object(
                obj=preprocessor,
                obj_file_path=self.data_transformer_config.preprocessor_obj_path
            )
            logging.info("preprocessor object saved")

            target_column = 'Exited'
            train_target = train_df[target_column]
            test_target = test_df[target_column]
            
            train_features_arr = np.c_[
                train_input_features_arr,np.array(train_target)
            ]
            
            test_features_arr = np.c_[
                test_input_features_arr, np.array(test_target)
            ]
            
            logging.info("Train array and test array created")
            return (
                train_features_arr,
                test_features_arr,
                self.data_transformer_config.preprocessor_obj_path

            )
        

        except Exception as e:
            raise CustomError(e,sys)
