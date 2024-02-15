import os
import logging
import sys

logging_style='[%(asctime)s:%(levelname)s:%(message)s]'
log_dir='logs'
log_filepath=os.path.join(log_dir,'running_logs.dir')
os.makedirs(log_filepath,exist_ok=True)

logging.basicConfig(level=logging.INFO,
                    format=logging_style,
                    
                    handlers=[
                        logging.FileHandler(log_filepath),
                        logging.StreamHandler(sys.stdout)
                    ])
logger=logging.getLogger('cnnClassifierLogger')