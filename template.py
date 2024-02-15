import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:,%(levelname)s:%(message)s')

project_name='cnnClassifier'

file_paths=[
    f'src/{project_name}/__init__.py',
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"templates/index.html",
    f"research/trial.ipynb",
    f"dvc.yaml",
    f"params.yaml",
    f"main.py",
    f"setup.py",
    f"requirements.txt",
    f"LICENSE",
    f"config/config.yaml",
    f".github/workflows/.gitkeep",
    f".gitignore"

]

for file_path in file_paths:
    path=Path(file_path)
    filedir,filename=os.path.split(path)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(file_path)) or(os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            logging.info(f'created {filename} for {filedir} directory')
    else:
        logging.info(f'already exists {filename} for {filedir} directory')