try:
    import os
    import time
    from yt_download import find_and_get
    from convert import convert_all
    import vk_api
    from vk_api.audio import VkAudio
except:
    os.system('pip install vk_api')
    os.system('pip install requests')
    os.system('pip install beautifulsoup4')
t0 = time.time()
login = input('Your vk email or telephone number    ')  
password =input('Your vk password    ')  
my_id = input('Your vk id. Example: @yaneivan    ')  
vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()
vkaudio = VkAudio(vk_session)
count = 0

print('\nGetting the audio list...')
t1 = time.time()
all_audios = vkaudio.get()
t2 = time.time()
print('Got', len(all_audios), 'songs! That took', str(t2-t1), 'seconds.')

print('\nStarting download...')
t1 = time.time()
for track in all_audios:
    count+=1
    if count%30==0:
        print(count, 'tracks done.')
    search = track.get('artist') + ' ' + track.get('title')
    find_and_get(search)
t2 = time.time()
print('Download finished in', str((t2-t1)/60), 'minutes.')
print('\nStarting conversion...')
t1 = time.time()
convert_all()
t2 = time.time()
print('\nConversion finished in', str((t2-t1)/60), 'minutes.')

tFin = time.time()
print('Programm finished, all that took', str((tFin - t0)/60), 'minutes.')