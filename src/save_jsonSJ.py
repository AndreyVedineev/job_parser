import json
import os

import requests
from dotenv import load_dotenv

from src.utils import all_file_json

load_dotenv()
api_key = os.getenv('SJ_SECRET_KEY')

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
            headers = {
                'X-Api-App-Id': 'v3.r.137537123.a11f0eb0919c5a7678776e135569141eb8c32a88'
                                '.307070a70cc950912e678555eadb8143d9c71338'}

            response = requests.get(self.url, params=params, headers=headers)
            print('Запрос №' + str(number))
            result_sj = response.json()

            if result_sj['objects']:
                next_file_name = '../src/data/{}.json'.format(len(os.listdir('../src/data')))
                f = open(next_file_name, mode='w', encoding='utf8')
                f.write(json.dumps(result_sj['objects'], ensure_ascii=False))
                f.close()
                number += 1
            else:
                break


def salary_validator_sj():
    count = 0
    temp_list = []
    with open(path_sj, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        for i in templates:
            for j in i:
                if j['payment_from'] != 0:
                    temp_list.append(j)
                    count += 1
    with open(path_sj, "w", encoding='UTF-8') as file:
        json.dump(temp_list, file, ensure_ascii=False)
    print(count)


sj = SaveJsonSJ('Python', 25)
sj.get_vacancies()
all_file_json(path_sj)
salary_validator_sj()
