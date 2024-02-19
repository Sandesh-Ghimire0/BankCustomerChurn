import os
import sys
import dill

from src.exception import CustomError


def save_object(obj, obj_file_path):
    try:
        dir_path = os.path.dirname(obj_file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(obj_file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomError(e, sys)