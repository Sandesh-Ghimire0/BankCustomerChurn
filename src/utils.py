import os
import sys
import dill


from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score,confusion_matrix
import pandas as pd

from src.exception import CustomError


def save_object(obj, obj_file_path):
    try:
        dir_path = os.path.dirname(obj_file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(obj_file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomError(e, sys)
    

def evaluate_models(X_train, X_test, y_train, y_test, models):
    report = {}
    
    for i in range (len(models)):
        model = list(models.values())[i]
        
        model.fit(X_train, y_train)
        
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        training_accuracy = accuracy_score(y_train,y_pred_train)
        test_accuracy = accuracy_score(y_test, y_pred_test)
        precision = precision_score(y_test, y_pred_test)
        recall = recall_score(y_test, y_pred_test)
        f1score = f1_score(y_test, y_pred_test)
        
        report[list(models.keys())[i]] = [training_accuracy,test_accuracy,precision,recall,f1score]
    
        report_df = pd.DataFrame.from_dict(data=report,orient='index').reset_index()
        report_df.rename(columns={
            'index':'models',
            0:'training_accuracy',
            1:'test_accuracy',
            2:'f1_score',
            3:'precision',
            4:'recall'
        },inplace=True)
        
    return report_df


def load_object(obj_path):
    try:
        with open(obj_path, 'rb') as file_obj:
            obj =dill.load(file_obj)

        return obj
    
    except Exception as e:
        CustomError(e,sys)

        