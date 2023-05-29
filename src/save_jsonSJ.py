import json
import os

import requests
from config import SJ_SECRET_KEY
from src.abs import ParsingErorr

path_sj = os.path.join('..', 'src', 'references', 'vacancy_sj.json')  # путь к файлу


class SaveJsonSJ:
    def __init__(self, key_word: str, town: int):
        """
        соднание списка вакансий в файле vacansj.json с сайта SuperJob
        :param key_word: ключевое слово для поиска вакансий
        :param town: код города, код города в файле town.json
        """
        self.key_word = key_word  # ключевое слово для поиска
        self.town = town  # код города, где ищем вакансию
        self.url = 'https://api.superjob.ru/2.0/vacancies/?'

    def get_vacancies(self):
        global result_sj
        number = 0
        while True:

            params = {'keyword': self.key_word,
                      'order_field': 'date',
                      'order_direction': 'asc',
                      'payment_from': 1,
                      'payment_to': 500000,
                      'no_agreement': 1,
                      'town': {self.town},
                      'page': number,
                      'count': 20
                      }
            headers = {'X-Api-App-Id': SJ_SECRET_KEY}
            try:
                response = requests.get(self.url, params=params, headers=headers)
                print(f'Запрос № {str(number)} к сайту SuperJob')
                result_sj = response.json()
            except ConnectionResetError as e:
                print(ParsingErorr("Ошибка получения вакансии - ", e))

            if result_sj['objects']:
                next_file_name = '../src/data/{}.json'.format(len(os.listdir('../src/data')))
                f = open(next_file_name, mode='w', encoding='utf8')
                f.write(json.dumps(result_sj['objects'], ensure_ascii=False))
                f.close()
                number += 1
            else:
                break
