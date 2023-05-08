import json

import requests

from src.abs import Parser


# from dotenv import load_dotenv
# load_dotenv()
# api_key = os.getenv('SJ_SECRET_KEY')


class SuperJobAPI(Parser):
    """ название вакансии,
        ссылка на вакансию,
        зарплата,
        краткое описание или требования"""

    def __init__(self, key_word: str, town: int):
        """
        такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования
        :param key_word:
        :param town:
        """
        self.key_word = key_word # ключевое слово для поиска
        self.town = town # код города, где ищем вакансию

    def get_vacancies(self):
        url = 'https://api.superjob.ru/2.0/vacancies/?'
        params = f'keyword={self.key_word}&order_field=date&order_direction=asc&payment_from' \
                 f'=10000&payment_to=300000&no_agreement=1&town={self.town}&catalogues=&type_of_work=0&period=7'
        headers = {
            'X-Api-App-Id': 'v3.r.137537123.a11f0eb0919c5a7678776e135569141eb8c32a88'
                            '.307070a70cc950912e678555eadb8143d9c71338'}
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    def json_saver(self):
        with open("vacancies.json", "w", encoding='UTF-8') as file:
            json.dump(self.get_vacancies(), file, ensure_ascii=False)



sj = SuperJobAPI('Python', 25)

sj.json_saver()
