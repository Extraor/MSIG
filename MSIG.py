import os
import sys
import urllib2
import requests
import json
import re
# import ast
from bs4 import BeautifulSoup

url = sys.argv[1]
plc = " ".join(sys.argv[2:])
if plc[:-1] == "\\":
	plc[:-1] == ""
if url == "-help":
	print(plc)
	sys.exit("""Working
		""")

def pjb(url, plc):
	soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url),timeout=0.51).read())
	a = soup.find_all("a", { "class" : "thlink" })
	crnt = 0
	for link in a:
		url = str(link.find("img").get("src"))
		url = url.replace("/bigthumbs/", "/original/")
		try:
			f = urllib2.urlopen(url)
			saveloc = str(plc) + "\\" + str(url[38:])
			print "Saving " + str(url[38:]) + " to " + str(plc) + " (" + str(crnt + 1) + " of " + str(len(a)) + ")"
			with open(saveloc, "wb") as code:
				code.write(f.read())
			crnt += 1
		except urllib2.HTTPError, err:
			if err.code == 404:
				print ("The image at " + url + " (#" + str(crnt + 1) + ")" + " no longer exists")
				continue

def reddit(url, plc):
	print("It thinks it's a reddit link")
	# soup = json.loads(urllib2.urlopen(urllib2.Request(url),timeout=0.51).read())
	# a = soup['data']['children']
	# b = str(soup['data']['after'])
	# # cnt = 1
	# # if b != "":
	# # 	url = "http://www.reddit.com" + url + ".json?count=" + str(cnt*100) + "&after=" + b 
		
	# # 	cnt +=1
	# # print b[0]
	# for i in range(0, 10):
	# 	if str(a[i]["data"]["is_self"]) == "False":
	# 		try:
	# 			url = a[i]["data"]["url"]
	# 			f = urllib2.urlopen(url)
	# 			if re.search(".html", url) != "None":
	# 				saveloc = str(plc) + str(url.rsplit('/', -1))
	# 				print saveloc
	# 			print "Saving " + str(url) + " to " + str(plc) + " (" + ")"
	# 			with open(saveloc, "wb") as code:
	# 				code.write(f.read())
	# 			# crnt += 1
	# 		except urllib2.HTTPError, err:
	# 			if err.code == 404:
	# 				continue
	# 	else:
	# 		continue

def fourchan(url, plc):
 	soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url),timeout=0.51).read())
 	a = soup.find_all("a", { "class" : "fileThumb" })
 	crnt = 0
 	for link in a:
 		url = "http:" + str(link.get("href"))
 		try:
 			f = urllib2.urlopen(url)
 			saveloc = str(plc) + "\\" + str(crnt) + str(url[30:])
 			print "Saving " + str(crnt) + str(url[30:]) + " to " + str(plc) + " (" + str(crnt + 1) + " of " + str(len(a)) + ")"
 			with open(saveloc, "wb") as code:
 				code.write(f.read())
 			crnt += 1
 		except urllib2.HTTPError, err:
 			if err.code == 404:
 				print ("The image at " + url + " (#" + str(crnt + 1) + ")" + " no longer exists")
 				continue
def execute(url, plc):
	supported = {"primejailbait" : pjb, "4chan" : fourchan, "reddit": reddit}
	hack = 1
	for i in supported:
		if bool(re.search(i, url)) == True:
			supported[i](url, plc)
			break
		else:
			hack += 1 
			continue
	if hack>(len(supported)):
		sys.exit("""Please check url, it is either an unsupported url or an invalid page.
Execute with the -help flag to see supported sites and syntax.""")
def errcheck(url, plc):
	try:
		r = requests.get(url)
		if str(r)[11:14] == str(404):
			sys.exit("Please check url, it returned a 404 error.")
	except:
		sys.exit("""Cannot connect to url.
The site is unreachable, this could mean it is undergoing heavy traffic and cannot deal with our requests,
or you simply made a typo.
Please try connecting to the page in your browser, if it succeeds, but this program does not,
try executing with -help to see supported sites and the correct syntax""")
	if os.path.isdir(plc) == False:
		print "Creating directory: " + str(plc)
		os.makedirs(plc)
		execute(url, plc)
	else:
		execute(url, plc)
errcheck(url, plc)	

