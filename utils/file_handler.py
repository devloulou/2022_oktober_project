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
        self.poster_path = None

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

    @staticmethod
    def get_data_from_folder(folder_path):
        """
        1. Nézzük meg, hogy létezik e a folder
        2. kislistázzuk os.listdir -el a mappa tartalmát - kiterjsztés vizsgálat!!
        3. itt elég csak a file-ok neve -> nem kell a teljes elérési útvonal
        """
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"{folder_path} is not exists!")

        # temp = []
        # for item in os.listdir(self.__movie_folder):
        #     if item[-4:] == '.mkv':
        #         temp.append(item[:-4])

        return [item[:-4].replace(".", '') for item in os.listdir(folder_path) if item.endswith(('.mkv', '.json', '.jpg'))]

    def write_json(self, data):
        """
        itt elő kell állítani path a json-höz
        """
        if not os.path.exists(self.metadata_folder):
            raise FileNotFoundError(f"{self.metadata_folder} is not exists!")
        
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    # elv: egy függvény 1 dologért legyen felelős -> clean code
    def set_json_path(self, movie_name):
        self.json_path = os.path.join(self.metadata_folder, f"{movie_name}.json")

    def set_poster_path(self, movie_name):
        self.poster_path = os.path.join(self.poster_folder, f"{movie_name}.jpg")

    def write_image(self, image_binary):
        try:
            with open(self.poster_path, "wb") as poster:
                poster.write(image_binary)
        except Exception as e:
            return False, str(e)

    @staticmethod
    def delete_file(file_path):
        if not os.path.exists(file_path):
            print(f"The given file: {file_path} not exists!")
            return
        os.remove(file_path)

if __name__ == '__main__':
    test = FileHandler()

    # test.get_json_path('Alien')
    # test.write_json({'adult': False, 'backdrop_path': '/3RJ0B8JnwuOaQf6qmwTILXibcJj.jpg', 'genre_ids': [28, 878, 14], 'id': 941520, 'original_language': 'en', 'original_title': 'Alien Sniperess', 'overview': 'A female sniper on military leave promises to fulfill her fiancé’s dying wish until she encounters a hostile alien invasion and is tasked with saving countless lives.', 'popularity': 315.116, 'poster_path': '/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg', 'release_date': '2022-04-08', 'title': 'Alien Sniperess', 'video': False, 'vote_average': 3.9, 'vote_count': 13})

    meta = test.get_data_from_folder(r'C:\WORK\2022_oktober_project\Metadata')
    movies = test.get_data_from_folder(r'C:\WORK\2022_oktober_project\movies')

    diff_del = [item for item in meta if item not in movies]

    diff_download = [item for item in movies if item not in meta]
    # a diff az, amit le kell törölni
    
    print(f"diff_del: {diff_del}")
    print(f"diff_download: {diff_download}")