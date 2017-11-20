import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen as uReq  
import sys
import warnings
import time
import random

warnings.filterwarnings("ignore")

USERNAME = raw_input()
PASSWORD = raw_input()


cdata = []
pydata = []
mathdata = []
chemdata = []
ecodata = []
engdata = []
	

while(1):

	num = random.randint(1,10000)
	# Login
	with requests.Session() as c:
		url = 'https://lms.iiitb.ac.in/moodle/login/index.php'
		c.get(url, verify=False)
		login_data = dict(username = USERNAME,password = PASSWORD,next = '/')
		c.post(url, data = login_data)


		# Sraping for C Language Assignments
		page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=929')	
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		clang = []
		for link in soup.findAll('td',{'class': 'cell c1'}):
			title = link.string
			clang.append(title)
		f = open("Assignment"+str(num)+".txt",'w')
		f.write("C Assignment --------------------------------------------------------------------\n")
		c1 = 0
		for i in clang:
			if i not in cdata:
				c1 += 1
				f.write(str(i) + " has been uploded, with date and time: " + str(time.strftime('%X %x %Z'))+'\n')
		if(c1 == 0):
			f.write("No New Update " + str(time.strftime('%X %x %Z')) + "\n")
		cdata = clang

		print "---------------------------------"

		# Scraping for Python Assignments
		page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=920')
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		py = []
		for link in soup.findAll('td',{'class': 'cell c1'}):
			title = link.string
			py.append(title)
		py1 = 0
		f.write("\nPython Assignment --------------------------------------------------------------------\n")
		for i in py:
			if i not in pydata:
				py1  += 1
				f.write(str(i) + " has been uploded, with date and time: " + str(time.strftime('%X %x %Z'))+'\n')
		if(py1 == 0):
			f.write("No New Update "+ str(time.strftime('%X %x %Z')) + "\n")
		pydata = py		


		print "---------------------------------"	

		# Scraping for Math Assignments
		page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=919')
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		math = []
		for link in soup.findAll('td',{'class': 'cell c1'}):
			title = link.string
			math.append(title)
		math1 = 0
		f.write("\nMath Assignment --------------------------------------------------------------------\n")
		for i in math:
			if i not in mathdata:
				math1 += 1
				f.write(str(i) + " has been uploded, with date and time: " + str(time.strftime('%X %x %Z'))+'\n')
		if(math1 == 0):
			f.write("No New Update " + str(time.strftime('%X %x %Z')) + '\n')
		mathdata = math
			

		print "---------------------------------" 
			
		#Scraping for Chemistry Assignments
		page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=918')
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		chem = []
		for link in soup.findAll('td',{'class': 'cell c1'}):
			title = link.string
			chem.append(title)
		chem1 = 0
		f.write("\nChemistry Assignment --------------------------------------------------------------------\n")
		for i in chem:
			if i not in chemdata:
				chem1 += 1
				f.write(str(i) + " has been uploded, with date and time: " + str(time.strftime('%X %x %Z'))+'\n')
		if(chem1 == 0):
			f.write("No New Update " + str(time.strftime('%X %x %Z')) +"\n")
		chemdata = chem



		print "---------------------------------" 
		
		#Scraping for Economics Assignments
		page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=918')
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		eco = []
		for link in soup.findAll('td',{'class': 'cell c1'}):
			title = link.string
			chem.append(title)
		eco1 = 0
		f.write("\nEconomics Assignment --------------------------------------------------------------------\n")
		for i in eco:
			if i not in ecodata:
				eco1 += 1
				f.write(str(i) + " has been uploded, with date and time: " + str(time.strftime('%X %x %Z'))+'\n')
		if(eco1 == 0):
			f.write("No New Update " + str(time.strftime('%X %x %Z')) +"\n")
		ecodata = eco




		
		print "---------------------------------"

		#Scraping for Englisg Assignments
		page = c.get('https://lms.iiitb.ac.in/moodle/mod/assign/index.php?id=922')
		plain_text = page.text
		soup = BeautifulSoup(plain_text, "lxml")
		eng = []
		for link in soup.findAll('td',{'class': 'cell c1'}):
			title = link.string
			eng.append(title)
		eng1 = 0
		f.write("\nEnglish Assignment --------------------------------------------------------------------\n")
		for i in eng:
			if i not in engdata:
				eng1 += 1
				f.write('\n' + str(i) + " has been uploded, with date and time: " + str(time.strftime('%X %x %Z'))+'\n')
		if(eng1 == 0):
			f.write("No New Update " + str(time.strftime('%X %x %Z'))+"\n")
		engdata = eng
		f.close()


	print ""	
	time.sleep(3600)


	
	









			

		







