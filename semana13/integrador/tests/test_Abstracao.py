from integrador.classes.Abstracao import Abstracao
import pytest
import unittest


class TestAbstracaoERP1(unittest.TestCase):
    def setUp(self):
        self.dicionario = {'erp': 'erp1',
                           'db': 'integrador/dados/banco_ERP1.db',
                           'relatorio': 'txt'}

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto, Abstracao)
        objeto2 = Abstracao(erp='erp1', relatorio="txt")
        assert isinstance(objeto2, Abstracao)

    def test_erp_nao_implementado(self):
        msg_erro = 'ERP não implementado'
        with pytest.raises(Exception) as error:
            dicionario = {'erp': 'erp_nao_implementado'}
            Abstracao(**dicionario)
        assert str(error.value) == msg_erro

    def test_relatorio_nao_implementado(self):
        msg_erro = 'Formato de relatório não implementado'
        with pytest.raises(Exception) as error:
            dicionario = {'erp': 'erp1', 'relatorio': 'xls'}
            Abstracao(**dicionario)
        assert str(error.value) == msg_erro

    def test_metodo_extrair_dados(self):
        objeto = Abstracao(**self.dicionario)
        assert type(objeto.extrair_dados()) == list

    def test_metodo_relatorio_simples(self):
        objeto = Abstracao(**self.dicionario)
        assert type(objeto.relatorio_simples()) == list

    def test_metodo_criar_relatorio(self):
        objeto = Abstracao(**self.dicionario)
        assert objeto.criar_relatorio()

    def test_metodo_criar_relatorio_csv(self):
        dicionario = {'erp': 'erp1',
                      'db': 'integrador/dados/banco_ERP1.db',
                      'relatorio': 'csv'}
        objeto = Abstracao(**dicionario)
        assert objeto.criar_relatorio()

    def test_formato_dados_extraidos(self):
        objeto = Abstracao(**self.dicionario)
        dados = objeto.extrair_dados()
        for linha in dados:
            assert len(linha) == 2
            assert type(linha[0]) == float
            assert type(linha[1]) == str


class TestAbstracaoERP2(unittest.TestCase):
    def setUp(self):
        self.dicionario = {'erp': 'erp2',
                           'db': 'integrador/dados/banco_ERP2.db',
                           'relatorio': 'txt'}

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto, Abstracao)
        objeto2 = Abstracao(erp='erp1', relatorio="txt")
        assert isinstance(objeto2, Abstracao)

    def test_erp_nao_implementado(self):
        msg_erro = 'ERP não implementado'
        with pytest.raises(Exception) as error:
            dicionario = {'erp': 'erp_nao_implementado'}
            Abstracao(**dicionario)
        assert str(error.value) == msg_erro

    def test_relatorio_nao_implementado(self):
        msg_erro = 'Formato de relatório não implementado'
        with pytest.raises(Exception) as error:
            dicionario = {'erp': 'erp1', 'relatorio': 'xls'}
            Abstracao(**dicionario)
        assert str(error.value) == msg_erro

    def test_metodo_extrair_dados(self):
        objeto = Abstracao(**self.dicionario)
        assert type(objeto.extrair_dados()) == list

    def test_metodo_relatorio_simples(self):
        objeto = Abstracao(**self.dicionario)
        assert type(objeto.relatorio_simples()) == list

    def test_metodo_criar_relatorio(self):
        objeto = Abstracao(**self.dicionario)
        assert objeto.criar_relatorio()

    def test_metodo_criar_relatorio_csv(self):
        dicionario = {'erp': 'erp2',
                      'db': 'integrador/dados/banco_ERP2.db',
                      'relatorio': 'csv'}
        objeto = Abstracao(**dicionario)
        assert objeto.criar_relatorio()

    def test_formato_dados_extraidos(self):
        objeto = Abstracao(**self.dicionario)
        dados = objeto.extrair_dados()
        for linha in dados:
            assert len(linha) == 2
            assert type(linha[0]) == float
            assert type(linha[1]) == str
