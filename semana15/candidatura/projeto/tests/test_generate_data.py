import os
from pathlib import Path
import pytest
from unittest import TestCase
from projeto.separate.generate_data import GenerateDataCsv


class TestGenerateDataCsv(TestCase):
    def setUp(self):
        path = './.temp'
        if not Path(path).exists():
            os.mkdir(path)
        self.params = {
            'path_file': path
        }

    def test_instanciar_objeto_ok(self):
        objeto = GenerateDataCsv(**self.params)
        assert isinstance(objeto, GenerateDataCsv)

    def test_instanciar_objeto_invalid(self):
        error_msg = 'Invalid file path'
        with pytest.raises(Exception) as error:
            GenerateDataCsv(path_file='./file.csv')
        assert str(error.value) == error_msg

    def test_metodo_generate_data(self):
        objeto = GenerateDataCsv(**self.params)
        assert objeto.generate_data(
            'file_name',
            ['row1,teste\n', 'row2,teste2'],
            header='row,name\n'
        )
