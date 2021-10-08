#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

print ("""                               
____        _                     
/ ___| _   _| |__   ___ __ _ _ __  
\___ \| | | | '_ \ / __/ _` | '_ \ 
 ___) | |_| | |_) | (_| (_| | | | |
|____/ \__,_|_.__/ \___\__,_|_| |_|
""")

domain = input("[+] Input domain target : ")
print ("[+] Sabar sayang lagi proses ... \n")

def main(domain):
	url = "https://sonar.omnisint.io/subdomains/{}".format(domain)
	data = requests.get(url).json()
	print ("[+] cuman dapet segini sayang : \n")
	for i in data:
		print(i)
		open('Result.txt','a').write(str(i) + '\n')

if __name__ == '__main__':
	main(domain)