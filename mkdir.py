import os
import cik



urllist = []
ciks = cik.getCikList()
for ciknum in ciks:
	try:
		os.mkdir('CompanyTextFiles/' + ciknum)
	except:
		print(ciknum)