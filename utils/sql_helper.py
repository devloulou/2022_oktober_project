create_tmdb_movies = """
create table tmdb_movies (
adult boolean,
backdrop_path varchar(100),
id integer primary key,
original_language varchar(10),
original_title varchar(100),
overview text,
popularity real,
poster_path varchar(100),
release_date date,
title varchar(100),
video boolean,
vote_average real,
vote_count integer
)
"""


tmdb_tables = {
    "tmdb_movies": create_tmdb_movies
}