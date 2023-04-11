import requests
from datetime import datetime
import os

class VK:
    URL = "https://api.vk.com/method/"

    def __init__(self, token):
        self.params = {
            "access_token": token,
            "v": "5.131"
        }

    def get_photos_data(self, owner_id, album_id):
        get_photos_url = self.URL + "photos.get"
        print("Метод photos.get создан")
        get_photos_params = {
            "owner_id": owner_id,
            "album_id": album_id,
            "photos_sizes": "0",
            "extended": "1",
        }
        req = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()["response"]["items"]
        print("Данные о фотографиях получены")
        return req

    def get_photos(self, owner_id, album_id, howmuch):
        photos_data = self.get_photos_data(owner_id, album_id)
        path = os.getcwd()
        target_path = os.path.join(path, "Photos")
        print("Путь до папки Photos обнаружен")
        count = 0
        for photo in photos_data:
            photo_url = photo["sizes"][-1]["url"]
            filename = str(photo["likes"]["count"]) + "_" + str(datetime.fromtimestamp(photo["date"]).date())
            photo_req = requests.get(photo_url)
            count += 1
            if count <= howmuch:
                with open(os.path.join(target_path, filename + ".png"), "wb") as file:
                    file.write(photo_req.content)
                    print("Фотография загружена")