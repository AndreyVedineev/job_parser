import os

from src.abs import Parser

path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу
references = os.path.join('..', 'src', 'references')


class CreatesVacancyAPI(Parser):
    """Класс создания вакансий"""

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

    def __str__(self):
        return f"Вакансия: {self.name}\n" \
               f"Зарплата: от {self.salary_from} до {self.salary_to} {self.currency}\n" \
               f"Требование: {self.requirement}\n" \
               f"Режим работы: {self.employment}\n " \
               f"Ссылка: {self.url}\n" \
               f""

    def __add__(self, other):
        return self.salary_from + other

    # – для оператора меньше <
    def __lt__(self, other):
        return self.salary_from < other.salary_from

