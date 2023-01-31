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

create_tmdb_genre_ids = """
create table tmdb_genre_ids (
id integer,
genre_id integer,
CONSTRAINT fk_tmdb_movies
      FOREIGN KEY(id) 
	  REFERENCES tmdb_movies(id)
)
"""

tmdb_tables = {
    "tmdb_movies": create_tmdb_movies,
    "tmdb_genre_ids": create_tmdb_genre_ids
}

# sql template
insert_tmdb_movies = """
insert
	into
	public.tmdb_movies
(adult,
	backdrop_path,
	id,
	original_language,
	original_title,
	overview,
	popularity,
	poster_path,
	release_date,
	title,
	video,
	vote_average,
	vote_count)
values(:adult,
:backdrop_path,
:id,
:original_language,
:original_title,
:overview,
:popularity,
:poster_path,
:release_date,
:title,
:video,
:vote_average,
:vote_count);
"""

insert_tmdb_genre_ids = """
insert into tmdb_genre_ids (
    id,
    genre_id
) values (:id, :genre_id)
"""