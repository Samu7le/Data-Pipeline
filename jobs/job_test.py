import sys
import os

from utility.pre_processing import PreProcessor
from utility.logger import logger

# ----------------------------------------------------------- TO-DO MOVE TO EXTERNAL FILE
PATH_DATA_ENTRY = "C:\\Users\\Samue\\Desktop\\learning\\data_pipeline\\data_acquisition" # improve reliability and reproducibility with external file

VALIDATOR = ['Name','Age','Gender','Blood Type','Medical Condition','Date of Admission','Doctor',
             'Hospital','Insurance Provider','Billing Amount','Room Number','Admission Type',
             'Discharge Date','Medication','Test Results']

test = PreProcessor(PATH_DATA_ENTRY, VALIDATOR)
test.data_counter()
dataset = test.data_acquition_list(PATH_DATA_ENTRY)
sanitazide = test.header_checker(PATH_DATA_ENTRY, dataset, VALIDATOR)
test.show_data(PATH_DATA_ENTRY, sanitazide)