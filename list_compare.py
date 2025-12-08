import polars as pl
from utility.pre_processing import PreProcessor

path = "C:\\Users\\Samue\\Desktop\\learning\\data_pipeline\\data_acquisition\\healthcare_dataset.csv"
validator = ['Name','Age','Gender','Blood Type','Medical Condition','Date of Admission','Doctor',
             'Hospital','Insurance Provider','Billing Amount','Room Number','Admission Type',
             'Discharge Date','Medication','Test Results']

df_csv = pl.read_csv(path, try_parse_dates=True)
columns = df_csv.columns

print(columns)
print(validator)

if columns == validator:
    print("same")