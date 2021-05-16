# WIN+R
# taskschd.msc 
# click 'Task Scheduler Library' then click 'New Folder'
# name it swampscript
# go into it, and then click 'create task'

# Name : swampscript
# tick 'run with highest privileges'
# configure for: Windows 10

# click the 'Triggers' tab
# click 'New'
# Begin the task: 'At logon'
# click 'ok'

# click the 'Actions' tab
# click 'New'
# click 'Browse'
# and then find the path to swamp.bat
# for example: C:\Users\ech06\Desktop\SwampScript-main\swamp.bat
# then click 'ok'

# click the 'Settings' tab
# Tick 'if the task fails, restart every : 1 minute, restart 3 times
# then click 'ok'

# Check if powershell is launched as elevevated
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if(-not $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))
{
	echo ''
    Write-Warning "Please run PowerShell as administrator"
	echo '[+] WIN+X A'
	$path=(Get-Item -Path ".\").FullName
	echo "[+] cd $path"
	echo '[+] .\UDP_sniffer.ps1'
	echo ''
    exit
		
}

$connection=0
$counter=0

echo '[+] SWAMP CINEMA CONNECTION SCRIPT'
echo '[+] 1) Active'
echo '[+] 2) Idle'
echo '[+] 3) Textmode'
$choice = Read-Host -Prompt '[+] Type the number of your choice:'

$steampath='C:\Program Files (x86)\Steam\Steam.exe'
switch ($choice) {
1 {
	echo "[+] Active"
	$args='-applaunch 4000 +connect cinema.swampservers.net:27015 -w 1920 -h 1080 -windowed -noborder -nosrgb'
	}
2 {
	echo "[+] Idle"
	$args='-applaunch 4000  +connect cinema.swampservers.net:27015  -w 1920 -h 1080 -noborder -nosrgb -noaddons -nochromium  -windowed -novid +contimes 0 +con_notifytime 0' 
	}
default {
	echo "[+] IDLE2 - TEXTMODE"
	$args='-applaunch 4000  +connect cinema.swampservers.net:27015  -w 1080 -h 700 -noborder -nosrgb -noaddons -nochromium  -windowed -novid +contimes 0 +con_notifytime 0' 
	#$args='-applaunch 4000 +connect cinema.swampservers.net:27015 -textmode -nochromium -noaddons -novid +volume 0 -nosound -noshaderapi -safe'
	}
}

#timeout 999
Start-Process -FilePath "$steampath" -ArgumentList "$args"
timeout 600 # wait 10 mins for the game to start
while(1){

$internet= Test-Connection -Computer swampservers.net -count 1 -quiet

if($internet){	
	echo '[+] Internet UP !'

	pktmon stop
	pktmon filter remove
	pktmon filter add -t UDP -i 208.103.169.51
	pktmon start --etw -s 1
	echo '[+] CHECKING UDP CONNECTIONS ... '
	timeout 10
	
	
	pktmon stop
	pktmon format PktMon.etl -o .\udp.txt 

	$LINES=(cat .\udp.txt | findstr '208.103.169.51' | Measure-Object -Line)
	
	
	if($LINES.Lines -lt 10){
		echo '[+] NOT ENOUGH UDP PACKETS !!!!'
		$connection=$connection+1
		timeout 1200
		
	}else{
		echo '[+] GOOD ENOUGH UDP PACKETS !!!!!'
		$connection=0
		timeout 1200
	}
	if($connection -gt 2){
		echo '[+] RESTART GMOD !!!'
		$connection=0
		
		$steam = Get-Process steam -ErrorAction SilentlyContinue
		$gmod = Get-Process gmod -ErrorAction SilentlyContinue
		
		$gmod | Stop-Process -Force
		$steam | Stop-Process -Force
		
		Start-Process -FilePath "$steampath" -ArgumentList "$args"
		timeout 1200
	}
}else{
	echo '[+] Internet DOWN !'
	$counter=0
	timeout 1200
}



}