from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def sorted_vacancies(self):
        pass

    @abstractmethod
    def top_vacancies(self):
        pass


class SaveVac(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

