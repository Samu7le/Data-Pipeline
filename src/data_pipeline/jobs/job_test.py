import sys
import os

from data_pipeline import PreProcessor

VALIDATOR = ['Name','Age','Gender','Blood Type','Medical Condition','Date of Admission','Doctor',
             'Hospital','Insurance Provider','Billing Amount','Room Number','Admission Type',
             'Discharge Date','Medication','Test Results']

test = PreProcessor(VALIDATOR)
test.data_counter()
dataset = test.data_acquition_list()
sanitazide = test.header_checker(dataset, VALIDATOR)
test.show_data(sanitazide)
