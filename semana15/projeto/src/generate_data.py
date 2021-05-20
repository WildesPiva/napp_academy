from pathlib import Path


class GenerateData():
    def __init__(self, path_file):
        if not Path(path_file).is_dir():
            raise Exception("Invalid file path")
        self.path_file = path_file

    def generate_csv(self, file_name, data, header=None):
        with open(f'{self.path_file}/{file_name}.csv', 'w') as csvfile:
            if header:
                csvfile.write(header)
            csvfile.writelines(data)
