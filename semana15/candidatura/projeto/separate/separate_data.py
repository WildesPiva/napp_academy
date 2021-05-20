from projeto.separate.dilute_data import DiluteDataCsv
from projeto.separate.generate_data import GenerateDataCsv


class SeparateCsvData():
    def __init__(
        self,
        kwargs_dilute,
        kwargs_generate,
        prefix_final_filename='separeted'
    ) -> None:
        self.dilution = DiluteDataCsv(**kwargs_dilute)
        self.generator = GenerateDataCsv(**kwargs_generate)
        self.prefix_final_filename = prefix_final_filename
        self.run()

    def run(self):
        for item in self.dilution:
            for key in item:
                print("Gerando dados: {}".format(key))
                self.generator.generate_data(
                    file_name=f'{self.prefix_final_filename}_{key}',
                    data=item[key]
                )
