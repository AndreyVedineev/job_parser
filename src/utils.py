import json
import os
import time

import requests

from src.creates_vacancy import CreatesVacancyAPI

references = os.path.join('..', 'src', 'references')  # директория справочники
path_sj = os.path.join('..', 'src', 'references', 'vacancy_sj.json')  # путь к файлу
path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу


def all_file_json(path):
    """ Формирование одного файла с вакансиями"""

    # уборка - удаление содержимого файла перед формированием
    open(path, 'w').close()
    file_list = []
    for i in range(len(os.listdir('../src/data')) - 1):
        with open('../src/data/{}.json'.format(i + 1), mode='r', encoding='utf8') as file:
            data = json.load(file)
            file_list.append(data)

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
    """Приводить файл к к одному формату -> список словарей """
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
            if i['salary']['from'] is None:
                salary_from = 0
            else:
                salary_from = i['salary']['from']
            if i['salary']['to'] is None:
                salary_to = "_XXX_"
            else:
                salary_to = i['salary']['to']
            currency = i['salary']['currency']
            vacancies_type = i['type']['name']
            if i['snippet']['requirement'] is None:
                requirement = "Не требуется"
            else:
                requirement = i['snippet']['requirement']  # требование
            employment = i['employment']['name']
            url = i['alternate_url']

            vac_hh = CreatesVacancyAPI(name, salary_from, salary_to, currency, vacancies_type, requirement,
                                       employment, url)
            list_vacancies_hh.append(vac_hh)
            counter += 1
    print(f'_Сформирован список из {counter} вакансий с сайта HeadHunter_')
    time.sleep(0.3)
    return list_vacancies_hh


def creating_vacancies_sj():
    """Создание экземпляров вакансий SJ"""
    list_vacancies_sj = []  # список вакансий с hh
    counter = 0  # счетчик вакансий

    with open(f"{references}/vacancy_sj.json", 'r', encoding='utf8') as file:
        data = json.load(file)
        for i in data:
            name = i['profession']
            if i['payment_from'] is None:
                salary_from = 0
            else:
                salary_from = i['payment_from']
            if i['payment_to'] == 0:
                salary_to = "_XXX_"
            else:
                salary_to = i['payment_to']
            currency = i['currency'].upper()
            vacancies_type = i['is_archive']
            requirement = i['vacancyRichText']  # требование
            employment = i['type_of_work']['title']
            url = i['link']

            vac_sj = CreatesVacancyAPI(name, salary_from, salary_to, currency, vacancies_type, requirement,
                                       employment, url)

            list_vacancies_sj.append(vac_sj)
            counter += 1
    print(f'_Сформирован список из {counter} вакансий с сайта SuperJob_')
    time.sleep(0.3)
    return list_vacancies_sj


def salary_validator_sj():
    """Валидатор  по отсутствии зарплаты перезаписывает файл """
    with open(path_sj, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        temp_list = [j for i in templates for j in i if j['payment_from'] != 0]
    with open(path_sj, "w", encoding='UTF-8') as file:
        json.dump(temp_list, file, ensure_ascii=False)


def salary_validator_hh():
    """Валидатор  по отсутствии зарплаты
        перезаписывает файл """

    with open(path_hh, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        temp_list = [i for i in templates if i['salary'] is not None]
    with open(path_hh, "w", encoding='UTF-8') as file:
        json.dump(temp_list, file, ensure_ascii=False)


def normalization_of_requirement_hh(list_no_norm):
    """Удаляет не нужные нам символы"""
    for i in list_no_norm:
        a = str(i.requirement)
        b = a.replace('<highlighttext>', '')
        c = b.replace('</highlighttext>', '')
        i.requirement = c


def normalization_of_requirement_sj(list_no_norm: object) -> object:
    """Удаляет не нужные нам символы Наверно есть другой способ 😀"""
    for i in list_no_norm:
        a = str(i.requirement)
        b = a.replace('<b>', ' ')
        c = b.replace('</b>', ' ')
        d = c.replace('<ul>', ' ')
        e = d.replace('</ul>', ' ')
        f = e.replace('<li>', ' ')
        g = f.replace('</li>', ' ')
        h = g.replace('<p>', ' ')
        k = h.replace('</p>', ' ')
        l = k.replace('<br>', ' ')
        m = l.replace('<br />', '')
        n = m.replace('\n', '')
        i.requirement = n
    return list_no_norm


def average_salary(list_):
    """Вычисляет среднюю по salary from не считает если значение от: 0"""
    sums = list_[0].salary_from
    for i in list_[1:]:
        sums = i.salary_from + sums
    return sums / len(list_)


def create_dir_data():
    """создать пустой каталог (папку)"""
    if not os.path.isdir("data"):
        os.mkdir("data")


def del_folder():
    """ Удаляет не нужный каталог """
    os.rmdir("data")



# def mim_salary(list_):
#     min_salary = list_[0].salary_from
#
#     for i in list_[1:]:
#         if min_salary < i.salary_from:
#             min_salary = i.salary_from
#     return min_salary
