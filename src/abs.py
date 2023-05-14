from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def a1(self):
        pass


class SaveVac(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass



