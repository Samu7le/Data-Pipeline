# DATA-PIPELINE

## This is a side project to improve design skill in data-pipeline creation

1. create python virtual env
```
python -m venv venv 
``` 
2. activate python virtual env
```
.\venv\Script\activate                                                        #Windows 
``` 
```
source venv/bin/activate                                                    #unix-like
``` 
3. mv to the root of the project and esecute command
```
pip install -e . 
``` 

## Architecture

### Folders Structure 
- **data_acquisition**: the enry poit of each dataset -> raw data
- **jobs**: scripts of each data jobs to process different kind of transformation   and data validation
- **logs**: logs of each job
- **utility**: the main folder of the project, contains the classes to perform Preprocessing -> Validation -> Transformation -> Load