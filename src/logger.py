import logging
import os
from datetime import datetime

LOG_FILE_NAME=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR_PATH=os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_DIR_PATH,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,


)

# if __name__ == "__main__":
#     logging.info("logging is working")