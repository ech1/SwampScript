
#get python3 on your windows machine (use microsoft store to do that)
#pip install --upgrade pip
#pip install scapy colorama psutil requests
#and you're good to go!

import psutil
import subprocess
import sys
import os
import time
from scapy.all import *
import socket
import requests
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

from colorama import init, Fore, Back
FGR = Fore.GREEN
FYE = Fore.YELLOW
FRE   = Fore.RED
FCY  = Fore.CYAN
FBL  = Fore.BLACK
FRESET = Fore.RESET

BGR = Back.GREEN
BBL = Back.BLACK
BRE   = Back.RED
BCY  = Back.CYAN
BRESET = Back.RESET

def main():
        endUP=time.time() # just in case the script starts before gmod is launched
        down=0
        interval=20 #interval to check UDP connection is 20 secs
        downUDP=0
        limit= 9 #number of udp connection tests (9x20secs) before retrying to launch gmod
        verbose=False #False for no verbose output, #True for verbose output
        #print('Your local IP is',IPAddr)
        while True:
            while(check_swampsv(verbose)):
                down=0
                if(verbose):
                    print(f"\n{BGR}[+] swampservers.net is up!{BRESET}")
                start= time.time() #start time elapsed

                while(check_udp_connection(verbose)):
                    downUDP=0
                    if(verbose):
                        print(f"\n{BGR}[+] UDP CONNECTION IS UP{BRESET}")
                    endUP=time.time() # endUP the end of the uptime, this means that this is the START of the downtime
                    secs=int(endUP-start)
                    days = secs // (24 * 3600)
                    if(secs<=interval):
                            print("")
                    print(f"{BGR}Uptime [",days,':',time.strftime("%H:%M:%S", time.gmtime(secs)),']\r', end="")
                    time.sleep(interval)
                else:
                    if(verbose):
                        print(f"\n{BRE}[+] UDP CONNECTION IS DOWN{BRESET}")
                    else:
                        if(downUDP == 0):
                            print("")
                        endDN=time.time()
                        secs=int(endDN-endUP) #to measure downtime, you start from the end of the uptime
                        if(secs<=interval):
                                print("")
                        days = secs // (24 * 3600)
                        print(f"{BRE}Downtime [",days,':',time.strftime("%H:%M:%S", time.gmtime(secs)),f"{BRE}]",downUDP,f"/",limit,f"{BRESET}",'\r', end="")
                        time.sleep(interval)
                    downUDP+=1
                    if((downUDP % limit) == 0):
                         #stop elapsed time
                        restart_gmod(verbose)
                time.sleep(interval)
            else:
                if(down == 0):
                    print("")
                down +=1
                if(verbose):
                    print(f"\n{BRE}[+] swampservers.net is down!{BRESET}")
                else:
                    endDN=time.time()
                    secs=int(endDN-endUP) #to measure downtime, you start from the end of the uptime
                    days = secs // (24 * 3600)
                    print(f"{BRE}Downtime [",days,':',time.strftime("%H:%M:%S", time.gmtime(secs)),f"{BRE}]",(down % 9),f"/",limit,f"{BRESET}",'\r', end="")
                if((down % 9) == 0):
                    kill_gmod(verbose)
                    time.sleep(interval*2)
                time.sleep(interval)

def check_swampsv(verbose):
    url='https://swamp.sv'
    if(verbose):
        print(f"\n{BCY}[+] CHECKING INTERNET{BRESET}")
    try:
            requests.get(url).status_code
            if(verbose):
                print('[+] swamp.sv online')
            return True
    except:
            if(verbose):
                print('[+] swamp.sv offline')
            return False





def check_udp_connection(verbose):
    if(verbose):
        print(f"\n{BCY}[+] CHECKING UDP{BRESET}")
    a=sniff(timeout=5,count=10,filter="udp and host 208.103.169.51") #check the udp connection to the server
    if(len(a) <= 3):  ####IF NO UDP CONNECTION THEN
        if(verbose):
            print(f"\n{BRE}[+]",a,f"{BRESET}")
            print(a.summary())
        return False
    else: ####IF UDP CONNECTION THEN
        if(verbose):
            print(f"\n{BGR}[+]",a,f"{BRESET}")
            print(a.summary())
        return True


def kill_gmod(verbose):
    if(verbose):
        print(f"\n{BRE}[+] CLOSING GMOD{BRESET}")
    for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in ['gmod', 'steam']):
                if(verbose):
                    print(f"{BRE}[+] KILLING: {BRESET}",proc.name())
                proc.kill()
    #time.sleep(60)

def restart_gmod(verbose):
    if(verbose):
        print(f"\n{BRE}[+] RESTARTING GMOD{BRESET}")
    for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in ['gmod', 'steam']):
                if(verbose):
                    print(f"{BRE}[+] KILLING: {BRESET}",proc.name())
                proc.kill()
    subprocess.Popen(fullpath,shell=False)

if __name__ == '__main__':
    choice='0'
    steampath='C:\Program Files (x86)\Steam\steam.exe'
    #steampath='Z:\Steam\steam.exe'
    args1=' -applaunch 4000 +connect cinema.swamp.sv -windowed -w 1920 -h 1080'
    args2=''
    while(choice == '0'):
            print(f"\n{BGR}[+] Swamp Cinema Connection Script\n{BRESET}1) Active\n2) Idle\n3) Idle Minimalist\n")
            choice=input()
            if(choice == '1'):
                print('Active Selected!')
                args2=''
            elif(choice == '2'):
                print('Idle Selected!')
                args2=' -nosrgb -noaddons -nochromium'
            elif(choice == '3'):
                print('Idle Minimalist')
                args1=' -applaunch 4000 +connect cinema.swamp.sv -windowed -safe' #-safe -w 1080 -h 700
                args2=' -nosrgb -noaddons -nochromium  -windowed -novid +contimes 0 +con_notifytime 0'
            else:
                choice='0'
            fullpath=steampath+args1+args2
            fullpath.split()
            subprocess.Popen(fullpath,shell=False)
    main()
