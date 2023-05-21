import os

from src.abs import Parser

path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу
references = os.path.join('..', 'src', 'references')


class createsvacancyAPI(Parser):

    def __init__(self, name, salary_from, salary_to, currency, vacancies_type, requirement,
                 employment, url):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.vacancies_type = vacancies_type
        self.requirement = requirement  # требование
        self.employment = employment  # трудоустройство
        self.url = url

    def sorted_vacancies(self):
        pass

    def top_vacancies(self):
        pass
