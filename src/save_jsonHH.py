import json
import os

import requests

from src.abs import SaveVac

from fake_useragent import UserAgent


class ParsingErorr(Exception):
    pass


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
        headers = {'User-Agent': UserAgent().chrome}
        # headers = {'User-Agent': 'K_ParserApp/1.0'}

        response = requests.get(self.url, params=params, headers=headers)
        data = response.json()
        count_data = data['pages']

        for i in range(count_data):
            param_cycle = {'text': self.key_word, 'area': self.town, 'page': i}
            try:
                response_cycle = requests.get(self.url, params=param_cycle, headers=headers)
                print(f'Запрос № {str(i)} к сайту HeadHunter')
                if response_cycle.status_code != 200:
                    raise ParsingErorr(f"Ошибка получения вакансий! Статус: {response_cycle.status_code}")
            except ParsingErorr as e:
                print(e)
            result = response_cycle.json()
            next_file_name = '../src/data/{}.json'.format(len(os.listdir('../src/data')))
            f = open(next_file_name, mode='w', encoding='utf8')
            f.write(json.dumps(result['items'], ensure_ascii=False))
            f.close()

    def __str__(self):
        return self
