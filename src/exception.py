import sys


def get_error_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomError(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_detail(error=error_message, error_detail=error_detail)

    # it is used to returns a human-readable, or informal, string representation of an object
    # prints the error_message whenever CustomError is raised i.e CustomError object is created
    def __str__(self):
        return self.error_message