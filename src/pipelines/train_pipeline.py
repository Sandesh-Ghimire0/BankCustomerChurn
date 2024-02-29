
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformer
from src.components.model_trainer import ModelTrainer

from src.exception import CustomError


class TrainPipeline:
    def __init__(self):
        pass

    def train(self): 
        try:
            data_ingestion_obj = DataIngestion()
            train_path, test_path = data_ingestion_obj.initiate_data_ingestion()

            data_transformation_obj = DataTransformer()
            train_arr, test_arr,_ = data_transformation_obj.get_transformed_data(train_path, test_path)

            model_trainer = ModelTrainer()
            model_trainer.initiate_model_training(train_arr, test_arr)

        except Exception as e:
            raise CustomError(e,sys)