def find_and_get(search):
	search = search.replace("'", '')
	try:
		from pytube import YouTube
		from youtube_search import YoutubeSearch
		import json
	except:
		import os
		os.system('pip install pytube')
		os.system('pip install youtube-search')
		from pytube import YouTube
		from youtube_search import YoutubeSearch


	results = YoutubeSearch(search, max_results = 3).to_json()
	results = json.loads(results)
	link = 'youtube.com' + results['videos'][0]['url_suffix']
	yt = YouTube(link)

	stream = yt.streams.filter(only_audio=True)

	arr = []
	for i in stream:
		arr.append(int(i.abr[:-4]))
	arr.sort(key = lambda x: -x)
	for i in stream:
		if int(i.abr[:-4]) == arr[0]:
			extan = i.mime_type
			extan = extan[6:]
			name = str(yt.title) +' (' + search +').'+ extan
			name = name.replace('"', '')
			name = name.replace('/', '')
			name = name.replace('!', '')
			name = name.replace('?', '')
			name = name.replace('|', '')
			name = name.replace('\\', '')
			name = name.replace(':', '')
			#print(search)
			try:
				i.download(output_path ='music', filename = name)
			except:
				print(name)