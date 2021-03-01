import pytest
from exercicio06 import calculo_porcentagem_entre_0_e_1


class TestEx06:
    valores = [
        (10, 1, 10),
        (10, 0.5, 5),
        (100, 0.7, 70),
        (1564.54, 0.4, 625.81),
    ]

    @pytest.mark.parametrize("valor, porcentagem, resultado", valores)
    def test_values_cenario_1(self, valor, porcentagem, resultado):
        calculo = calculo_porcentagem_entre_0_e_1(valor, porcentagem)
        assert calculo == pytest.approx(resultado, 0.1)

    def test_wrong_cenario_1(self):
        """ Porcentagem maior que o permitido """
        with pytest.raises(ValueError) as error:
            porcentagem = calculo_porcentagem_entre_0_e_1(valor=100, porcentagem=10)
        assert str(error.value) == 'Porcentagem precisa estar entre 0 e 1'
    
    def test_wrong_cenario_2(self):
        """ Porcentagem abaixo do permitido """
        with pytest.raises(ValueError) as error:
            porcentagem = calculo_porcentagem_entre_0_e_1(valor=100, porcentagem=-1)
        assert str(error.value) == 'Porcentagem precisa estar entre 0 e 1'        
