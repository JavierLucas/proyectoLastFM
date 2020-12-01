import pandas as pd 
import datetime as dt

def get_previous_month():
	yesterday = dt.date.today() - dt.timedelta(days = 1)
	firstDay = yesterday.replace(day = 1)
	last_month = firstDay - dt.timedelta(days = 1)
	return last_month


def read_data(filename):
	df = pd.read_excel(filename, sheet_name = get_previous_month().strftime("%Y-%m"))
	return df


#Returns dictionary name: (pos, playcount)
def process_old(filename = "artists.xlsx"):
	df = read_data(filename)
	raw_data = df.to_dict(orient = "split")["data"]

	artists = {}
	for artist in raw_data:
		artists[artist[1]] = (artist[0], artist[2])
	return artists



