from dilute_data import DiluteData
from generate_data import GenerateData

dilution = DiluteData(
    csv_path='../data/teste.csv',
    column_to_consider=0,
    header=1
)

for item in dilution:
    for key in item:
        print("Gerando dados: {}".format(key))
        generator = GenerateData(path_file='./.temp')
        generator.generate_csv(
            file_name=f'eleicao_{key}',
            data=item[key]
        )
