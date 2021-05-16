
#get python3 on your windows machine (use microsoft store to do that)
#pip install --upgrade pip
#pip install scapy
#pip install colorama
#pip install psutil
#and you're good to go!

import psutil
import subprocess
import sys
import os
import time
from scapy.all import *
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

from colorama import init, Fore, Back
FGR = Fore.GREEN
#FYE = Fore.YELLOW
FRE   = Fore.RED
FCY  = Fore.CYAN
#FBL  = Fore.BLACK
FRESET = Fore.RESET

BGR = Back.GREEN
#BYE = Back.YELLOW
BBL = Back.BLACK
BRE   = Back.RED
BCY  = Back.CYAN
BRESET = Back.RESET



def main():
        down=0
        downUDP=0
        print('Your local IP is',IPAddr)
        #a=sniff(store=0,count=10,filter="udp and host 208.103.169.51",prn=lambda x: x.sprintf("%IP.src% -> %IP.dst%"))
        while True:
            while(check_swampservers()):
                down=0
                print(f"\n{BGR}[+] swampservers.net is up!{BRESET}")
                #time.sleep(60)
                if(check_udp_connection()):
                    downUDP=0
                    print(f"\n{BGR}[+] UDP CONNECTION IS UP{BRESET}")
                else:
                    print(f"\n{BRE}[+] UDP CONNECTION IS DOWN{BRESET}")
                    #args1=args1.split()
                    #args2=args2.split()
                    downUDP+=1
                    #print the attempt numbers in the ELSE of that if
                    print(f"{BRE}[+]",downUDP,f"/3{BRESET}")
                    if(downUDP >= 3):
                        downUDP=0
                        restart_gmod()
                
                time.sleep(20)
            else:
                down +=1
                print(f"\n{BRE}[+] swampservers.net is down!{BRESET}")
                if(down >= 10):
                    kill_gmod()
                
#def check_gmod():
    #check the process is running
    #check the CPU usage
    #check the RAM usage
 
def kill_gmod():  
    print(f"\n{BRE}[+] RESTARTING GMOD{BRESET}")  
    for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in ['gmod', 'steam']):
                print(f"{BRE}[+] KILLING: {BRESET}",proc.name())
                proc.kill()
    time.sleep(60)
    
def restart_gmod():  
    print(f"\n{BRE}[+] RESTARTING GMOD{BRESET}")  
    #os.system('taskkill /im gmod.exe') #doesnt even work
    #os.system('taskkill /im steam.exe')
    for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in ['gmod', 'steam']):
                print(f"{BRE}[+] KILLING: {BRESET}",proc.name())
                proc.kill()
    time.sleep(3)
    subprocess.Popen(fullpath,shell=False)
    
    
def check_udp_connection():
    print(f"\n{BCY}[+] CHECKING UDP{BRESET}")  
    #check the udp connection to the server
    a=sniff(timeout=5,count=10,filter="udp and host 208.103.169.51")
    
    if(len(a) <= 3):
        print(f"\n{BRE}[+]",a,f"{BRESET}")
        print(a.summary())
        return False
    else:
        print(f"\n{BGR}[+]",a,f"{BRESET}")
        print(a.summary())
        return True
   
def check_swampservers():
    print(f"\n{BCY}[+] CHECKING INTERNET{BRESET}")  
    #example
    response = os.system("ping -n 1 swampservers.net | findstr Reply")

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    choice='0'
    steampath='C:\Program Files (x86)\Steam\steam.exe'
    #steampath='Z:\Steam\steam.exe'
    args1=' -applaunch 4000 +connect cinema.swampservers.net -windowed -noborder -w 2560 -h 1440'
    args2=''
    while(choice == '0'):
            choice=input('''
            1) Active
            2) Idle
            3) Idle2 Textmode-Like
            ''')
            if(choice == '1'):
                print('Active Selected!')
            elif(choice == '2'):
                print('Idle Selected!')
                args2=' -nosrgb -noaddons -nochromium'
            elif(choice == '3'):
                print('Idle2 Selected!')
                args1=' -applaunch 4000 +connect cinema.swampservers.net -windowed -w 1080 -h 700'
                args2=' -nosrgb -noaddons -nochromium  -windowed -novid +contimes 0 +con_notifytime 0'
            else:
                choice='0'
            fullpath=steampath+args1+args2
            fullpath.split()
            subprocess.Popen(fullpath,shell=False)
    main()
