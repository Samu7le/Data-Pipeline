# DATA-PIPELINE

## Goals and Workflow
To understand how to create a robust and resilient data pipeline in Python, I teamed up to learn new libraries, like polars, but also to improve my design and programming skills.
I chose the OOP paradigm, to abstract components as building blocks.
In this section, you'll find the organization of the project's architecture; in short, the goal is to execute **ETL**: **Extract** -> **Transform** -> **Load**

The script **job_test.py** describe the workflow: first declare and entry data folder, second validate the header of .csv and then make the magic

## Installation
1. clone the project
```
git clone https://github.com/Samu7le/Data-Pipeline.git 
```
2. create python virtual env
```
python -m venv venv 
``` 
3. activate python virtual env
```
.\venv\Scripts\activate                                                        #Windows 
``` 
```
source venv/bin/activate                                                    #unix-like
``` 
4. mv to the root folder of the project (where you found the file pyproject.toml) and esecute command
```
pip install -e . 
``` 
## Usage
To run the test job, execute:
```
python src/data_pipeline/jobs/job_test.py
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