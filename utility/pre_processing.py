import polars as pl
import os
from logger import logger

# ----------------------------------------------------------- TO-DO MOVE TO EXTERNAL FILE
PATH_DATA_ENTRY = "C:\\Users\\Samue\\Desktop\\learning\\data_pipeline\\data_acquisition" # improve reliability and reproducibility with external file

validator = ['Name','Age','Gender','Blood Type','Medical Condition','Date of Admission','Doctor',
             'Hospital','Insurance Provider','Billing Amount','Room Number','Admission Type',
             'Discharge Date','Medication','Test Results']

def data_counter(path: str) -> int:
    counter = 0
    for _ in os.scandir(path):
        counter += 1
    return counter

def data_acquition_list(path: str) -> list: #TO-DO CHECK FILE EXTENSIONS IF IT'S .CSV
    files = []
    for file in os.listdir(path):
        files.append(file)
    return files

data_count = data_counter(PATH_DATA_ENTRY)
logger.info(f"|PIPELINE| Counter : {data_count}")

files = data_acquition_list(PATH_DATA_ENTRY)
for file in files:
    logger.info(f"|PIPELINE| Content : {file}")

def header_checker(path: str, files : list, validator: str) -> None:
    sanitized = []
    for file in files:
        df_csv = pl.read_csv(f"{path}/{file}", try_parse_dates=True)
        if df_csv.columns != validator: # TO-DO improve diff algorithm
            logger.info(f"|PIPELINE| No matched : {file}")
            continue
        sanitized.append(file)

def show_data(path: str, files : list) -> None:
    for file in files:
        df_csv = pl.read_csv(f"{path}/{file}", try_parse_dates=True)
        # print(f"file: {file} | columns: {df_csv.columns}")
        print(f"\n {df_csv}")

header_checker(PATH_DATA_ENTRY, files, validator)
#show_data(PATH_DATA_ENTRY, files)

# TO-DO
# 2) Evolve this script into a Class to handle multi flux data
# 3) Create a config.py file
