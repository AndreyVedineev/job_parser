import json
import os

from src.abs import Parser


from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SJ_SECRET_KEY')
path_sj = os.path.join('..', 'src', 'references', 'vacancy_sj.json')  # путь к файлу
references = os.path.join('..', 'src', 'references')

class SuperJobAPI(Parser):
    """ название вакансии,
        ссылка на вакансию,
        зарплата,
        краткое описание или требования"""

    def __init__(self, key_word: str, town: int):
        pass
