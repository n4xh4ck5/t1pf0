#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
import re
import socket

API_KEY = "API_KEY"

def VerifyTarget(target):
	match = False

	try:

		if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', target):

			match = True #IP

		elif re.match(r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.[a-zA-Z]{2,3})$', target):

			match = False

		else:

			match = None
	except Exception as e:
		print e 

	return match

def SearchDomain(target):
	data = None
	array_subdomains = []
	url = "http://ipv4info.com/api_v1/?key="+API_KEY+"&type=SUBDOMAINS&value="+target+"&page=0"
	try:
		response = requests.get (url,allow_redirects=False, timeout=5,verify=False)
		data = json.loads(response.text)
		for subdomain in data['Subdomains']:
			print "\n\t- " + subdomain['domain']
			array_subdomains.append(subdomain['domain'])
	except Exception as e:
		print e
	return array_subdomains


### SEARCH IP ###
def SearchIP (target):
	#target is not a IP, it must be a range of IP
	data = None
	url = "http://ipv4info.com/api_v1/?key="+API_KEY+"&type=IPADDRESS&value="+target+"&page=0"
	array_domains = []
	try:
		response = requests.get (url,allow_redirects=False, timeout=5,verify=False)
		data = json.loads(response.text)
		for domain in data['Domains']:
			print "\n\t- " + domain['domain']
			array_domains.append(domain['domain'])
	except Exception as e:
		print e
	return array_domains

def ipv4info ():
	print "Enter a domain or IP?"
	target=raw_input ()
	flag = VerifyTarget(target)
	if flag == True:
		return  SearchIP(target)
	else:
		return SearchDomain(target)
""" FUNCTION BANNER """
def banner ():
	print """
             __                                                       
         ...-'  |`.                                                    
         |      |  |_________   _...._                                 
         ....   |  |\        |.'      '-.       _.._                   
     .|    -|   |  | \        .'```'.    '.   .' .._|   .-''` ''-.     
   .' |_    |   |  |  \      |       \     \  | '     .'          '.   
 .'     |...'   `--'   |     |        |    |__| |__  /              `  
'--.  .-'|         |`. |      \      /    .|__   __|'                ' 
   |  |  ` --------\ | |     |\`'-.-'   .'    | |   |         .-.    | 
   |  |   `---------'  |     | '-....-'`      | |   .        |   |   . 
   |  '.'             .'     '.               | |    .       '._.'  /  
   |   /            '-----------'             | |     '._         .'   
   `'-'                                       |_|        '-....-'`         
	                             '-....-'`                        """
	print "\n"
	print """** Tool to interact the API ipv4info - http://ipv4info.com/tools/api/
	** Version 1.0
	** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
	** Github: https://github.com/n4xh4ck5/
	** DISCLAMER This tool was developed for educational goals. 
	** The author is not responsible for using to others goals.
	** A high power, carries a high responsibility!"""

def help ():
	print  """ \nThis script interacts the API ipv4info 

			Example of usage: python t1pf0.py """

""" FUNCTION MAIN """
def main (argv):

	banner()
	#call help
	help()
	#Call Menu
	ipv4info ()

# CALL MAIN
if __name__ == "__main__":
	main(sys.argv[1:])