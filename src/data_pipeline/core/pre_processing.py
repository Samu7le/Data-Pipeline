import polars as pl
from pathlib import Path
from data_pipeline.core.logger import logger

PATH_DATA_ENTRY = Path.joinpath(Path.cwd(), "data_acquisition")
class PreProcessor():

    def __init__(self, validator: list, path: str = PATH_DATA_ENTRY):
        logger.info(f"|PIPELINE| START")
        self.path = path
        self.validator = validator

    def fetch_files(self) -> list: 
        '''
        Docstring: fetch_files
        
        :return: list of all files inside entry-point folder
        :rtype: list
        '''
        files = []
        for file in Path.iterdir(self.path):
            logger.debug(f"DEBUG {file.name} type: {type(file)}")
            files.append(file.name) # name attribute return the file name instead of path object

        logger.info(f"|PIPELINE| Display files: {files}")
        logger.info(f"|PIPELINE| Number of files: {len(files)}")

        return files

    def header_checker(self, files : list, validator: list[str]) -> list:
        '''
        Docstring: header_checker

        :param files: list of files provided by data_acquisition_list function
        :type files: list
        :param validator: values of expected header
        :type validator: str
        :return: list of validated files (matched validator)
        :rtype: list
        '''
        sanitized = []
        for file in files:
            if '.csv' in file:
                logger.debug(f"pass for file: {file}")
                df_csv = pl.read_csv(f"{self.path}/{file}", try_parse_dates=True, n_rows=0)
                if df_csv.columns != validator: # TO-DO improve diff algorithm
                    logger.info(f"|PIPELINE| No matched : {file}")
                    continue
                sanitized.append(file)
        
        logger.info(f"|PIPELINE| Correct files: {sanitized}")

        return sanitized

    def show_preprocessed_data(self, files : list) -> None:
        '''
        Docstring: show_data
        
        :param files: list of validated files (matched validator)
        :type files: list
        '''
        for file in files:
            df_csv = pl.read_csv(f"{self.path}/{file}", try_parse_dates=True)
            print(f"\n {df_csv}")
