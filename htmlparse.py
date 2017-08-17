import requests
from BeautifulSoup import BeautifulSoup
import urllib, json
import urllib2
import time

f1 = open('ICMLURLs.txt', 'r'); f2 = open('papers.txt', 'w'); count = 1;

for line in f1:

	url = line.strip('\n'); 
	
	try:
	
		response = requests.get(url); 
		page = str(BeautifulSoup(response.content));
		strparts = page.split('@InProceedings{'); title = strparts[1].split('title =');
		print url;
	
		papertitle = title[1].split('author =')[0].split(',')[0].strip().strip('} ').strip(' {');
		authors = title[1].split('author =')[1].split('booktitle =')[0].split(',')[0].strip().strip('} ').strip(' {');
		abstract = strparts[1].split('abstract =')[1].split('}\n}')[0];
		abstract = abstract.strip().strip(' {')
		
		f2.write('Paper Number: '+str(count)+'\n');		
		f2.write('Title: '+papertitle+'\n');
		f2.write('Authors: '+authors+'\n');	
		f2.write('Abstract: '+abstract+'\n');	
		f2.write('URL: '+url+'\n');		
		f2.write('**************************************************'+'\n');
	
		time.sleep(0.25); count = count + 1;

	except ValueError:		
		continue
	
f1.close(); f2.close()
