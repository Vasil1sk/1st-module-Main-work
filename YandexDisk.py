import requests

class YD:
    URL = "https://cloud-api.yandex.net/v1/disk"
    def __init__(self, token):
        self.token = token

    def get_upload_link(self, disk_file_path):
        upload_url = self.URL + "/resources/upload"
        headers = {
            "Content-type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print("Ссылка для загрузки на Яндекс диск получена")
        return response.json()

    def create_folder(self, folder_name):
        create_url = self.URL + "/resources"
        name = folder_name
        headers = {
            "Content-type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }
        params = {"path": name}
        response = requests.put(create_url, headers=headers, params=params)
        if response.status_code == 201:
            print("Папка успешно создана")
        else:
            print("Ошибка при создании папки")

    def upload_file_to_disk(self, disk_file_path, filename):
        result = self.get_upload_link(disk_file_path=disk_file_path)
        url = result.get("href")
        response = requests.put(url, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Фотография успешно загружена")
        else:
            print("Ошибка при загрузке фотографии")