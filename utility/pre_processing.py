import polars as pl
import os
from utility.logger import logger

class PreProcessor():

    def __init__(self, path, validator):
        logger.info(f"|PIPELINE| START")
        self.path = path
        self.validator = validator

    def data_counter(self) -> int:
        '''
        Docstring: data_counter
        
        :param path: path of folder entry-point data files
        :type path: str
        :return: number of files inside entry-point folder
        :rtype: int
        '''
        counter = 0
        for _ in os.scandir(self.path):
            counter += 1

        logger.info(f"|PIPELINE| Number of files: {counter}")

        return counter
    
    def data_acquition_list(self, path: str) -> list: #TO-DO CHECK FILE EXTENSIONS IF IT'S .CSV
        '''
        Docstring: data_acquition_list
        
        :param path: path of folder entry point data files
        :type path: str
        :return: list of all files inside entry-point folder
        :rtype: list
        '''
        files = []
        for file in os.listdir(path):
            files.append(file)

        logger.info(f"|PIPELINE| Display files: {files}")

        return files

    def header_checker(self, path: str, files : list, validator: str) -> list:
        '''
        Docstring: header_checker
        
        :param path: path of folder entry point data files
        :type path: str
        :param files: list of files provided by data_acquisition_list function
        :type files: list
        :param validator: values of expected header
        :type validator: str
        :return: list of validated files (matched validator)
        :rtype: list
        '''
        sanitized = []
        for file in files:
            df_csv = pl.read_csv(f"{path}/{file}", try_parse_dates=True)
            if df_csv.columns != validator: # TO-DO improve diff algorithm
                logger.info(f"|PIPELINE| No matched : {file}")
                continue
            sanitized.append(file)
        
        logger.info(f"|PIPELINE| Correct files: {sanitized}")

        return sanitized

    def show_data(self, path: str, files : list) -> None:
        '''
        Docstring: show_data
        
        :param path: path of folder entry point data files
        :type path: str
        :param files: list of validated files (matched validator)
        :type files: list
        '''
        for file in files:
            df_csv = pl.read_csv(f"{path}/{file}", try_parse_dates=True)
            # print(f"file: {file} | columns: {df_csv.columns}")
            print(f"\n {df_csv}")
