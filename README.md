# SwampScript
A script that is being used to connect to swamp's servers
```
The minimum duration is set to 12 hours so that it does not reconnect you and get considered as anti afking.
If you change the value to be under 720 minutes, don't be suprised if console detects it.
```

#How to install it
First enable powershell scripts:
```
WIN + X
Run powershell as admin
set-executionpolicy remotesigned
then hit A to say yes to all
```
Then clone the repo somewhere (you can use github desktop for that or something else)
Then make sure you have gmod running on the chromium branch, because my script checks for gmod.exe and not something else
if gmod isn't on the correct branch, it won't be named gmod.exe and console will most likely pick this up as anti afking because you're being reconnected every minute.
So make sure gmod is actually called gmod.exe when you run it (Chromium Branch), then proceed:

Basically the file swamp.bat is used to call the other powershell scripts,
you can double click it and it will open up (just type 1 2 or 3 depending on what you want to do with gmod)
It will automatically reconnect you every 12 hours or if the game crashes

