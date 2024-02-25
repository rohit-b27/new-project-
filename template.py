import os
from  pathlib import Path
import logging

while True:
    project_name=input("Enter project name: ")
    if project_name != "":
        break
    
logging.basicConfig(level=logging.INFO, format ='[%(asctime)s]:%(message)s:' ) 

list_of_files={
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/constanst/__init__.py",
    "setup.py",
    "main.py",
    "app.py",
    "requirements.txt"    
}

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if ((not os.path.exists(filepath)) or (os.path.getsize(filepathn) ==0)):
       with open(filepath,"w") as f:
           pass
           logging.info("creating new file, {filepath}")
        
    else:
        logging.info("file already exists,{filepath}")
        
    

   
    
