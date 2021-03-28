from datetime import date


class Colaborador:
    def __init__(self, nome, dia=None, mes=None, ano=None):
        self.nome = nome
        try:
            self._aniversario = date(ano, mes, dia)
        except TypeError:
            raise TypeError('Informe dia, mês, ano ou verifique se são validos')

    @property
    def aniversario(self):
        return self._aniversario.isoformat()

    def aniversario_hoje(self):
        hoje = date.today()
        if self._aniversario.day == hoje.day:
            if self._aniversario.month == hoje.month:
                return True
        return False

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Colaborador: ' + self.nome
