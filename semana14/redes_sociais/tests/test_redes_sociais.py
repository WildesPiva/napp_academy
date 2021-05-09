import pytest
from unittest import TestCase

from redes_sociais.classes.redes_sociais import (
    Profile,
    facebook,
    linkedin,
    github,
    instagram
)


class TestRedesSociais(TestCase):
    def setUp(self):
        self.redes_sociais = [
            'facebook',
            'linkedin',
            'github',
            'instagram'
        ]

    def test_redes_sub_class(self):
        for rede_social_str in self.redes_sociais:
            rede_social_class = eval(rede_social_str.lower())
            assert issubclass(rede_social_class, Profile)

    def test_redes_instance(self):
        for rede_social_str in self.redes_sociais:
            rede_social_class = eval(rede_social_str.lower())
            rede_social_instance = rede_social_class()
            assert isinstance(rede_social_instance, rede_social_class)

    def test_redes_sections_type(self):
        for rede_social_str in self.redes_sociais:
            rede_social_instance = eval(rede_social_str.lower())()
            assert type(rede_social_instance.getSections()) == list

    def test_facebook_get_sections(self):
        rede_social = facebook()
        sections = rede_social.getSections()
        assert len(sections) == 2

    def test_linkedin_get_sections(self):
        rede_social = linkedin()
        sections = rede_social.getSections()
        assert len(sections) == 2

    def test_github_get_sections(self):
        rede_social = github()
        sections = rede_social.getSections()
        assert len(sections) == 2

    def test_instagram_get_sections(self):
        rede_social = instagram()
        sections = rede_social.getSections()
        assert len(sections) == 2
