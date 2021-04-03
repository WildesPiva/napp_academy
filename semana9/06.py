from datetime import datetime
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', \
               'junho', 'julho', 'agosto', 'setembro', 'outubro', \
               'novembro', 'dezembro']

meses = dict( zip(list(range(1, 13)), lista_meses) )


def data_por_extenso(data):
    """
    Recebe uma data no formado dd/MM/aaaa e retorna por extenso.
    Entrada '10/12/2020'
    Saída '10 de dezembro de 2020'

    Args:
        data ([str]): Data no formado dd/MM/aaaa

    Returns:
        [str]: Data por extenso
    """
    if not isinstance(data, str):
        raise Exception('A data precisa ser uma string')

    try:
        data = datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        raise ValueError(f"A data '{data}' não bate com o formato 'dd/MM/aaaa'")

    return f'{data.day} de {meses[int(data.month)]} de {data.year}'

print(data_por_extenso('1/5/2020'))