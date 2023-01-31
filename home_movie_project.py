"""
A project feladat a következő:

A gépünkön lévő filmekhez fogunk az internetről metaadatokat letölteni
API -on keresztül
Meta adatok: borító képek illetve a filmekhez kapcsolatos szöveges adatok:
pl. rendező, szereplők, rövid ismertető, genre, stb.

Ezeket az adatokat Postgres illetve MongoDB-ben illetve file alapon is külön megoldásként le fogjuk tárolni

A feladat megvalósítása során Docker környezetet is meg fogjuk érintőlegesen ismerni

Az API egy ingyenes használható, puplikus adatbázis lesz, 
http requestek segítségével fogjuk az adatokat lekérni.

A teljes feladat git kezelve lesz

"""

"""
3 féle megoldás lesz: 
1. file alapon tároljuk le a metaadatot
2. postgres-ben tároljuk le a metaadatot
3. mongodb-ben tároljuk le a metaadatot

Feladat lépései:
1. kilistázom a mappában lévő fileokat: kiterjesztés alapján - mkv
2. API hívás: lekérem cím alapján a filmekhez tartozó metaadatokat
3. a metadat alapján letöltöm a képet és kiírom file-ba
4. letárolom a metaadatot

adatbázis kezelése legyen 1 modul: 4. 
file kezelés legyen 1 modul: 1 pont, 3. pont, 4. pont
API kezelés legyen 1 modul

"""

"""
PostgreSQL oldali megoldása a meta data letöltőnek:
a képek maradnak úgy, ahogy vannak
a search_module marad úgy ahogy van

4. letárolom a metaadatot -> a json kiírás helyett, adatbázis betöltésre van szükségünk

"""


"""
Hiba:
nem vizsgáljuk egyik megoldásnál sem, hogy a filmhez van-e letöltve metaadat

Bonyolítás:
ha törlök egy filmet a mappából, akkor mi történjen

ha hozzáadok egy filmet a mappából, akkor mi történjen

"""