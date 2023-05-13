import json
import os

import requests

path_hh = os.path.join('..', 'src', 'vacancy_hh.json')  # путь к файлу


class SaveJsonHH:
    def __init__(self, key_word: str, town: int):
        """
        соднание списка вакансий в файле vacansj.json с сайта SuperJob
        :param key_word: ключевое слово для поиска вакансий
        :param town: код города, код города в файле town.json
        """
        self.key_word = key_word  # ключевое слово для поиска
        self.town = town  # код города, где ищем вакансию
        self.page_number = 0
        self.url = 'https://api.hh.ru/vacancies?'


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


def one_file_json_hh():
    """ Формирование одного файла с вакансиями, словарь ключ: номер файла, значение json из запросов"""

    # уборка - удаление содержимого файла перед формированием
    open(path_hh, 'w').close()

    # one_list = [x for x in range(len(os.listdir('../src/data')))]
    two_list = []
    for i in range(len(os.listdir('../src/data'))):
        with open('../src/data/{}.json'.format(i), mode='r', encoding='utf8') as file:
            data = json.load(file)
            two_list.append(data)

    # all_dict = dict(zip(one_list, two_list))
    with open(path_hh, 'w', encoding='utf8') as fp:
        json.dump(two_list, fp, ensure_ascii=False)
    # уборка - удаление всех файлов из директории data/
    filelist = [f for f in os.listdir('../src/data/') if f.endswith(".json")]
    for f in filelist:
        os.remove(os.path.join('../src/data/', f))


def read_hh():
    count = 0
    with open(path_hh, "r", encoding='UTF-8') as file:
        templates = json.load(file)
        for i in templates:
            for j in i:
                count += 1
                print(f" {j['name']} - {j['salary']}")
    print(count)


hh = SaveJsonHH('', 53)  # 53 - Краснодар. 2444 - Мостовской
hh.get_vacancies()
one_file_json_hh()
read_hh()
