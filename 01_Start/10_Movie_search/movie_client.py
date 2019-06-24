import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres'
)


class MovieClient:
    def __init__(self, search_text):
        self.search_text = search_text

    def perform_search(self):
        url = f'http://movie_service.talkpython.fm/api/search/{self.search_text}'

        r = requests.get(url)
        r.raise_for_status()

        movie_data = r.json()
        movies_list = movie_data.get('hits')


        movies = [
            MovieResult(**m)
            for m in movies_list
            ]
        movies.sort(key=lambda m: m.title)

        return movies