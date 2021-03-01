import pytest
from exercicio08 import juros_compostos

class TestEx08:
    valores = [
        (10, 100, 1, 20),
        (55, 20, 1, 66),
        (30, 14, 3, 44),
    ]

    @pytest.mark.parametrize("valor_inicial, juros, tempo, resultado", valores)
    def test_values_cenario_1(self, valor_inicial, juros, tempo, resultado):
        calculo = juros_compostos(valor_inicial, juros, tempo)
        assert calculo == pytest.approx(resultado, 0.1)

    def test_wrong_cenario_1(self):
        """ Verificando caso passe string """
        with pytest.raises(ValueError) as error:
            calculo = juros_compostos(valor_inicial=40, juros='A', tempo=5)
        assert str(error.value) == "could not convert string to float: 'A'"

    def test_wrong_cenario_2(self):
        """ Juros maior que o permitido """
        with pytest.raises(ValueError) as error:
            calculo = juros_compostos(valor_inicial=40, juros=101, tempo=5)
        assert str(error.value) == 'Juros precisa estar entre 0 e 100'
    
    def test_wrong_cenario_3(self):
        """ Juros abaixo do permitido """
        with pytest.raises(ValueError) as error:
            calculo = juros_compostos(valor_inicial=40, juros=-111, tempo=5)
        assert str(error.value) == 'Juros precisa estar entre 0 e 100'        