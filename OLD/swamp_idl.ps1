echo ''
echo '[+] IDLE MODE STARTING'
$counter=0

while(1){
	
	$steam = Get-Process steam -ErrorAction SilentlyContinue
	$gmod = Get-Process gmod -ErrorAction SilentlyContinue
	if(!$gmod){
			echo ''
			echo '[+] GMOD IS CLOSED ! RESTARTING'
			$steampath='C:\Program Files (x86)\Steam\Steam.exe'
			$args='-applaunch 4000 -w 1920 -h 1080 +connect cinema.swampservers.net:27015 -noaddons -nosrgb -nochromium -noborder -low -heapsize 1048576 -forcenovsync -hushasserts -noipx -nops2b -novid -nocdaudio -hijack -flushlog +r_hunkalloclightmaps 0 -mat_showlowresimage -processheap'
			#& "$steampath" $args
			Start-Process -FilePath "$steampath" -ArgumentList "$args"
			$counter=0
	}

	$counter=$counter+1
	echo ''
	echo "[+] Time is $counter limit is 720 minutes"
	timeout 60
	
	if (($gmod) -and ($counter -gt 720)) { #12 hours, under that it can be considered anti afking
		# try gracefully first
		$gmod.CloseMainWindow()
		$steam.CloseMainWindow()
		# kill after five seconds
		timeout 5
		if (!$steam.HasExited) {
			$gmod | Stop-Process -Force
			$steam | Stop-Process -Force
		}
		$counter=0
	}
	Remove-Variable steam
	
}
	