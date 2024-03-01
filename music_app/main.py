import re, subprocess, requests, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import random
import vk_api
from vk_api.audio import VkAudio


class UserAuthIdentity:
    Login = ''
    Password = ''

    def __init__(self, login, password):
        self.Login = login
        self.Password = password


if __name__ == '__main__':
    while True:
        choice = input('\nВведите что выхотите послушать музончик или видосик(музончик/видосик/выход): ')
        if choice == 'видосик':
            music_name = input("\nВведите название трека для воспроизведения: ")
            query_string = urllib.parse.urlencode(
                {
                    "search_query": music_name
                }
            )
            # кодирования url-адреса Youtube с идентификатором трека:
            # к "https://www.youtube.com/results?search_query=" добавляется идентификатор
            # в итоге получаем (https://www.youtube.com/results?search_query=linkin+park+numb)
            formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

            # Здесь re.findall(r"watch\?v=(\S{11})"
            # отображается 11-символьный идентификатор всех результатов видео по запросу.
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
            random_search_results = random.choice(search_results)

            # После декодирования контента мы можем извлечь полный URL-адрес,
            # объединив основной URL-адрес YouTube с идентификатором из 11 символов.
            # статус получения запроса
            clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(random_search_results))
            # склеиная ссылка по запросу
            clip2 = "https://www.youtube.com/watch?v=" + "{}".format(random_search_results)
            print("Было найдено видео по ссылке: " + clip2)
            inspect = BeautifulSoup(clip.content, "html.parser")
            yt_title = inspect.find_all("meta", property="og:title")
            for concatMusic1 in yt_title:
                print(concatMusic1['content'])

            # Вывод музыки
            vlc_path = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
            # Windows_media_player_path = 'C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe'
            subprocess.Popen([vlc_path, clip2])
            continue

        elif choice == 'музончик':
            Login = ''
            Password = ''
            with open("Auth_ID.txt", 'r') as file:

                identity = file.readlines()
                for item in identity:
                    # убираем значения : c пробелом и \n
                    res = (re.split(": |\n", item))
                    if res[0] == 'Login':
                        Login = res[1]
                    if res[0] == 'Password':
                        Password = res[1]

            obj = UserAuthIdentity(Login, Password)
            vk_session = vk_api.VkApi(obj.Login, obj.Password)
            try:
                vk_session.auth()
            # в случае ошибки аутентификации
            except vk_api.AuthError as error_msg:
                print(error_msg)
                break

            # модуль для получения аудиозаписей без использования официального Api
            vkaudio = VkAudio(vk_session)

            music_name = input("\nВведите название трека для воспроизведения: ")
            sp = vkaudio.search(music_name)
            music_found_url = ''
            music_found_title = ''
            for track in sp:
                music_found_url = track.get('url')
                music_found_title = track.get('title')
                pass

            # Вывод музыки
            vlc_path = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
            Windows_media_player_path = 'C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe'
            print(f"Сейчас играет {music_found_title}")
            subprocess.Popen([vlc_path, music_found_url])
            # subprocess.Popen([Windows_media_player_path, music_found_url])
            continue
        elif choice == 'выход':
            print('Работа программы завершена!')
            break
        else:
            continue
