import json
import os

from dotenv import load_dotenv

from src.abs import Parser

load_dotenv()
api_key = os.getenv('SJ_SECRET_KEY')
path_sj = os.path.join('..', 'src', 'references', 'vacancy_sj.json')  # путь к файлу
references = os.path.join('..', 'src', 'references')


class SuperJobAPI(Parser):
    """ название вакансии,
        ссылка на вакансию,
        зарплата,
        краткое описание или требования"""

    def __init__(self):
        self.name = None
        self.url = "http:/ya.ru"
        self.salary = 100000
        self.brief_description = 'SuperJob'

    def sorted_vacancies(self):
        """Сортирует вакансии по зарплате"""
        with open(path_sj, "r", encoding='UTF-8') as file:
            l = json.load(file)
            sorted(l, key=lambda x: x['payment_from'])

