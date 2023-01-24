from urllib.request import urlopen

import tmdbsimple as tmdb

# https://image.tmdb.org/t/p/original/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg
class SearchModule:
    tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'
    image_server = "https://image.tmdb.org/t/p/original"

    def __init__(self, search_obj: tmdb.Search):
        # ez nem szép megoldás -> Dependecy Injection - SOLID 
        # self.search = tmdb.Search()  # példányosítás -> objektum fog létrejönni
        self.search = search_obj
        self.poster_path = None

    def search_movie(self, title):
        # search.movie(query='Alien')['results']
        movie_meta = self.search.movie(query=title)['results']
        if not movie_meta:
            return False

        self.poster_path = movie_meta[0]['poster_path']
        return movie_meta[0]

    def get_image_obj_in_binary(self):        
        return urlopen(f"{self.image_server}{self.poster_path}").read()


if __name__ == '__main__':
    search_obj = tmdb.Search()
    test = SearchModule(search_obj)

    print(test.search_movie('Alien'))
    print(test.get_image_obj_in_binary())
