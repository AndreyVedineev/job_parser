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


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self):
        """ Все найденные вакансии"""
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, param: str):
        """запись по диапазону зарплаты"""

        pass

    @abstractmethod
    def delete_close_vacancy(self):
        """Удаляет ваканисию"""
        pass


class ParsingErorr(Exception):
    def __init__(self, mess):
        self.mess = mess
        
    def __str__(self):
        return self.mess
        
