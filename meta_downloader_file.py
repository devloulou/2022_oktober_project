"""
import sorrend:

1. helyen a built-in azaz a beépített modulok / package
2. helyen a third party libraryk / modulok / packagek
3. helyen a saját modulok importja
"""
import os
import tmdbsimple as tmdb

from utils.file_handler import FileHandler
from utils.search_module import SearchModule

def meta_data_loader():
    search_obj = tmdb.Search()
    file_handler = FileHandler()
    search = SearchModule(search_obj)

    meta = file_handler.get_data_from_folder(file_handler.metadata_folder)
    movies = file_handler.get_data_from_folder(file_handler.movie_folder)

    diff_del = [item for item in meta if item not in movies]
    diff_download = [item for item in movies if item not in meta]

    # a törlési logiát ide kell implementálni
    for item in diff_del:
        file_handler.delete_file(os.path.join(file_handler.metadata_folder, item + '.json'))
        file_handler.delete_file(os.path.join(file_handler.poster_folder, item + '.jpg'))

    # ebben a for ciklusban fog megtörténni minden lépés
    # ami a metaadat letöltéssel / kiírással kapcsolatos
    for movie in diff_download:
        data = search.search_movie(movie)
        file_handler.set_json_path(movie)
        file_handler.write_json(data)

        file_handler.set_poster_path(movie)
        image_binary = search.get_image_obj_in_binary()
        file_handler.write_image(image_binary)

if __name__ == '__main__':
    meta_data_loader()
