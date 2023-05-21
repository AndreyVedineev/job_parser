import json
import os


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
            if i['payment_to'] == 0:
                salary_to = "_X_"
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
    return list_vacancies_sj


def salary_validator_sj():
    """Валидатор  по отсутствии зарплаты
        перезаписывает файл """
    temp_list = []
    with open(path_sj, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        for i in templates:
            for j in i:
                if j['payment_from'] != 0:
                    temp_list.append(j)
                    # print(f"{j['profession']} -{j['payment_from']} - {j['payment_to']}")
    with open(path_sj, "w", encoding='UTF-8') as file:
        json.dump(temp_list, file, ensure_ascii=False)


def salary_validator_hh():
    """Валидатор  по отсутствии зарплаты
        перезаписывает файл """
    temp_list = []
    with open(path_hh, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        for i in templates:
            if i['salary'] is not None:
                temp_list.append(i)
                # print(f" {i['name']} -  от {i['salary']['from']} до {i['salary']['to']} ")
    # print(count)
    with open(path_hh, "w", encoding='UTF-8') as file:
        json.dump(temp_list, file, ensure_ascii=False)


def normalization_of_requirement_hh(list_no_norm):
    """Удаляет не нужные нам символы"""
    for i in list_no_norm:
        a = str(i.requirement)
        b = a.replace('<highlighttext>', '')
        c = b.replace('</highlighttext>', '')
        i.requirement = c


def normalization_of_requirement_sj(list_no_norm):
    """Удаляет не нужные нам символы
    Наверно есть другой способ😀"""
    for i in list_no_norm:
        a = str(i.requirement)
        b = a.replace('<b>', '')
        c = b.replace('</b>', '')
        d = c.replace('<ul>', '')
        e = d.replace('</ul>', '')
        f = e.replace('<li>', '')
        g = f.replace('</li>', '')
        h = g.replace('<p>', '')
        k = h.replace('</p>', '')
        l = k.replace('<br>', '')
        m = l.replace('<br />', '')

        i.requirement = m
