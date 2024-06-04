from src.customer_reader import CustomerReader
import os


class CsvCustomerReader(CustomerReader):

    def __init__(self):
        data_directory = os.getenv('DATA_DIRECTORY')
        source_file = os.getenv('INPUT_FILE')
        self.file_path = data_directory + '/' + source_file

    def read(self) -> list:
        file = open(self.file_path, "r")
        print(file.read())
        return []
