# Disclaimer
So far this python version is the most effective one, it can detect if you have an internet connection,
it can detect if the UDP connection to the server is made or not,
it will kill both gmod and steam if the UDP connection is lost,
And it will restart gmod automatically. I recommend testing it for a few hours to see if it behaves as intended. And most importantly as i've seen, it does not run out of memory space after running it for extended periods of time like powershell's badly-written-packet-sniffing-utility pktmon does.

## this is a script to use only if you have a solid internet connection, do not use it if your internet connection has alot of frequent downtimes

# Setup
-get python3 on your windows machine (you can use microsoft store to get it)

-This script uses 4 libraries, and you can get them with pip (it comes with python) from a powershell terminal
```
WIN+X  a (to launch a terminal with admin privileges)
PS> pip install --upgrade pip
PS> pip install scapy colorama psutil requests
```
and you're good to go!

```
cd C:\path\to\SwampScript\
python swamp.py
```
