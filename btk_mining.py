import requests
from bs4 import BeautifulSoup
import re


def btk_siber_dersler():
    titles = []
    headers = {
        'Authorization': 'Bearer ZXlKaGJHY2lPaUpTVXpJMU5pSjkuZXlKemRXSWlPaUl6TnpJMk9DSXNJbVJ2YldGcGJpSTZJa0pVU3lJc0ltbHpjeUk2SWt0Q0lpd2ljR2xrSWpvek9UWXhPQ3dpYjJsa0lqbzFNU3dpWlhod0lqb3hOamc0TmpVeU9UYzRMQ0oxZFdsa0lqb2lNRE0zT0RneFpXSXROalU1TlMwMFl6Y3pMV0UxWldRdE1tSmhOell4WXpGbU5EQm1JaXdpYVdGMElqb3hOamc0TlRZMk5UYzRMQ0pxZEdraU9pSmpaVEF6TVdNMVlTMDNORFF3TFRSaFl6QXRZVGhoTmkxaE9ERXdZVFZrTWpNMk16SWlmUS5MM2dDSDlVQWtRY01VTTB0aHgxT0t1WFNXd21tYWdrd0FfQlVuejdFMFpYVzM2Y2ZKNTRqbG1ENjZaS3owdlJMUmFBWlV1MlhZNHNscjcwZjc2QVpyYkYwNFNwNmlSVzdidXU5Q0s5eUZRUEZzZnJ6TzNPWXB3eDhGa0cwYlRwZUl1NEhkQU8xelFTZ2kzZVA4Q3Ata3QyMVl6ZUlfZDZST0lhdmFVdGdOazE5ekRIX3huUnZ6b0x6YWNTT21IQkd2QlVaX3ZScjF3R2dKWmZFeHgydlM2YTg1S3NZaFU3X25EYm5fMUZsWktydlFGdVB5Y2NabUhLT0NvdHNLMVhyUzh0dVFzNzcwUHNuMS01YU9TUlpqZ002VXNHS2x6cXZEQU0tUy0tUjdwZkxnc1FHMUVQZlVnZ3YzY2N5Yy1Gdm5nbWx2Q0VuRjRqTFl2OGZQeU1Qbmc='
    }

    params = {
        'language': [
            'tr',
            'tr',
        ],
    }
    json_data = {
        'firstResult': 0,
        'maxResults': 70,
        'sortField': 'recent',
        'sortOrder': 'ASCENDING',
        'filter': {
            'documentType': 'course',
            'categoryIds': [
                '1002',
            ],
            'courseTypes': [],
            'localeIds': [],
            'courseLevels': [],
            'demanded': None,
        },
    }
    try:
        response = requests.post(
            'https://www.btkakademi.gov.tr/api/service/v1/public/51/catalog/search',
            #url,
            params=params,
            #cookies=cookies,
            #headers=headers,
            json=json_data,
        )
        json=response.json()
        documents = json["documents"]
        for document in documents :
            title = document["title"]
            titles.append(title)
            # print(title.strip())
    except Expection as e:
        print("Hata",e)
        pass
    return titles



