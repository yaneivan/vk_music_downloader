try:
    import os
    from yt_download import find_and_get
    import vk_api
    from vk_api.audio import VkAudio
except:
    os.system('pip install vk_api')
    os.system('pip install requests')
    os.system('pip install beautifulsoup4')

login = input('Your vk email or telephone number    ')  
password =input('Your vk password    ')  
my_id = input('Your vk id Example: @yaneivan    ')  
vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()
vkaudio = VkAudio(vk_session)
count = 0
for track in vkaudio.get_iter():
    count+=1
    search = track.get('artist') + ' ' + track.get('title')
    find_and_get(search)