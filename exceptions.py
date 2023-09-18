
import sys
from logger import logging


def cst_report_error_msg(error_msg,error_detail:sys):
    a,b,c=error_detail.exc_info()
    err_filename=c.tb_frame.f_code.co_filename
    err_msg1="Error has occured at [{0}] file and [{1}]".format(err_filename,error_msg)
    print(err_msg1)
    return err_msg1
    
class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        logging.info("Exception [{0}] occured".format(error_msg))
        self.error_msg=cst_report_error_msg(error_msg=error_msg,error_detail=error_detail)
        super().__init__( error_msg)
        
    
if __name__=="__main__":
    try:
        if 1/0:
            print ("Yo")
    except Exception as e:
        raise CustomException(e, sys)