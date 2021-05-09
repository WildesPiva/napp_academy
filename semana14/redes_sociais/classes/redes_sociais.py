from abc import ABC, abstractmethod
from redes_sociais.classes.sessoes import (
    PublicationSection,
    PersonalSection,
    AlbumSection,
    UploadCode
)


class Profile(ABC):
    def __init__(self):
        self._sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self._sections

    def addSections(self, section):
        self._sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


class github(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(UploadCode())


class instagram(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
