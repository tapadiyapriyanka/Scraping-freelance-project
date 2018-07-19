import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from datetime import datetime
import zipfile, os
import csv

get_year = input("Enter from which year You want data? = ")
current_year = datetime.now().year
print("type of get year = ",type(get_year))
print("type of current year = ",type(current_year))
current_year = str(current_year)[-2:]
print("current year = ",current_year)
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
year = []
while int(get_year) <= int(current_year):
	if len(str(get_year))!=2:
		yr = '0'+str(get_year)
		year.append(yr)
	else:
		yr = str(get_year)
		year.append(yr)
	get_year = int(get_year) + 1
print("year = ",year)


for day in range(1,31):
	if len(str(day)) !=2:
		dayy = '0'+str(day)
	else:
		dayy = str(day)

	for mon in months:
		day_mon = dayy+mon

		for yr in year:
			day_mon_yr = day_mon + yr
			print("day month year = ", day_mon_yr)
			url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_{}.zip'.format(day_mon_yr)
			r = requests.get(url)
			print(r)
			if r.status_code != 200:
				print("files with 404 ",day_mon_yr)   #write into file
				with open("logfile_bse.csv",'a') as file_bse:
					writer = csv.writer(file_bse)
					writer.writerows([[day_mon_yr]])
			else:
				with open(day_mon_yr+".zip", "wb") as code:
					code.write(r.content)
				with ZipFile(day_mon_yr+".zip", 'r') as zip:
					zip.extractall("extracted_folder_bse//")
					print("done")
				os.remove(day_mon_yr+".zip")



	# for day in range(31):
	# 	if len(str(day)) !=2:
	# 		dayy = '0'+str(day)
	# 	else:
	# 		dayy = str(day)
	# for mon in months:
	# 	day_mon = dayy+mon
	
	# 	print("actual day month year string  = ",day_mon_yr) 
	# get_year = int(get_year) + 1
	