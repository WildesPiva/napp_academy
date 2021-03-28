from rh.classes.Colaborador import Colaborador


class Departamento:
    def __init__(self, nome_setor, nome_responsavel, dia_responsavel, mes_responsavel, ano_responsavel):
        self.nome = nome_setor
        self._colaboradores = []
        self.informar_responsavel(nome_responsavel, dia_responsavel, mes_responsavel, ano_responsavel)

    @property
    def responsavel(self):
        return self._responsavel

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, dia, mes, ano):
        self._responsavel = Colaborador(nome, dia, mes, ano)
        self.add_colaborador(nome, dia, mes, ano)     

    def add_colaborador(self, nome, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((self.nome, colaborador.nome, colaborador.aniversario))
        return lista

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Departamento = ' + self.nome
