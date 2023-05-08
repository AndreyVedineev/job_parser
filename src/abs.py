from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def json_saver(self):
        pass



