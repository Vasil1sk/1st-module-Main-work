from VKPhotos import VK
from YandexDisk import YD
import yaml, json
import os

with open("private.yaml") as f:
    get_data = yaml.load(f, Loader=yaml.FullLoader)
    VK_token = get_data["VK_token"]
    VK_user_id = get_data["VK_user_id"]
    YD_token = get_data["YD_token"]

VK_photos = VK(VK_token)
YaDisk = YD(YD_token)

def download_photos_data(id):
    data_get = VK_photos.get_photos_data(id, "profile")
    with open("PhotosData.json", "w") as f:
        json.dump(data_get, f, indent=4)
        print("Данные о фотографиях успешно загружены")


def upload_photos_to_disk(id, album, delete, folder_name, howmuch=5):
    VK_photos.get_photos(id, album, howmuch)
    path = os.getcwd()
    folder_path = os.path.join(path, "Photos/")
    new_folder = YaDisk.create_folder(folder_name)
    for photo in os.listdir(folder_path):
        i = YaDisk.upload_file_to_disk(disk_file_path=str(folder_name) + "/" + photo, filename=folder_path + photo)
        if delete.lower() == "ДА".lower():
            photo_path = os.path.join(folder_path, photo)
            os.remove(photo_path)

# download_photos_data(VK_user_id)
upload_photos_to_disk(VK_user_id,
                      str(input("Выберите откуда загрузить фото: 'profile': фото профиля, 'wall': со стены, 'saved': сохранённые фотографии, если есть доступ: ")),
                      str(input("Удалить фотографии после загрузки, напишите 'Да' для удаления или введите что угодно для сохранения: ")),
                      str(input("Назовите новую папку на Яндекс диске или укажите уже существующую: ")),
                      int(input("Сколько фотографий загрузить(по умолчанию 5): ")))