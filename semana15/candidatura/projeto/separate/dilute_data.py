from abc import ABC, abstractmethod
from pathlib import Path
from itertools import tee


class AbstractDiluteData(ABC):
    @abstractmethod
    def _extract(self):
        """
        Method to extract data from source
        Returns -> Iterable
        """
        pass

    def _get_columns(self):
        """
        Method to extract get all values from consider_column
        Returns -> Generator
        """
        pass

    def _get_data(self, consider_column):
        """
        Method to fill data from iterable using consider_column
        Returns -> Generator
        """
        pass

    @abstractmethod
    def __iter__(self):
        """
        Method to iter in uniqued values from columns_consider
        Returns -> Generator {key:value}
        """
        pass


class DiluteDataCsv(AbstractDiluteData):
    """
    class to fill and distinct data from csv file

    Parameters
    ----------
    csv_path : str, path object or file-like object
        Any valid string path is acceptable. 

    column_to_consider : int, default '0'
        column from csv to consider in separate data

    delimiter : str, default ``None``
        Alias for sep.

    header : int, default '0'
        Row number(s) to use as the header, and the start of the
        data. 
    """

    def __init__(self, csv_path, column_to_consider=0, delimiter=',', header=0):
        self.csv_path = csv_path
        self.column_to_consider = column_to_consider
        self.delimiter = delimiter
        self.header = header
        self.lines_with_header = []
        self.csv_it = self._extract()

    def _extract(self):
        if Path(self.csv_path).is_file():
            fp = open(self.csv_path, 'r')
            for n in range(self.header):
                next(fp)
                # self.lines_with_header.extend(headerline for headerline in fp)
            return fp
        raise Exception("Invalid csv_path location")

    def _get_columns(self):
        self.csv_it, csv_it_copy = tee(self.csv_it)
        for line in csv_it_copy:
            yield line.split(self.delimiter)[self.column_to_consider]

    def _get_data(self, consider_column):
        self.csv_it, csv_it_copy = tee(self.csv_it)
        for line in csv_it_copy:
            t = line.split(self.delimiter)[self.column_to_consider]
            if t == consider_column:
                yield line

    def __iter__(self):
        unique_columns_consider = list(set(self._get_columns()))
        for consider_column in unique_columns_consider:
            yield {consider_column: self._get_data(consider_column)}
