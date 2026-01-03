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
I use the new standard src layout
## Project Structure

```text
DATA_PIPELINE/
├── src/
│   └── data_pipeline/                                      <-- Main package root
│       ├── __init__.py                                     <-- Package initializer (exposes core classes)
│       ├── jobs/                                           <-- Executable scripts and task definitions
│       │   ├── __init__.py                             
│       │   └── job_test.py                             
│       ├── logs/                                           <-- Directory for runtime log files
│       │   └── pipeline.log                                
│       └── core/                                           <-- Core logic and utility modules
│           ├── __init__.py                             
│           ├── logger.py                                   <-- Logging configuration
│           └── pre_processing.py                           <-- class with methods to pre processing data
├── data_acquisition/                                       <-- Raw input data (CSV, TXT, etc.)
├── venv/                                                   <-- Python virtual environment
├── .gitignore                                              
├── pyproject.toml                                          <-- Build system and dependency configuration
└── README.md                                               
```
- **data_acquisition**: the enry poit of each dataset -> raw data
- **jobs**: scripts of each data jobs to process different kind of transformation   and data validation
- **logs**: logs of each job
- **core**: the main folder of the project, contains the classes to perform Preprocessing -> Validation -> Transformation -> Load