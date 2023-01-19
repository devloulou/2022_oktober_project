import os
import json

class FileHandler:
    # class attributok - ő az osztályhoz tarozik
    # valami/valami/fo_mappa
    # C:\WORK\2022_oktober_project/Poster
    
    poster_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Poster') 
    metadata_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Metadata')

    def __init__(self):
        # self-el ellátott attribútumok azok az instance attributumok 
        # - az objekthez tartoznak
        self.__movie_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'movies') 
        self.__create_necessary_folders()
        self.json_path = None

    @property
    def movie_folder(self):
        pass

    @movie_folder.getter
    def movie_folder(self):
        return self.__movie_folder

    @movie_folder.setter
    def movie_folder(self, mfolder):
        self.__movie_folder = mfolder

    def __create_necessary_folders(self):
        # Poster - Metadata creation
        if not os.path.exists(self.poster_folder):
            os.mkdir(self.poster_folder)
        if not os.path.exists(self.metadata_folder):
            os.mkdir(self.metadata_folder)

    def get_data_from_folder(self):
        """
        1. Nézzük meg, hogy létezik e a folder
        2. kislistázzuk os.listdir -el a mappa tartalmát - kiterjsztés vizsgálat!!
        3. itt elég csak a file-ok neve -> nem kell a teljes elérési útvonal
        """
        if not os.path.exists(self.__movie_folder):
            raise FileNotFoundError(f"{self.__movie_folder} is not exists!")

        # temp = []
        # for item in os.listdir(self.__movie_folder):
        #     if item[-4:] == '.mkv':
        #         temp.append(item[:-4])

        return [item[:-4] for item in os.listdir(self.__movie_folder) if item[-4:] == '.mkv']

    def write_json(self, data):
        """
        itt elő kell állítani path a json-höz
        """
        if not os.path.exists(self.metadata_folder):
            raise FileNotFoundError(f"{self.metadata_folder} is not exists!")
        
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    # elv: egy függvény 1 dologért legyen felelős -> clean code
    def get_json_path(self, movie_name):
        self.json_path = os.path.join(self.metadata_folder, f"{movie_name}.json")

if __name__ == '__main__':
    test = FileHandler()

    test.get_json_path('Alien')
    test.write_json({'adult': False, 'backdrop_path': '/3RJ0B8JnwuOaQf6qmwTILXibcJj.jpg', 'genre_ids': [28, 878, 14], 'id': 941520, 'original_language': 'en', 'original_title': 'Alien Sniperess', 'overview': 'A female sniper on military leave promises to fulfill her fiancé’s dying wish until she encounters a hostile alien invasion and is tasked with saving countless lives.', 'popularity': 315.116, 'poster_path': '/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg', 'release_date': '2022-04-08', 'title': 'Alien Sniperess', 'video': False, 'vote_average': 3.9, 'vote_count': 13})
