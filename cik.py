import csv


def tickerLookup(ticker):
	with open('cik_ticker.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='|')
		for row in reader:
			if(row['Ticker'] == ticker):
				return row['CIK']

def getCikList():
	ciklist = []
	with open('cik_ticker.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='|')
		for row in reader:
			ciklist.append(row['CIK'])
	return ciklist

def cikLookup(cik):
	with open('cik_ticker.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='|')
		for row in reader:
			if(row['CIK']== cik):
				return row['Ticker']

def getTickerList():
	ticklist = []
	with open('cik_ticker.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter='|')
		for row in reader:
			ticklist.append(row['Ticker'])
	return ticklist