from dataProcessingNew import process_new
from dataProcessingOld import process_old

def analyse_data(filename):
	old_artists = process_old(filename)
	new_artists = process_new()

	analysed = []
	for name, data in new_artists.items():
		if old_artists.get(name):
			old = old_artists.get(name)
			analysed.append([name, data[1], old[0] - data[0], data[1] - old[1]])
		else:
			analysed.append([name, data[1], "NEW", "NEW"])
	return analysed

def salidas_lista(filename):
	old_artists = process_old(filename)
	new_artists = process_new()

	salidas = []

	for name, data in old_artists.items():
		if not new_artists.get(name):
			salidas.append([name, data[0], data[1]])
	return salidas


def max_sub(analysed):
	final = []
	max_rep = 0

	for idx, artist in enumerate(analysed):
		#print(artist)
		if (artist[2] != "NEW" and artist[2] > max_rep):
			artist[0] = f"{idx + 1}. {artist[0]}"
			final = artist
			max_rep = artist[2]
	return final

def max_caida(analysed):
	final = []
	caida = 0

	for idx, artist in enumerate(analysed):
		#if (artist[2] != "NEW" and artist[2] < caida) or not final:
		if (artist[2] != "NEW" and artist[2] < caida):
			artist[0] = f"{idx + 1}. {artist[0]}"
			final = artist
			caida = artist[2]
	return final

def entrada_fuerte(analysed):

	for idx, artist in enumerate(analysed):
		if artist[2] == "NEW":
			artist[0] = f"{idx + 1}. {artist[0]}"
			return artist


def further_info(filename):
	analysed = analyse_data(filename)
	data = []
	data.append(max_sub(analysed))
	data.append(max_caida(analysed))
	data.append(entrada_fuerte(analysed))
	return data


