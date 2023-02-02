import os

import tmdbsimple as tmdb

from utils.file_handler import FileHandler
from utils.search_module import SearchModule
from utils.postgres_handler import PostgresHandler
from utils.sql_helper import delete_from_genre, delete_from_tmdb_movies


def meta_data_loader():
    search_obj = tmdb.Search()
    file_handler = FileHandler()
    search = SearchModule(search_obj)
    postgres = PostgresHandler()

    poster = file_handler.get_data_from_folder(file_handler.poster_folder)
    movies = file_handler.get_data_from_folder(file_handler.movie_folder)

    diff_del = [item for item in poster if item not in movies]
    diff_download = [item for item in movies if item not in poster]
    # ebben a for ciklusban fog megtörténni minden lépés
    # ami a metaadat letöltéssel / kiírással kapcsolatos
    # postgres.delete_data() #csak a testelés miatt

    #magához a path-okat hozzá kell adni az adathoz
    # ide teszem a törlést

    for item in diff_del:
        file_handler.delete_file(os.path.join(file_handler.poster_folder, item + '.jpg'))
        postgres.run_query(delete_from_genre.format(movie=item))
        postgres.run_query(delete_from_tmdb_movies.format(movie=item))

    for movie in diff_download:
        data = search.search_movie(movie)
        # ide jönnek az adatbázis műveletek
        # data enrichment
        data['poster_location'] = file_handler.poster_folder
        data['movie_location'] = file_handler.movie_folder

        postgres.insert_movies(data)

        file_handler.set_poster_path(movie)
        image_binary = search.get_image_obj_in_binary()
        file_handler.write_image(image_binary)

if __name__ == '__main__':
    meta_data_loader()