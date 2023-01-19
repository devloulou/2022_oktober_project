import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

# http get request-el lekértünk adatot ->JSON-be kaptuk vissza

search = tmdb.Search()
response = search.movie(query='Alien')['results']

import pprint
# pprint.pprint(response[0], indent=4)

print(response[0])

movie = tmdb.Movies(response[0]['id'])

# for item in movie.credits()['cast']:
#     print(item)

# https://image.tmdb.org/t/p/original/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg