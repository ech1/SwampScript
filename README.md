# SwampScript
A script that is being used to connect to swamp's servers
```
The minimum duration is set to 12 hours so that it does 
not reconnect you and get considered as anti afking.
If you change the value to be under 720 minutes, 
don't be suprised if console detects it.
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
```So make sure gmod is actually called gmod.exe when you run it (Chromium Branch)
Steam > library > right click gnod > properties > Betas > x86-64 - Chromium + 64bit binaries
```

Basically the file swamp.bat is used to call the other powershell scripts,
you can double click it and it will open up (just type 1 2 or 3 depending on what you want to do with gmod)
It will automatically reconnect you every 12 hours or if the game crashes
If you want to run that swamp.bat at each startup, do the following:
```
create a shortcut of swamp.bat
WIN+R
shell:startup
put the shortcut to swamp.bat in here
```
By default, the script assume that:
```
-Steam is installed at the default location ( C:\Program Files (x86)\Steam\Steam.exe )
-that you have a 1920x1080 screen
-that you are running gmod on the chromium branch
```
if any of those conditions are not there, make sure to tweak the .ps1 scripts to your liking. Keep in mind that if it does not work properly, console might pick it up as anti afking, so make sure that you test the script properly before letting it run for hours on end. IF you have any questions just send them over on discord / telegram / steam so i can answer them.
