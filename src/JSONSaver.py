import json
import os

from src.abs import Saver

path = os.path.join('..', 'src', 'references', 'vacancy.json')  # путь к файлу c вакансиями


class JSONSaver(Saver):
    """Запись вакансий в файлы по параметрам"""

    def __init__(self, ls_vacancy):
        self.ls_vacancy = ls_vacancy

    def add_vacancy(self):
        """ Все найденные вакансии формат json"""
        temp_list = []
        temp_dict = {}

        for i in self.ls_vacancy:
            temp_dict['name'] = i.name
            temp_dict['salary_from'] = i.salary_from
            temp_dict['salary_to'] = i.salary_to
            temp_dict['currency'] = i.currency
            temp_dict['vacancies_type'] = i.vacancies_type
            temp_dict['requirement'] = i.requirement
            temp_dict['employment'] = i.employment
            temp_dict['url'] = i.url
            temp_list.append(temp_dict)

        with open(path, "w", encoding='UTF-8') as file:
            json.dump(temp_list, file, ensure_ascii=False)

    def get_vacancies_by_salary(self, param: str):
        """Запись по диапазону зарплаты"""

        pass

    def delete_vacancy(self):
        """Удаляет ваканисию"""
        pass

    def __str__(self):
        for i in self.ls_vacancy:
            print(f'Вакансия: {i.name}\n'
                  f'Зарплата: {i.salary_from} до {i.salary_to} {i.currency}.')

    # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)
