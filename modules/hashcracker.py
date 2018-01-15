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

def startCrack():

    if hashType=="md5":

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

    elif hashType=="sha1":

    	wordlist = open(wordlistFile, "r")

	hash = myHash

	pass
	for line in wordlist:
		m = hashlib.sha1()
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

    elif hashType=="sha224":

    	wordlist = open(wordlistFile, "r")

	hash = myHash

	pass
	for line in wordlist:
		m = hashlib.sha224()
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
			
    else:
	print("error not supported")


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
    choice = raw_input(colored('\033[1m' + 'Enter your choice [1-5]:' +  '\033[0m', 'green'))

    if choice=="":
	raw_input(colored('\033[1m' + 'Error wrong input selection. Press any key to try again!' +  '\033[0m', 'red'))
	os.system('cls' if os.name == 'nt' else 'clear')
    elif choice=="1":
	myHash = raw_input(colored('\033[1m' + 'Enter Your Hash:' + '\033[0m', 'red'))
	print myHash
    elif choice=="2":
	
	print(colored('\033[1m' + 'What Is Your Has Type? \n[1]md5\n[2]sha1\n[3]sha224' + '\033[0m', 'red'))
	myChoice = raw_input(colored('\033[1m' + 'Enter your choice [1-5]:' +  '\033[0m', 'red'))

	if myChoice=="1":
		hashType="md5"
	elif myChoice=="2":
		hashType="sha1"
	elif myChoice=="3":
		hashType="sha224"
	else:
			raw_input(colored('\033[1m' + 'Error In Choice!' + '\033[0m', 'red'))
    elif choice=="3":
	wordlistFile = raw_input(colored('\033[1m' + 'Please Enter The Location Of Your Wordlist! ' +  '\033[0m', 'red'))
	
	if os.path.exists(wordlistFile):
		pass
	else:
		raw_input(colored('\033[1m' + 'No Wordlist Found! ' +  '\033[0m', 'red'))
		
    elif choice=="4":
	if myHash=="":
		raw_input(colored('\033[1m' + 'Error You Must Enter A Hash To Crack' +  '\033[0m', 'red'))
	elif hashType=="":
		raw_input(colored('\033[1m' + 'Error You Must Enter A Hash Type' +  '\033[0m', 'red'))
	elif wordlistFile=="":
		raw_input(colored('\033[1m' + 'Error You Must Enter A location Of Your Wordlist' +  '\033[0m', 'red'))
	else:
		loop=False
		startCrack()
		
    elif choice=="5":
	print(colored('\033[1m' + 'Thank You For Usinig Except' +  '\033[0m', 'green'))
	time.sleep(5)
	os.system('cls' if os.name == 'nt' else 'clear')
	quit()
	loop=False	
