from dilute_data import DiluteData
from generate_data import GenerateData

dilution = DiluteData(
    # csv_path='../data/teste.csv',
    csv_path='../data/.temp/candidatura.csv',
    column_to_consider=0,
    header=1
)
# dilution.lines_with_header
for item in dilution:
    print("*"*100)
    for key in item:
        print("Gerando dados: {}".format(key))
        generator = GenerateData(path_file='./.temp')
        generator.generate_csv(
            file_name=f'eleicao_{key}',
            data=item[key]
        )

        # print("Data: {}".format(list(data)))
