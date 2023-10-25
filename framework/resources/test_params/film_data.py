import json

class BaseFilm:
    film_title = ''
    country = ''
    genre = ''

    if film_title == '' and country == '' and genre == '':
        with open('../../framework/resources/test_params/film.json', 'r') as file:
            data = json.loads(file.read())
            film_title = data['film_title']
            country = data['country']
            genre = data['genre']

