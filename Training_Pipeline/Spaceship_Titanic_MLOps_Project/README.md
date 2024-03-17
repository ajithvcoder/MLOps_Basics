# Spaceship_Titanic_MLOps_Project

Predict which passengers are transported to an alternate dimension

https://www.kaggle.com/competitions/spaceship-titanic/discussion/309323

Data ingestion:
- Connect with cassandra database (CSQL model)
Prepare base model
Model training
Model evaluation

DVC dag
DVC repro

Tensorboard:
tensorboard --logdir artifacts\\prepare_callbacks\\tensorboard_log_dir

Any questions?

----------------------------
new conda environment 
    - conda create -n trainingpipeline1 python=3.10

create template.py 

fill utils/common.py , add logger to utils/__init__.py , titanicSpaceShip/constants/__init__.py

update setup.py 

requirements.txt

trails.ipynb 

01_data_ingestion.ipynb - "if logger is not importing restart it"

copy to enitity/
components/
configuration.py
pipeline.py 
then main.py

if its a configBox problem check config.yaml 

repeat for everything 

then for dvc 

dvc init
dvc repro
dvc dag 
no need flask here 

