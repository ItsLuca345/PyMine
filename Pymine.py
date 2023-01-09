import time
from time import sleep
import colorama
from colorama import Fore 
from colorama import Style
import random 
import string
print("Welcome to PyMiner")
print("")

Crypto = str(input('Choose between ETC ot BTC:'))

if Crypto == "ETH" or Crypto == "BTC":
    print("Please input Licence Key")
    sleep(0.5)

LicenseKey = input("LicenseKey: ")
if LicenseKey == "admin":
    print("Key is Valid")
else:
    print("Invalid key Tryagain!")
    exit()

if Crypto == "ETH":
    Address = str(input("Please input ETH Address:"))
    print("Checking if address is valid...")
    sleep(1)
    print("Address is Valid:)")
    sleep(1)
    print("Starting...")

elif Crypto == "BTC":
    Address = str(input("Please input BTC Address:"))
    print("Checking if address is valid...")
    sleep(1)
    print("Address is Valid:)")
    sleep(1)

    class bcolors:
        Won = '\033{92M'
        Fail = '\003{91M'

def id_gen(size = 40, chars = string.ascii_uppercase + string.digits):
    return"".join(random.choice(chars) for _ in range(size))

trys = 0
 
if Crypto == "ETH":
    colorama.init()
    while(True):
        if(trys > random.randint(150, 10000000000)):
            print(Fore.GREEN + "[-] ETH" + id_gen() + " │ Valid │ " + " 2.34562 ETH!")
            print("Transfering your ETH!")
            sleep(3)
            print("Your ETH will be transferd within the next 72 hours!")
            trys - 0
            print("Done! PyMiner Restarting!")
        else:
            print(Fore.RED + "[-] ETH" + id_gen() + " │ Invalid │ " + " 0 ETH :(")
            trys =+ 1

if Crypto == "BTC":
    colorama.init()
    while(True):
        if(trys > random.randint(150, 10000000000)):
            print(Fore.GREEN + "[-] BTC" + id_gen() + " │ Valid │ " + " 0.63242 BTC!")
            print("Transfering your BTC!")
            sleep(3)
            print("Your BTC will be transferd within the next 72 hours!")
            trys - 0
            print("Done! PyMiner Restarting!")
        else:
            print(Fore.RED + "[-] BTC" + id_gen() + " │ Invalid │ " + " 0 BTC :(")
            trys =+ 1

else:
    print("Invalid Currency please pick ETH or BTC")


