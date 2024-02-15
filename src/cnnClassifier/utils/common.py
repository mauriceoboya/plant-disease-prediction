import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import joblib
import base64

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """ reads yaml file and returns
    Args:
        path_to_yaml(str):path like input
    Raises:
        valueError 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} load successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at:{path}")
  
@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path) as f:
        content=json.load(f)

    logger.info(f"json loaded successfully form:{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary saved at:{path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info(f"binary loaded from:{path}")
    return data


@ensure_annotations
def get_size(path:Path)->str:
    size=round(os.path.getsize(path)/1024)
    return f'~ {size} kB'

def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(filename):
    with open(filename,'rb') as f:
        return base64.b64encode(f.read())