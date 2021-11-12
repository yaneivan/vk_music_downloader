import os
os.system('pip install vk_api')
os.system('pip install requests')
os.system('pip install beautifulsoup4')
import vk_api
from vk_api.audio import VkAudio
import requests
from time import time
import pathlib

name_dir = '\\mus1c_by_m9'
path = str(pathlib.Path(__file__).parent.resolve()) + name_dir 
login = input('Your vk login or telephone number    ')  
password =input('Your vk password    ')  
my_id = input('Your vk id Example: @yaneivan    ')  
if not os.path.exists(path):
    os.makedirs(path)
vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()
os.chdir(path)
vkaudio = VkAudio(vk_session)
count = 0
for track in vkaudio.get_iter():
    count+=1
    print(f"Исполнитель: {track.get('artist')}")
    print(f"Название трека: {track.get('title')}")
    print(f"Ссылка на трек(url) : {track.get('url')}")
    print('----------------------' +str(count)+'----------------------')
    r = requests.get(track.get('url'), allow_redirects = True)
    artist = track.get('artist')
    artist = artist.replace('/', '(')
    artist = artist.replace("'", '`')
    artist = artist.replace('"', '`')
    artist = artist.replace('\\', ')')
    artist = artist.replace('|', ')')
    artist = artist.replace(':', ';')
    title = track.get('title')
    title = title.replace('/', '(')
    title = title.replace('"', '`')
    title = title.replace("'", '`')
    title = title.replace('\\', ')')
    title = title.replace('|', ')')
    title = title.replace(':', ';')
    open(path +'\\'+ artist+title+'.mp3', 'wb').write(r.content)