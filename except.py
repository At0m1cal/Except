import sys
import os
import pip
import subprocess
import time

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from termcolor import colored, cprint

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print ""

    welcome = "EXCEPT"; 

    cprint(figlet_format(welcome, font='banner3', justify="center"),
           'green', attrs=['bold'])

    creators = colored('Coded By At0m1cal!', 'red')
    github = colored('https://github.com/At0m1cal \n', 'red')

    cprint('{:^80}'.format('\033[1m' + creators +  '\033[0m'))
    cprint('{:^80}'.format('\033[1m' + github +  '\033[0m'))


    print(colored('\033[1m' + '1. Hash Cracker' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '2. Comming Soon.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '3. Comming Soon.' +  '\033[0m', 'green'))
    print(colored('\033[1m' + '4. Comming Soon' +  '\033[0m', 'green'))
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
	if os.name=='nt':
		subprocess.check_call(["modules/update.bat"]) 
		time.sleep(15)
		subprocess.check_call(["python2.7", "modules/hashcracker.py"]) 
	else:
		pass
    elif choice=="2": 
	raw_input(colored('\033[1m' + 'Error Comming Soon!' +  '\033[0m', 'red'))
    elif choice=="3":
	raw_input(colored('\033[1m' + 'Error Comming Soon!' +  '\033[0m', 'red'))
    elif choice=="4":
	raw_input(colored('\033[1m' + 'Error Comming Soon!' +  '\033[0m', 'red'))
    elif choice=="5":
		print(colored('\033[1m' + 'Thank You For Usinig Except' +  '\033[0m', 'green'))
		time.sleep(5)
		os.system('cls' if os.name == 'nt' else 'clear')
		quit()
		loop=False
    else:
		raw_input(colored('\033[1m' + 'Error wrong input selection. Press any key to try again!' +  '\033[0m', 'red'))
		os.system('cls' if os.name == 'nt' else 'clear')
