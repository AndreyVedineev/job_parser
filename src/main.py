import os

from src.save_jsonHH import SaveJsonHH
from src.save_jsonSJ import SaveJsonSJ
from src.utils import creating_vacancies_sj, \
    normalization_of_requirement_sj, all_file_json, normalization_hh_1, salary_validator_hh, creating_vacancies_hh, \
    normalization_of_requirement_hh, salary_validator_sj

path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу с вакансиями HH
path_sj = os.path.join('..', 'src', 'references', 'vacancy_sj.json')  # путь к файлу с вакансиями SJ


def user_interaction():
    """ Эта программа для поиска вакансий,  на сайтах SuperJob и HeadHunter."""

    print('Эта программа для поиска вакансий, на сайтах SuperJob и HeadHunter.')

    print('Введите ключевое слово для поиска вакансии:')
    key_word = input().strip()
    # print('Введите код города')
    # key_town = int(input().strip())

    # Парсинг сайта HeadHunter
    hh = SaveJsonHH(key_word, 53)  # 53 - Краснодар. 2444 - Мостовской. 1438 - Краснодарский край 70 - Оренбург
    hh.get_vacancies()  # Запрос к API
    all_file_json(path_hh)  # Формирование одного файла с вакансиями"
    normalization_hh_1()  # Приводить файл к к одному формату список словарей как у SJ
    salary_validator_hh()  # Валидатор  по отсутствии зарплаты, удаляет вакансию, перезаписывает файл
    hh_list = creating_vacancies_hh()
    normalization_of_requirement_hh(hh_list)
    for i in hh_list:
        print(i)

    # Парсинг сайта SuperJob
    sj = SaveJsonSJ(key_word, 25)  # 25 - краснодар, 1330 - Мостовской, 3309 - Краснодарский край, 47 - Оренбург
    sj.get_vacancies()  # Запрос к API
    all_file_json(path_sj)  # Формирование одного файла с вакансиями"
    salary_validator_sj()  # Валидатор  по отсутствии зарплаты, удаляет вакансию, перезаписывает файл
    sj_list = creating_vacancies_sj()
    normalization_of_requirement_sj(sj_list)
    for i in sj_list:
        print(i)


if __name__ == "__main__":
    user_interaction()
