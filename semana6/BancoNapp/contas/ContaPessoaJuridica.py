from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Classe representa a conta de pessoa juridica.
    Args:
        Conta ([type]): [description]
    """
    def __init__(self, **kwargs):
        """
        Construtor da classe ContaPessoaJuridica.
        Extrai do dicionário kwargs a profissao do correntista.
        """
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        print(self.__dict__)