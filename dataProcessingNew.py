import requests

def get_LastFM(payload):
	url = 'http://ws.audioscrobbler.com/2.0/'
	USER_AGENT = "jlucasaura"
	API_KEY = "761792064ea8e9d21926749f62b19f03"

	headers = {
		'user-agent': USER_AGENT
	}

	payload['api_key'] = API_KEY
	payload['format'] = 'json'

	response = requests.get(url, headers = headers, params = payload)

	return response

def get_artists(limit = 5, period = "1month"):
	args = {
		"method": "user.gettopartists",
		"period": period,
		"limit": limit,
		"user": "jlucasaura"
	}

	return get_LastFM(args).json()

#Returns dictionary name: (pos, playcount)
def process_new():
	artists = {}
	raw_artists = get_artists(75)["topartists"]["artist"]
	
	for idx, artist in enumerate(raw_artists):
		artists[artist["name"]] = (idx + 1, int(artist["playcount"]))
	return artists





	
