
import csv

def find_substring_credit_card(lista, parametro='322'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca a string 'parâmetro' como substring
    do campo 'Cartão de Crédito'.

    Args:
        lista (List): [description]
        parametro (str, optional): Substring a ser encontrada. Padrão '322'.

    Returns:
        List: Lista com os nomes de pessoas que possuam substring
        no cartão de crédito
    """
    results = list()
    for item in lista:
        if parametro in item.get('credit_card',''):
            results.append(item.get('name'))
    return results

def find_start_subtring_credit_card(lista, parametro='303'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca a string 'parâmetro' como início
    do campo 'Cartão de Crédito'.

    Args:
        lista (List): [description]
        parametro (str, optional): Substring a ser encontrada. Padrão '303'.

    Returns:
        List: Lista com os nomes de pessoas que possuam substring
        no cartão de crédito
    """
    results = list()
    for item in lista:
        if parametro == item.get('credit_card','')[:len(parametro)]:
            results.append(item.get('name'))
    return results

def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o DictReader e carrega os dados em uma lista retornada.

    Args:
        path (String): Nome do arquivo

    Returns:
        (List): Lista com todos os registros
    """
    local_list = list()
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = carregar_arquivo(path)

    print(find_substring_credit_card(lista))
    print(find_substring_credit_card(lista, '222'))

    print(find_start_subtring_credit_card(lista))
    print(find_start_subtring_credit_card(lista, '222'))
