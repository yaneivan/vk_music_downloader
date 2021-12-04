def convert_all():
	path = 'music/'
	import os
	for filename in os.listdir(path):
		new_name = filename[:len(filename)-5] + '.mp3'
		command = 'ffmpeg.exe -y -hide_banner -loglevel error -i "'+path+ filename+'" "'+path+ new_name+'"'
		os.system(command)
		deleting = path + '/' + filename
		os.remove(deleting)
