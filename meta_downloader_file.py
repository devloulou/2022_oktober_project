"""
import sorrend:

1. helyen a built-in azaz a beépített modulok / package
2. helyen a third party libraryk / modulok / packagek
3. helyen a saját modulok importja
"""
import tmdbsimple as tmdb

from utils.file_handler import FileHandler
from utils.search_module import SearchModule


def meta_data_loader():
    search_obj = tmdb.Search()
    file_handler = FileHandler()
    search = SearchModule(search_obj)

    movies = file_handler.get_data_from_folder()
    # ebben a for ciklusban fog megtörténni minden lépés
    # ami a metaadat letöltéssel / kiírással kapcsolatos
    for movie in movies:
        data = search.search_movie(movie)
        file_handler.set_json_path(movie)
        file_handler.write_json(data)

        file_handler.set_poster_path(movie)
        image_binary = search.get_image_obj_in_binary()
        file_handler.write_image(image_binary)

if __name__ == '__main__':
    meta_data_loader()
