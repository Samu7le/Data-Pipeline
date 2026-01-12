# DATA-PIPELINE

## Goals and Workflow
In order to understand how create a robust and resilient data-piline in python I put togheter aspire to learn new library, like polars, but also improve design and programming skill.
I choose OOP paradign, to abstract the componets like bricks.
Under this section you find the architecture organization of the project, in simple term the goal is to perform **ETL**: **Extract** -> **Transform** -> **Load**

The script **job_test.py** describe the workflow: first declare and entry data folder, second validate the header of .csv and then make the magic

## Installation
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