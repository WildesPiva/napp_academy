from projeto.separate.separate_data import SeparateCsvData

if __name__ == '__main__':
    SeparateCsvData(
        kwargs_dilute=dict(
            csv_path='./projeto/data/teste.csv',  # csv with data
            # csv_path='./projeto/data/.temp/candidatura.csv',  # csv with data
            column_to_consider=0,  # column index number to separate
            header=1  # number rows from header
        ),
        kwargs_generate=dict(
            path_file='./'  # path to final file
        ),
        prefix_final_filename='eleicao'  # prefix to final file
    )
