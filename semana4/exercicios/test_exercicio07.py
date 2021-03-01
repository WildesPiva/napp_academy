import pytest
from exercicio07 import calculo_porcentagem_entre_0_e_100


class TestEx07:
    valores = [
        (10, 100, 10),
        (10, 50, 5),
        (100, 70, 70),
        (1564.54, 40, 625.81),
    ]

    @pytest.mark.parametrize("valor, porcentagem, resultado", valores)
    def test_values_cenario_1(self, valor, porcentagem, resultado):
        calculo = calculo_porcentagem_entre_0_e_100(valor, porcentagem)
        assert calculo == pytest.approx(resultado, 0.1)

    def test_wrong_cenario_1(self):
        """ Porcentagem maior que o permitido """
        with pytest.raises(ValueError) as error:
            porcentagem = calculo_porcentagem_entre_0_e_100(valor=100, porcentagem=110)
        assert str(error.value) == 'Porcentagem precisa estar entre 0 e 100'
    
    def test_wrong_cenario_2(self):
        """ Porcentagem abaixo do permitido """
        with pytest.raises(ValueError) as error:
            porcentagem = calculo_porcentagem_entre_0_e_100(valor=100, porcentagem=-1)
        assert str(error.value) == 'Porcentagem precisa estar entre 0 e 100'        
