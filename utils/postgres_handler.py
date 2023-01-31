from sqlalchemy import create_engine
from sqlalchemy import text

from utils.connection_params import postgres_url
from utils.sql_helper import (create_tmdb_movies,
                                tmdb_tables,
                                insert_tmdb_movies,
                                insert_tmdb_genre_ids)



# nativ sql-re alapozzuk
class PostgresHandler:
    def __init__(self):
        self.engine = create_engine(postgres_url)
        self.create_objects()

    def create_objects(self):
        select_statement = """select count(*) from information_schema.tables t 
                            where t.table_name = '{table_name}'"""        

        with self.engine.connect() as conn:
            for table, cre_script in tmdb_tables.items():
                temp = conn.execute(text(select_statement.format(table_name=table)))
                
                if temp.fetchone()[0] == 0:
                    conn.execute(cre_script)

    def insert_movies(self, data):
        with self.engine.connect() as conn:
            # 1. lépés: az adatot a tmdb_movies-ba be kell tölteni
            # 2. lépés: a genre_id táblába töltjök az id-kat
            # az execute egyben tud bulk insert - tömeges insert
            try:
                conn.execute(text(insert_tmdb_movies), data)
                genre_ids = [{'id': data['id'], 'genre_id': item} for item in data['genre_ids']]       
                conn.execute(text(insert_tmdb_genre_ids), genre_ids)

            except Exception as e:
                print(str(e))

    def delete_data(self):
        with self.engine.connect() as conn:
            conn.execute('delete from tmdb_genre_ids')
            conn.execute('delete from tmdb_movies')

if __name__ == '__main__':
    test = PostgresHandler()

    test_data = {
        "adult": False,
        "backdrop_path": "/3RJ0B8JnwuOaQf6qmwTILXibcJj.jpg",
        "genre_ids": [
            28,
            878,
            14
        ],
        "id": 941520,
        "original_language": "en",
        "original_title": "Alien Sniperess",
        "overview": "A female sniper on military leave promises to fulfill her fiancé’s dying wish until she encounters a hostile alien invasion and is tasked with saving countless lives.",
        "popularity": 278.302,
        "poster_path": "/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg",
        "release_date": "2022-04-08",
        "title": "Alien Sniperess",
        "video": False,
        "vote_average": 3.9,
        "vote_count": 13
    }  

    test.delete_data()
    test.insert_movies(test_data)