from produtos.classes.Produtos import (
    GuaranaAntartica,
    Pepsi,
    Dolly,
)
from produtos.classes.Caracteristicas import (
    Caracteristicas,
    Tamanho600ml,
    Tamanho1litro,
    Tamanho2litros,
    Tamanho3litros,
)

import pytest


class TestCaracteristicas:
    def test_Pepsi_600ml(self):
        msg = 'Pepsi tamanho: 600ml.'
        caracteristica = Tamanho600ml()
        objeto = Pepsi(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho600ml)
        assert objeto.operation() == msg

    def test_Pepsi_1_litro(self):
        msg = 'Pepsi tamanho: 1 litro.'
        caracteristica = Tamanho1litro()
        objeto = Pepsi(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho1litro)
        assert objeto.operation() == msg

    def test_Dolly_1_litro(self):
        msg = 'Dolly tamanho: 2 litros.'
        caracteristica = Tamanho2litros()
        objeto = Dolly(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho2litros)
        assert objeto.operation() == msg

    def test_GuaranaAntartica_1_litro(self):
        msg = 'Guarana Antartica tamanho: 3 litros.'
        caracteristica = Tamanho3litros()
        objeto = GuaranaAntartica(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho3litros)
        assert objeto.operation() == msg

    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Caracteristicas "
        msg_erro = msg_erro + "with abstract methods operation_implementation"
        with pytest.raises(TypeError) as error:
            Caracteristicas()
        assert str(error.value) == msg_erro

    def test_class_abstractClass_error(self):
        msg_erro = 'Class need to be instantiated with a Caracteristicas type'
        with pytest.raises(TypeError) as error:
            _ = Pepsi('teste')
        assert str(error.value) == msg_erro
