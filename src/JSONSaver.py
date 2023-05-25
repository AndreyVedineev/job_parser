import json
import os

from src.abs import Saver

path = os.path.join('..', 'src', 'references', 'vacancy.json')  # путь к файлу c вакансиями
path_by_salary = os.path.join('..', 'src', 'references', 'vacancyft.json')  # путь к файлу c вакансиями from  -> to


def unpacking(ls):
    """Рапакова экземпляра в словарь"""
    temp_list = []
    for i in ls:
        temp_dict = {'name': i.name, 'salary_from': i.salary_from, 'salary_to': i.salary_to, 'currency': i.currency,
                     'vacancies_type': i.vacancies_type, 'requirement': i.requirement, 'employment': i.employment,
                     'url': i.url}
        temp_list.append(temp_dict)

    return temp_list


class JSONSaver(Saver):
    """Запись вакансий в файлы по параметрам"""

    def __init__(self, ls_vacancy):
        self.ls_vacancy = ls_vacancy

    def add_vacancy(self):
        """ Все найденные вакансии формат json"""

        with open(path, "w", encoding='UTF-8') as file:
            json.dump(unpacking(self.ls_vacancy), file, ensure_ascii=False)

    def get_vacancies_by_salary(self, param: str):
        """Запись по диапазону зарплаты"""
        temp_l = []
        temp_ls = param.split('-')
        n_salary_from = int(temp_ls[0])
        n_salary_to = int(temp_ls[-1])
        for i in self.ls_vacancy:
            if n_salary_from <= i.salary_from <= n_salary_to:
                temp_l.append(i)
        with open(path_by_salary, "w", encoding='UTF-8') as file:
            json.dump(unpacking(temp_l), file, ensure_ascii=False)

    def delete_vacancy(self):
        """Удаляет ваканисию"""
        pass

    def __str__(self):
        for i in self.ls_vacancy:
            print(f'Вакансия: {i.name}\n'
                  f'Зарплата: {i.salary_from} до {i.salary_to} {i.currency}.')

    # json_saver.delete_vacancy(vacancy)
