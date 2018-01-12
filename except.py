import sys
import os

from colorama import init 
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
from termcolor import colored, cprint

os.system('cls' if os.name == 'nt' else 'clear')

print ""

welcome = "EXCEPT"; 

cprint(figlet_format(welcome, font='banner3', justify="center"),
       'green', attrs=['bold'])

creators = colored('Coded By At0m1cal!', 'red')
github = colored('https://github.com/rsmudge', 'red')

cprint('{:^80}'.format('\033[1m' + creators +  '\033[0m'))
cprint('{:^80}'.format('\033[1m' + github +  '\033[0m'))
