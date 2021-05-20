from pathlib import Path
from itertools import tee


class DiluteData:
    def __init__(self, csv_path, column_to_consider=0, delimiter=',', header=0):
        self.csv_path = csv_path
        self.column_to_consider = column_to_consider
        self.delimiter = delimiter
        self.header = header
        self.lines_with_header = []
        self.csv_it = self._open()

    def _open(self):
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

        # def fill(c):
        #     return c.split(self.delimiter)[self.column_to_consider] == consider_column
        # print(line for line in csv_it_copy if fill(line))

        for line in csv_it_copy:
            t = line.split(self.delimiter)[self.column_to_consider]
            if t == consider_column:
                yield line

    def __iter__(self):
        unique_columns_consider = list(set(self._get_columns()))
        for consider_column in unique_columns_consider:
            yield {consider_column: self._get_data(consider_column)}
