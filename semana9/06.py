lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio']
lista_meses += ['junho', 'julho', 'agosto', 'setembro']
lista_meses += ['outubro', 'novembro', 'dezembro']

meses = dict(zip(
    list(range(1, 13)),
    lista_meses))


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
    data = data.split('/')
    try:
        return data[0] + ' de ' + meses[int(data[1])] + ' de ' + data[2]
    except KeyError:
        raise KeyError('Mês inválido')
