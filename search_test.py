import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

# http get request-el lekértünk adatot ->JSON-be kaptuk vissza

search = tmdb.Search()
response = search.movie(query='Alien')['results']

# print(search.movie(query='Alien')['results'][0])


"C:\WORK\2022_oktober_project\Poster\Alien.jpg"


import pprint
# pprint.pprint(response[0], indent=4)

# print(response[0])

movie = tmdb.Movies(response[0]['id'])

# for item in movie.credits()['cast']:
#     print(item)

# https://image.tmdb.org/t/p/original/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg
# 
# /vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg

from urllib.request import urlopen

# print(urlopen("https://image.tmdb.org/t/p/original/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg").read())


with open("test.jpg", "wb") as poster:
    poster.write(urlopen("https://image.tmdb.org/t/p/original/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg").read())
