import os
import sys
from dataclasses import dataclass

import pandas as pd 
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomError
from src.components.data_transformation import DataTransformer
from src.components.model_trainer import ModelTrainer


# gives the name of the path where the data shold be stored
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')


'''
This class collects the data from source and 
creates the train and test data
'''
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            #collecting the data and storing it
            logging.info("Data ingestion started")
            data = pd.read_csv('notebook\data\Customer-Churn-Records.csv')
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok = True)   
            data.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            logging.info("Data collected from source and train test split initiated")
            # creating the train and test data and storing it
            train_data , test_data = train_test_split(data, test_size=0.2, random_state=42)
            train_data.to_csv(self.data_ingestion_config.train_data_path, index = False)
            test_data.to_csv(self.data_ingestion_config.test_data_path, index= False)

            logging.info("Data ingestion completed")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )



        except Exception as e:
            raise CustomError(e,sys)



