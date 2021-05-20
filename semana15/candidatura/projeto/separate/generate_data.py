from abc import ABC, abstractmethod
from pathlib import Path


class AbstractGenerateData(ABC):
    """ Class to generate final file data
    ----------
    Parameters
    path_file : str, path object or file-like object
        Any valid string path is acceptable. 
    """

    def __init__(self, path_file):
        if not Path(path_file).is_dir():
            raise Exception("Invalid file path")
        self.path_file = path_file

    @abstractmethod
    def generate_data(self):
        pass


class GenerateDataCsv(AbstractGenerateData):
    def generate_data(self, file_name, data, header=None):
        """ Generate csv with final data """
        with open(f'{self.path_file}/{file_name}.csv', 'w') as csvfile:
            if header:
                csvfile.write(header)
            csvfile.writelines(data)
        return True
