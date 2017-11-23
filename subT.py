#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import os, platform
import time

so = platform.system()

if  so == 'Windows':
	os.system("cls")


else:
	os.system("clear")

print '''
 _____ ____   ___   ____ ___ _____ _______   __  ____  ____  
|  ___/ ___| / _ \ / ___|_ _| ____|_   _\ \ / / | __ )|  _ \ 
| |_  \___ \| | | | |    | ||  _|   | |  \ V /  |  _ \| |_) | 
|  _|  ___) | |_| | |___ | || |___  | |   | |   | |_) |  _ <   
|_|   |____/ \___/ \____|___|_____| |_|   |_|   |____/|_| \_\ 


By: Predin Bastos e Derick Elliot.

'''


def brute():
	wordlist = 'wordlist.txt'
	f = open(wordlist)
	lines = []

	for line in f.readlines():
		lines.append(str(line.replace("\n","")))
	return lines

wordlist = brute()

site  = raw_input("Insira o nome do site (exemplo: facebook.com)\n~> ")

for subdomain in wordlist:

	req = urllib2.Request('http://'+subdomain+'.'+site, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8'})
	
	try:
		resp = urllib2.urlopen(req)

	except urllib2.HTTPError as e:
		if e.code == 404:
			print subdomain + "." + site + "- > NOT FOUND"

	except urllib2.URLError as e:
		print subdomain + "." + site + "- > NOT FOUND"

	else:
		print subdomain + "." + site + "- > OK"
		save = open('result.txt', 'a')
		save.write(subdomain + "." + site + "\n")

	time.sleep(1)
