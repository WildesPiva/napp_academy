import pytest
from unittest import TestCase

# from redes_sociais.redes_sociais import facebook


class TestRedesSociais(TestCase):
    def setUp(self):
        self.profile_types = [
            'facebook', 'linkedin'
        ]
