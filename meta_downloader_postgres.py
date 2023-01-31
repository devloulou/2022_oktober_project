import tmdbsimple as tmdb

from utils.file_handler import FileHandler
from utils.search_module import SearchModule
from utils.postgres_handler import PostgresHandler


def meta_data_loader():
    search_obj = tmdb.Search()
    file_handler = FileHandler()
    search = SearchModule(search_obj)
    postgres = PostgresHandler()

    movies = file_handler.get_data_from_folder()
    # ebben a for ciklusban fog megtörténni minden lépés
    # ami a metaadat letöltéssel / kiírással kapcsolatos
    postgres.delete_data() #csak a testelés miatt
    for movie in movies:
        data = search.search_movie(movie)
        # ide jönnek az adatbázis műveletek        
        postgres.insert_movies(data)

        file_handler.set_poster_path(movie)
        image_binary = search.get_image_obj_in_binary()
        file_handler.write_image(image_binary)

if __name__ == '__main__':
    meta_data_loader()