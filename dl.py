import os

try:
    import vk_api
    import requests
    import pathlib
except:  # -- Install dependencies -- #
    print('Some dependencies are not installed. Installing...')
    os.system('pip install vk_api colorama requests pyfiglet')


from vk_api.audio import VkAudio
from time import time
from colorama import Fore as cl
from pyfiglet import figlet_format as ff

from cli import *


print(f'{cl.MAGENTA}{ff("VK DL", "doom")}{cl.RESET}')

name_dir = '/downloaded'
path = str(pathlib.Path(__file__).parent.resolve()) + name_dir 

login = input_prompt('VK Login / Phone Number')
password = input_prompt('VK Password')

if login == 'EXIT_APP' or password == 'EXIT_APP':
    import sys
    print('\n\nFinished...')
    os.system(f'rm -f {sys.argv[0].replace("dl.py", "")}vk_config.v2.json')
    os.system(f'rm -f {sys.argv[0].replace("dl.py", "")}__pycache__')

    quit()

if not os.path.exists(path):
    os.makedirs(path)

print(f'\033[1m   Used login\033[0m : {login}')
print(f'\033[1mUsed password\033[0m : {password}\n')

if confirm(action='use this data'):
    pass
else:
    login = input_prompt('VK Login / Phone Number')
    password = input_prompt('VK Password')

    if login == 'EXIT_APP' or password == 'EXIT_APP':
        import sys
        print('\n\nFinished...')
        os.system(f'rm -f {sys.argv[0].replace("dl.py", "")}vk_config.v2.json')
        os.system(f'rm -f {sys.argv[0].replace("dl.py", "")}__pycache__')


        quit()



vk_session = vk_api.VkApi(login=login, password=password)
try:
    vk_session.auth()
except:
    print('\033[1mAUTH FAILED : \033[0m Incorrect login or password')
    quit()

vk = vk_session.get_api()
os.chdir(path)
vkaudio = VkAudio(vk_session)

count = 0


for track in vkaudio.get_iter():

    count+=1

    print(f'\033[1mDownloaded{cl.RESET}: {cl.GREEN}{count}{cl.RESET}')
    print(f"\033[1mArtist{cl.RESET}    : {track.get('artist')}")
    print(f"\033[1mTitle{cl.RESET}     : {track.get('title')}\n")

    r = requests.get(track.get('url'), allow_redirects = True)

    artist = track.get('artist')
    title = track.get('title')

    artist = artist.replace('/', '(')
    artist = artist.replace("'", '`')
    artist = artist.replace('"', '`')
    artist = artist.replace('\\', ')')
    artist = artist.replace('|', ')')
    artist = artist.replace(':', ';')

    title = title.replace('/', '(')
    title = title.replace('"', '`')
    title = title.replace("'", '`')
    title = title.replace('\\', ')')
    title = title.replace('|', ')')
    title = title.replace(':', ';')

    open(f'{path}/{artist}-{title}.mp3', 'wb').write(r.content)


import sys
print('\n\nFinished...')
os.system(f'rm -f {sys.argv[0].replace("dl.py", "")}vk_config.v2.json')
os.system(f'rm -f {sys.argv[0].replace("dl.py", "")}__pycache__')
