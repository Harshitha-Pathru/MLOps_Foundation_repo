import os
from pathlib import Path

print(Path("a/b/c.txt"))
#output-->a\b\c.txt

'''
Here stages of the pipeline goes--->plan > data > eda>  fe>build > evaluate /test > deploy > monitor and maintainence > retrain >..
Basic files required for every project, here we can automate the  files creation using listOfFiles 
To maintain pipeline i.e; training and prediction pipelines(stages)in where several components required, those are listed down below.
src>pipeline=mutilple components
'''

listOfFiles= [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",\
    "src/components/data_transformation.py",
    "src/components/model_trainer.py"
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]
print(listOfFiles)

for filepath in listOfFiles:
    filepath= Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        print(f'Creating directory:{filedir} for file:{filename}')
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #create an empty file




