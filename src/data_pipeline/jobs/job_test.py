from data_pipeline import PreProcessor

VALIDATOR = ['Name','Age','Gender','Blood Type','Medical Condition','Date of Admission','Doctor',
             'Hospital','Insurance Provider','Billing Amount','Room Number','Admission Type',
             'Discharge Date','Medication','Test Results']

test = PreProcessor(VALIDATOR)
dataset = test.fetch_files()
sanitazide = test.header_checker(dataset, VALIDATOR)
test.show_preprocessed_data(sanitazide)
