import csv, datetime

def extract_year(date, format="%Y-%m-%d"):
    """ 
    Função que recebe  uma data e extrai o ano

    Args:
        date (str): string data;
        format (str): formato que o parametro data está. Defaults to '%Y-%m-%d' - ex date: 2020-02-21;

    Returns:
        str: Ano da data informada;
    """
    try:
        return str(datetime.datetime.strptime(date, format).year)
    except ValueError as error:
        # print(error)
        return ''

def find_born_in(lista, birth_year='1996'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca os clientes nascidos em 'birth_year'.

    Args:
        lista (List): Lista de tuplas
        birth_year (str, optional): Ano de nascimento . Defaults to '1996'.

    Returns:
        List: Lista com os nomes de pessoas que nasceram no ano informado.
    """
    results = list()
    for item in lista:
        if extract_year(item[4]) == birth_year:
            results.append(item[0])
    return results


def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.

    Args:
        path (String): Nome do arquivo

    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_born_in(lista))
    print(find_born_in(lista, '1982'))
