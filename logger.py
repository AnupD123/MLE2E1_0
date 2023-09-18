import logging
import os
from datetime import datetime


LOG_FILE_NAME=f"log_{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_file_path=os.path.join(os.getcwd(),"Logs",LOG_FILE_NAME)
os.makedirs(log_file_path,exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_NAME,
    format="[%(asctime)s] %(lineno)d :: %(levelname)s :: %(message)s",
    level=logging.INFO)
