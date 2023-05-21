import os
from abc import ABC

from src.abs import Parser

path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу
references = os.path.join('..', 'src', 'references')


class HeadHunterAPI(Parser):

    def __init__(self, vacancies_id, name, salary_from, salary_to, currency, vacancies_type, requirement,
                 responsibility, employment):
        self.vacancies_id = vacancies_id
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.vacancies_type = vacancies_type
        self.requirement = requirement  # требование
        self.responsibility = responsibility  # ответственность
        self.employment = employment  # трудоустройство

    def sorted_vacancies(self):
        pass

    def top_vacancies(self):
        pass
