import StringIO
import getopt
import hashlib
import sys
import os
import time

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from termcolor import colored, cprint

myHash = ""
hashType = ""
wordlistFile = ""

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print ""

    welcome = "EXCEPT"; 

    cprint(figlet_format(welcome, font='banner3', justify="center"),
           'green', attrs=['bold'])

    creators = colored('Coded By At0m1cal!', 'red')
    github = colored('https://github.com/At0m1cal', 'red')
    name = colored('Hash Cracker \n', 'red')

    cprint('{:^80}'.format('\033[1m' + creators +  '\033[0m'))
    cprint('{:^80}'.format('\033[1m' + github +  '\033[0m'))
    cprint('{:^80}'.format('\033[1m' + name +  '\033[0m'))

    print(colored('\033[1m' + '1. Define Hash.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '2. Define Hash Type.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '3. Define Wordlist.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '4. Start.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '5. Exit.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + 70 * "-" +  '\033[0m', 'red'))

loop=True

while loop:
    menu()
    choice = input(colored('\033[1m' + 'Enter your choice [1-5]:' +  '\033[0m', 'green'))

    if choice==1:
	myHash = raw_input(colored('\033[1m' + 'Enter Your Hash:' + '\033[0m', 'red'))
    elif choice==2:
	print(colored('\033[1m' + 'What Is Your Has Type? \n md5, sha1, sha224, sha256, sha384, sha512' + '\033[0m', 'red'))
	myChoice = raw_input(colored('\033[1m' + 'What Is Your Hash Type? ' + '\033[0m', 'red'))
	
	if myChoice=="md5":
		hashType = "md5"
	elif myChoice=="sha1":
		hashType = "sha1"
	elif myChoice=="sha224":
		hashType = "sha224"
	elif myChoice=="sha256":
		hashType = "sha256"
	elif myChoice=="sha384":
		hashType = "sha384"
	elif myChoice=="sha512":
		hashType = "sha512"
	else:
		raw_input(colored('\033[1m' + 'Error wrong input selection. Press any key to try again!' +  '\033[0m', 'red'))
    elif choice==3:
	wordlistFile = raw_input(colored('\033[1m' + 'Please Enter The Location Of Your Wordlist! ' +  '\033[0m', 'red'))
    elif choice==4:
	if myHash=="":
		raw_input(colored('\033[1m' + 'Error You Must Enter A Hash To Crack' +  '\033[0m', 'red'))
	elif hashType=="":
		raw_input(colored('\033[1m' + 'Error You Must Enter A Hash Type' +  '\033[0m', 'red'))
	elif wordlistFile=="":
		raw_input(colored('\033[1m' + 'Error You Must Enter A location Of Your Wordlist' +  '\033[0m', 'red'))
	else:
		if hashType=="md5":
			m = hashlib.md5()
		else:
			print("error not supported")
		
		wordlist = open(wordlistFile, "r")

		hash = myHash

		pass
		for line in wordlist:
			m = hashlib.md5()
			line = line.replace("\n","")
			m.update(line)
			word_hash = m.hexdigest()
			if word_hash==hash:
				print(colored('\033[1m' + "The hash you entered is [" + line +  "]" + '\033[0m', 'red'))
				raw_input()
				sys.exit()
	
		print "The hash given does not correspond to any supplied word in the wordlist."
		raw_input()
		sys.exit()
		
		
    elif choice==5:
	print(colored('\033[1m' + 'Thank You For Usinig Except' +  '\033[0m', 'green'))
	time.sleep(5)
	os.system('cls' if os.name == 'nt' else 'clear')
	quit()
	loop=False	
    else:
	raw_input(colored('\033[1m' + 'Error wrong input selection. Press any key to try again!' +  '\033[0m', 'red'))
	os.system('cls' if os.name == 'nt' else 'clear')
