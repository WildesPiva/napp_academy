
import csv, datetime

class Buscador:
    """ Buscador no csv em OO. """
    def __init__(self, path):
        """
        Construtor de objetos Buscador para consulta de dados no csv.

        Args:
            path (String): Nome do arquivo
        """
        self.path = path
        self.lista = self.carregar_arquivo()

    def find_substring_credit_card(self, parametro='322'):
        """
        Função que recebe a lista com todos os registros carregados de um
        arquivo CSV via DictReader e busca a string 'parâmetro' como substring
        do campo 'Cartão de Crédito'.

        Args:
            lista (List): [description]
            parametro (str, optional): Substring a ser encontrada. Padrão '322'.

        Returns:
            List: Lista com os nomes de pessoas que possuam substring
            no cartão de crédito
        """
        results = list()
        for item in self.lista:
            if parametro in item.get('credit_card',''):
                results.append(item.get('name'))
        return results

    def find_start_substring_credit_card(self, parametro='303'):
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
        for item in self.lista:
            if parametro == item.get('credit_card','')[:len(parametro)]:
                results.append(item.get('name'))
        return results

    def carregar_arquivo(self):
        """
        Função que recebe a string com o arquivo, abre o arquivo CSV
        com o DictReader e carrega os dados em uma lista retornada.

        Args:
            path (String): Nome do arquivo

        Returns:
            (List): Lista com todos os registros
        """
        local_list = list()
        with open(self.path, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            for line in reader:
                local_list.append(line)
        return local_list

    def extract_datetime(self, date, format="%Y-%m-%d"):
        """ 
        Função que recebe  uma data e extrai o ano

        Args:
            date (str): string data;
            format (str): formato que o parametro data está. Defaults to '%Y-%m-%d' - ex date: 2020-02-21;

        Returns:
            datetime: Obj datetime;
        """
        try:
            return datetime.datetime.strptime(date, format)
        except ValueError as error:
            # print(error)
            return None

    def find_born_in(self, birth_year='1996'):
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
        for item in self.lista:
            if self.extract_datetime(item.get('birthdate')).year == int(birth_year):
                results.append(item.get('name'))
        return results

    def find_born_in_month(self, paramether='03'):
        """
        Função que recebe a lista com todos os registros carregados de um
        arquivo CSV via Reader e busca os clientes nascidos no mês 'paramether'.

        Args:
            lista (List): Lista de tuplas
            paramether (str, optional): Mês de nascimento com dois caracteres
            janeiro = '01', Fevereiro = '02' . Padrão '03'.

        Returns:
            List: Lista com os nomes de pessoas que nasceram no mês informado.
        """
        results = list()
        for item in self.lista:
            if self.extract_datetime(item.get('birthdate')).month == int(paramether):
                results.append(item.get('name'))
        return results

    def find_born_in_month_and_gender(self, paramether='03', gender='F'):
        """
        Função que recebe a lista com todos os registros carregados de um
        arquivo CSV via Reader e busca os clientes nascidos no mês 'paramether'
        E pelo gênero gender.

        Args:
            lista (List): Lista de tuplas
            paramether (str, optional): Mês de nascimento com dois caracteres
            janeiro = '01', Fevereiro = '02' . Padrão '03'.
            gender (str, optional): Gênero ( M ou F) com um caracter. Padrão 'F'.

        Returns:
            List: Lista com os nomes de pessoas que nasceram no mês informado
            e com gênero informado.
        """
        results = list()
        for item in self.lista:
            if self.extract_datetime(item.get('birthdate')).month == int(paramether) and item.get('gender') == gender:
                results.append(item.get('name'))
        return results

    def find_start_substring_credit_card_more_opt(self, *paramethers):
        """
        Função que recebe a lista com todos os registros carregados de um
        arquivo CSV via Reader e busca os clientes com o número de cartão
        de crédito passado como parâmetro. Pode-se passar diversos parâmetros.
        Retorna uma lista vazia, caso nenhum parâmetro seja passado.

        Args:
            lista (List): Lista de tuplas

        Returns:
            List: Lista com os nomes de pessoas com cartão de crédito com 
        """
        results = list()
        for item in self.lista:
            for parameter in paramethers:
                if parameter == item.get('credit_card')[:len(parameter)]:
                    results.append(item.get('name'))
        return results

if __name__ == "__main__":
    buscador_obj = Buscador('usernames.csv')

    print(buscador_obj.find_substring_credit_card())
    print(buscador_obj.find_substring_credit_card('222'))

    print(buscador_obj.find_start_substring_credit_card())
    print(buscador_obj.find_start_substring_credit_card('222'))

    # print(buscador_obj.find_born_in())
    # print(buscador_obj.find_born_in('1982'))

    # print(buscador_obj.find_born_in_month())
    # print(buscador_obj.find_born_in_month('01'))

    # print(buscador_obj.find_born_in_month_and_gender())
    # print(buscador_obj.find_born_in_month_and_gender('01', 'M'))

    # print(buscador_obj.find_start_substring_credit_card_more_opt())
    # print(buscador_obj.find_start_substring_credit_card_more_opt('222', '223', '224'))