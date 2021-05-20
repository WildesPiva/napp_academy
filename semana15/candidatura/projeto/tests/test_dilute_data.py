import pytest
from io import TextIOWrapper
from unittest import TestCase
from projeto.separate.dilute_data import AbstractDiluteData, DiluteDataCsv


class TestDiluteDataCsv(TestCase):
    def setUp(self):
        self.params = {
            # consider test in semana15
            'csv_path': './candidatura/projeto/data/teste.csv',
            'header': 1
        }

    def test_abstract_sub_class(self):
        assert issubclass(DiluteDataCsv, AbstractDiluteData)

    def test_instanciar_objeto_ok(self):
        objeto = DiluteDataCsv(**self.params)
        assert isinstance(objeto, DiluteDataCsv)

    def test_metodo_extract(self):
        objeto = DiluteDataCsv(**self.params)
        assert type(objeto.csv_it) == TextIOWrapper

    def test_metodo__get_columns(self):
        objeto = DiluteDataCsv(**self.params)
        assert len(set(objeto._get_columns())) == 6

    def test_metodo_get_data(self):
        objeto = DiluteDataCsv(**self.params)
        assert len(list(objeto._get_data('2021'))) == 1

    def test_metodo__iter__(self):
        objeto = DiluteDataCsv(**self.params)
        it = iter(objeto)
        assert next(it)
