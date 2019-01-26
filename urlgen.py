#import mechanize
from time import sleep
import cik
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import time


def internet_on():
	try:
		requests.get('www.google.com')
		return True
	except: 
		internet_on()
		time.sleep(1)
		print('wtf')

counter=0
file2=open("failed.txt", 'w+')
urllist = []
compciklist = cik.getCikList()
for compcik in compciklist:
	url = ("https://www.sec.gov/Archives/edgar/data/" + str(compcik) + "/index.json")
		#print(url)
	data = requests.get(url).json()
	listdata = data['directory']['item']
	for item in listdata:
		filename = item['name'][:10] + '-' + item['name'][10:12] + '-' + item['name'][12:]
		#print(filename)
		url2 = ("https://www.sec.gov/Archives/edgar/data/" + str(compcik) + "/" + str(item['name'] + "/" + filename + ".txt"))
		try:
			doc = requests.get(url2)
			file=open("CompanyTextFiles/" + str(compcik) +"/" + listdata[counter]['name'], 'w+')
			file.write(doc.text)
		except:
			internet_on()
			try:
				doc = requests.get(url2)
				file=open("CompanyTextFiles/" + str(compcik) +"/" + listdata[counter]['name'], 'w+')
				file.write(doc.text)
			except:
				file2.write(str(compcik) + ": " + str(filename) + ": " + url2+ '\n')

		counter = counter+1
		if counter%100==0:
			print(str(counter) + ": " + compcik)






#missing some quarters in early areas, use try catch