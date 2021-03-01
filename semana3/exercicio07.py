import csv, json

def carregar_dicionario_websites(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o dict_reader e carrega os dados em uma lista retornada.

    Args:
        path (String): Nome do arquivo

    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            local_list.append(line)
    return local_list

def websites_por_username(lista):
    results = {}
    for item in lista:
        if item.get('username'):
            results[item.get('username')] = item.get('website','[]').strip('[]').replace("'","").split(", ")
    return results

if __name__ == "__main__":
    lista = carregar_dicionario_websites('names.csv')
    dict_websites = websites_por_username(lista)
    print(json.dumps(dict_websites, indent=2))

