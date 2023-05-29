import os

from src.JSONSaver import JSONSaver
from src.save_jsonHH import SaveJsonHH
from src.save_jsonSJ import SaveJsonSJ
from src.utils import *

# all_file_json, normalization_hh_1, salary_validator_hh, creating_vacancies_hh, \
# normalization_of_requirement_hh, salary_validator_sj, creating_vacancies_sj, normalization_of_requirement_sj, \
# average_salary, create_dir_data, del_folder

path_hh = os.path.join('', 'references', 'vacancy_hh.json')  # путь к файлу с вакансиями HH
path_sj = os.path.join('', 'references', 'vacancy_sj.json')  # путь к файлу с вакансиями SJ


def user_interaction():
    """ Эта программа для поиска вакансий,  на сайтах SuperJob и HeadHunter."""

    print('Эта программа для поиска вакансий, на сайтах SuperJob и HeadHunter.')

    print('Введите ключевое слово для поиска вакансии:')
    key_word = input().strip()
    # print('Введите код города')
    # key_town = int(input().strip())

    # создаю временную папку для работы с файлами
    create_dir_data()

    # # Парсинг сайта HeadHunter
    hh = SaveJsonHH(key_word, 53)  # 53 - Краснодар. 2444 - Мостовской. 1438 - Краснодарский край 70 - Оренбург
    hh.get_vacancies()  # Запрос к API
    all_file_json(path_hh)  # Формирование одного файла с вакансиями"
    normalization_hh_1()  # Приводить файл к к одному формату список словарей как у SJ
    salary_validator_hh()  # Валидатор  по отсутствии зарплаты,
    hh_list = creating_vacancies_hh()  # Создание экемпляров вакансий
    normalization_of_requirement_hh(hh_list)

    # Парсинг сайта SuperJob
    sj = SaveJsonSJ(key_word, 25)  # 25 - краснодар, 1330 - Мостовской, 3309 - Краснодарский край, 47 - Оренбург
    sj.get_vacancies()  # Запрос к API
    all_file_json(path_sj)  # Формирование одного файла с вакансиями"
    salary_validator_sj()  # Валидатор
    sj_list = creating_vacancies_sj()
    normalization_of_requirement_sj(sj_list)

    del_folder()
    # обработка вакансий
    general_list_of_vacancies = hh_list + sj_list
    general_list_of_vacancies_sort = sorted(general_list_of_vacancies, key=lambda x: x.salary_from, reverse=True)
    print(f'Всего по ключевому слову {key_word} удалось получить: {len(general_list_of_vacancies)} вакансий.')

    num_top = get_top_number()
    for i in general_list_of_vacancies_sort[:num_top]:
        print(i)
    print(f'Средняя зарплата: {round(average_salary(general_list_of_vacancies_sort))} руб.')

    json_saver = JSONSaver(general_list_of_vacancies_sort)

    print("Запись всех вакансий в файл vacancy.json")
    json_saver.add_vacancy()

    print('Введите интересующий Вас диапазон зарплаты в формате "100000-150000"')
    param = input().strip()
    json_saver.get_vacancies_by_salary(param)
    print('Записываю все интересующие Вас вакансий в файл vacancyft.json')

    print('Удаляю все закрытые вакансии, записываю в файл vacancyop.json"')
    json_saver.delete_close_vacancy()


def get_top_number():
    """просим пользователя ввести число"""
    while True:
        try:
            num = int(input("Введите количество вакансий для вывода в топ N: "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


if __name__ == "__main__":
    user_interaction()
