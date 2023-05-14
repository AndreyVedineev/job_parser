import json
import os

import requests

references = os.path.join('..', 'src', 'references')  # директория справочники


def all_file_json(path):
    """ Формирование одного файла с вакансиями"""

    # уборка - удаление содержимого файла перед формированием
    open(path, 'w').close()

    # вспомогательный словарь
    # one_list = [x for x in range(len(os.listdir('../src/data')))]
    file_list = []
    for i in range(len(os.listdir('../src/data')) - 1):
        with open('../src/data/{}.json'.format(i + 1), mode='r', encoding='utf8') as file:
            data = json.load(file)
            file_list.append(data)
    # сшивание словаря ключ: номер файла, значение: содержимое запроса
    # all_dict = dict(zip(one_list, file_list))
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


# get_area('https://api.superjob.ru/2.0/regions/combined/')
# get_area('https://api.hh.ru/areas')
