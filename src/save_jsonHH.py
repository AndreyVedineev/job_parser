import json
import os

import requests

from src.abs import SaveVac
from src.utils import all_file_json, normal_hh

path_hh = os.path.join('..', 'src', 'references', 'vacancy_hh.json')  # путь к файлу


class SaveJsonHH(SaveVac):
    """
           соднание списка вакансий в файле save_jsonHH.json с сайта HeadHunter
           :param key_word: ключевое слово для поиска вакансий
           :param town: код города, код города в файле town.json
           """

    def __init__(self, key_word: str, town: int):
        self.key_word = key_word  # ключевое слово для поиска
        self.town = town  # код города, где ищем вакансию
        self.page_number = 0
        self.url = 'https://api.hh.ru/vacancies?'
        self.min_payment = 0

    def get_vacancies(self):
        """ Создание файлов с вакансиями """
        params = {'text': self.key_word, 'area': self.town, 'page': self.page_number, 'per_page': 20}
        headers = {'User-Agent': 'K_ParserApp/1.0'}

        response = requests.get(self.url, params=params, headers=headers)
        data = response.json()
        print(f"Всего вакансий: {data['found']}")
        print(f"Всего страниц: {data['pages']}")

        for i in range(data['pages']):
            param_cycle = {'text': self.key_word, 'area': self.town, 'page': i}
            response_cycle = requests.get(self.url, params=param_cycle, headers=headers)
            print('Запрос №' + str(i))
            result = response_cycle.json()
            next_file_name = '../src/data/{}.json'.format(len(os.listdir('../src/data')))
            f = open(next_file_name, mode='w', encoding='utf8')
            f.write(json.dumps(result['items'], ensure_ascii=False))
            f.close()


def salary_validator_hh():
    """Валидатор  по отсутствии зарплаты
        перезаписывает файл """
    count = 0
    temp_list = []
    with open(path_hh, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        for i in templates:
            if i['salary'] is not None:
                count += 1
                temp_list.append(i)
                print(f" {i['name']} -  от {i['salary']['from']} до {i['salary']['to']} ")
    print(count)
    with open(path_hh, "w", encoding='UTF-8') as file:
        json.dump(temp_list, file, ensure_ascii=False)


# hh = SaveJsonHH('Python', 1438)  # 53 - Краснодар. 2444 - Мостовской. 1438 - Краснодарский край 70 - Оренбург
# hh.get_vacancies()
# all_file_json(path_hh)
# normal_hh()
# salary_validator_hh()

