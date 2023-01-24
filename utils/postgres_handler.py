from sqlalchemy import create_engine

from utils.connection_params import postgres_url
from utils.sql_helper import create_tmdb_movies, tmdb_tables

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
                temp = conn.execute(select_statement.format(table_name=table))
                
                if temp.fetchone()[0] == 0:
                    conn.execute(cre_script)

if __name__ == '__main__':
    test = PostgresHandler()