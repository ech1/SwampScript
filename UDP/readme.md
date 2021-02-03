# UDP Version
```
Warning, this version requires admin privileges, however this is a much more efficient approach
because you are checking the UDP connection to the server instead of just the process.

If anything happens to the connection itself, you will be reconnected.
If you loose your connection to internet, the script will just wait until it goes back on.

The script uses pktmon, which is a built-in windows 10 utility that can check the udp packets,
And it requires admin privileges to be executed.
``` 


# Installation

If you want to make this script run at startup, we cannot use the usual method of just putting it in shell:startup 
because this is not going to launch it as Administrator (for it to be able to check the udp packets)

Therefore, there is this method:
```
WIN+R
taskschd.msc 
click 'Task Scheduler Library' then click 'New Folder'
name it swampscript
go into it, and then click 'create task'

Name : swampscript
tick 'run with highest privileges'
configure for: Windows 10

click the 'Triggers' tab
click 'New'
Begin the task: 'At logon'
click 'ok'

click the 'Actions' tab
click 'New'
click 'Browse'
and then find the path to swamp.bat
for example: C:\Users\ech06\Desktop\SwampScript-main\UDP\swamp.bat
then click 'ok'

click the 'Settings' tab
Tick 'if the task fails, restart every : 1 minute, restart 3 times
then click 'ok'

Reboot to Check if the script is launched with elevevated privileges
```

# Disclaimer

Do not use this script if your internet connection isn't stable enough,
This is a script to be used if you have a continuous internet connection with as few 
downtimes as possible. Ideally, your connection never fails, and you will never need to be reconnected, if there is a downtime, the script will know it and will attempt a reconnection. Do not use this script if your internet connection switches on and off for extended periods of time every hours
