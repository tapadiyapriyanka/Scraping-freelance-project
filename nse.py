import requests
import zipfile, os
from bs4 import BeautifulSoup
from zipfile import ZipFile
from datetime import datetime
import csv

get_year = input("Enter from which year you want to get data?? = ")
current_year = datetime.now().year
diff = current_year - int(get_year)
all_years = []
all_years.append(get_year)
for i in range(diff):
    a = get_year
    b = int(a)+1
    all_years.append(str(b))
    get_year = b

print("all_years = ",all_years) 
all_months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

for yr in all_years:
    for mon in all_months:
        for day in range(31):
            whole_date = str(day)+mon+yr
            url = 'https://www.nseindia.com/content/historical/EQUITIES/{}/{}/cm{}bhav.csv.zip'.format(yr, mon, whole_date)
            r = requests.get(url)
            if r.status_code != 200:
            	print("files with 404 ",whole_date)   #write into file
            	with open("logfile.csv",'a') as logfile:
            		writer = csv.writer(logfile)
            		writer.writerows([[whole_date]])
            else:
            	with open(whole_date+".zip", "wb") as code:
            		code.write(r.content)
            	with ZipFile(whole_date+".zip", 'r') as zip:
            		zip.extractall("extracted_folder//")
            		print("done")
            	os.remove(whole_date+".zip")


# ___________________________________________________________
# # url = 'https://www.nseindia.com/content/historical/EQUITIES/2018/MAR/cm13MAR2018bhav.csv.zip'
# https://www.nseindia.com/ArchieveSearch?h_filetype=eqbhav&date=13-03-2015&section=EQ










# https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_070917.zip
# https://www.bseindia.com/download/BhavCopy/Equity/EQ070917_CSV.ZIP