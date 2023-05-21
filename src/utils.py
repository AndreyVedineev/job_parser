import json
import os

import requests

from src.head_hunter import createsvacancyAPI

references = os.path.join('..', 'src', 'references')  # директория справочники


def all_file_json(path):
    """ Формирование одного файла с вакансиями"""

    # уборка - удаление содержимого файла перед формированием
    open(path, 'w').close()

    # вспомогательный словарь
    # one_list = [x for x in range(len(os.listdir('../src/data')))]
    file_list = []
    for i in range(len(os.listdir('../src/data')) - 1):
        with open('../src/data/{}.json'.format(i + 1), mode='r', encoding='utf8') as file:
            data = json.load(file)
            file_list.append(data)
    # сшивание словаря ключ: номер файла, значение: содержимое запроса
    # all_dict = dict(zip(one_list, file_list))
    with open(path, 'w', encoding='utf8') as file:
        json.dump(file_list, file, ensure_ascii=False)
    # уборка - удаление всех файлов из директории data/
    filelist = [f for f in os.listdir('../src/data/') if f.endswith(".json")]
    for f in filelist:
        os.remove(os.path.join('../src/data/', f))


def get_area(url):
    """'https://api.hh.ru/areas'  - Hunt Hanter
        https://api.superjob.ru/2.0/regions/combined/  - superJob
    """
    response = requests.get(url)
    area = response.json()

    with open(f"{references}/area_sj.json", "w", encoding='UTF-8') as file:
        json.dump(area, file, ensure_ascii=False)


def normalization_hh_1():
    """Приводить файл к к одному формату список словарей """
    temp_list = []
    with open(f"{references}/vacancy_hh.json", 'r', encoding='utf8') as file:
        data = json.load(file)
        for i in data:
            for j in i:
                temp_list.append(j)

    with open(f"{references}/vacancy_hh.json", 'w', encoding='utf8') as file:
        json.dump(temp_list, file, ensure_ascii=False)


def creating_vacancies_hh():
    """Создание экземпляров вакансий HH"""

    list_vacancies_hh = []  # список вакансий с hh
    counter = 0  # счетчик вакансий

    with open(f"{references}/vacancy_hh.json", 'r', encoding='utf8') as file:
        data = json.load(file)
        for i in data:
            name = i['name']
            salary_from = i['salary']['from']
            salary_to = i['salary']['to']
            currency = i['salary']['currency']
            vacancies_type = i['type']['name']
            requirement = i['snippet']['requirement']  # требование
            employment = i['employment']['name']
            url = i['alternate_url']

            vac_hh = createsvacancyAPI(name, salary_from, salary_to, currency, vacancies_type, requirement,
                                       employment, url)
            list_vacancies_hh.append(vac_hh)
            counter += 1
    print(f'_Сформирован список из {counter} вакансий с сайта HeadHunter_')
    return list_vacancies_hh


def creating_vacancies_sj():
    """Создание экземпляров вакансий SJ"""
    list_vacancies_sj = []  # список вакансий с hh
    counter = 0  # счетчик вакансий

    with open(f"{references}/vacancy_sj.json", 'r', encoding='utf8') as file:
        data = json.load(file)
        for i in data:
            name = i['profession']
            salary_from = i['payment_from']
            salary_to = i['payment_to']
            currency = i['currency'].upper()
            vacancies_type = i['is_archive']
            requirement = i['vacancyRichText']  # требование
            employment = i['type_of_work']['title']
            url = i['link']

            vac_hh = f'vacancy{counter}'  # формирование имени экземпляра класса hh
            vac_hh = createsvacancyAPI(name, salary_from, salary_to, currency, vacancies_type, requirement,
                                       employment, url)

            list_vacancies_sj.append(vac_hh)
            counter += 1
    print(f'_Сформирован список из {counter} вакансий с сайта SuperJob_')
    return list_vacancies_sj

# def normalization_hh_2():
#     """Проверяет поле зарплаты, если нет то ... и приводит к .... """
#
#     with open(f"{references}/vacancy_hh.json", 'r', encoding='utf8') as file:
#         data = json.load(file)
#         for i in data:
#             print(i['employment'])


# def normalization_sj_1():
#     """Проверяет поле
#     payment_from зарплаты, если 0 то меняет на None
#     payment_to зарплаты, если 0 то меняет на None
#     и приводит к .... """
#
#     temp_list = []
#     with open(f"{references}/vacancy_sj.json", 'r', encoding='utf8') as file:
#         data = json.load(file)
#         for i in data:
#
#             print(i['payment_from'])


