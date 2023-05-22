from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __add__(self, other):
        pass


class SaveVac(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


