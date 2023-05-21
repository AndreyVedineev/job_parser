import os

from src.save_jsonHH import salary_validator_hh, SaveJsonHH
from src.save_jsonSJ import SaveJsonSJ, salary_validator_sj
from src.utils import creating_vacancies_hh, normalization_hh_1, all_file_json, creating_vacancies_sj

path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу с вакансиями HH
path_sj = os.path.join('..', 'src', 'references', 'vacancy_sj.json')  # путь к файлу с вакансиями SJ


def user_interaction():
    print(""" Эта программа для поиска вакансий,  на сайтах SuperJob и HeadHunter.
    """)
    #Парсинг сайта HeadHunter
    hh = SaveJsonHH('Водитель', 53)  # 53 - Краснодар. 2444 - Мостовской. 1438 - Краснодарский край 70 - Оренбург
    hh.get_vacancies()  # Запрос к API
    all_file_json(path_hh)  # Формирование одного файла с вакансиями"
    normalization_hh_1()  # Приводить файл к к одному формату список словарей как у SJ
    salary_validator_hh()  # Валидатор  по отсутствии зарплаты, удаляет вакансию, перезаписывает файл
    creating_vacancies_hh() # создает список вакансий с ссайта HH

    # Парсинг сайта SuperJob
    sj = SaveJsonSJ('Водитель', 25) # 25 - краснодар, 1330 - Мостовской, 3309 - Краснодарский край, 47 - Оренбург
    sj.get_vacancies() # Запрос к API
    all_file_json(path_sj) # Формирование одного файла с вакансиями"
    salary_validator_sj() # Валидатор  по отсутствии зарплаты, удаляет вакансию, перезаписывает файл
    creating_vacancies_sj()


if __name__ == "__main__":
    user_interaction()
