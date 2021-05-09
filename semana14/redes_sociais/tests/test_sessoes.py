import pytest
from unittest import TestCase

from redes_sociais.sessoes import (
    PublicationSection,
    PersonalSection,
    AlbumSection,
    Section
)


class TestPersonalSection(TestCase):
    def setUp(self):
        self.section = PersonalSection()

    def test_section_subclass(self):
        assert issubclass(PersonalSection, Section)

    def test_section_instance(self):
        assert isinstance(self.section, PersonalSection)

    def test_section_str(self):
        assert str(self.section) == 'Dados Pessoais'

    def test_section_repr(self):
        assert repr(self.section) == 'Dados Pessoais'


class TestAlbumSection(TestCase):
    def setUp(self):
        self.section = AlbumSection()

    def test_section_subclass(self):
        assert issubclass(AlbumSection, Section)

    def test_section_instance(self):
        assert isinstance(self.section, AlbumSection)

    def test_section_str(self):
        assert str(self.section) == 'Sessão para fotos'

    def test_section_repr(self):
        assert repr(self.section) == 'Sessão para fotos'


class TestPublicationSection(TestCase):
    def setUp(self):
        self.section = PublicationSection()

    def test_section_subclass(self):
        assert issubclass(PublicationSection, Section)

    def test_section_instance(self):
        assert isinstance(self.section, PublicationSection)

    def test_section_str(self):
        assert str(self.section) == 'Sessão publicações'

    def test_section_repr(self):
        assert repr(self.section) == 'Sessão publicações'
