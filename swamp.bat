@ECHO OFF


GOTO :A

:A
echo [+] Swamp Automation Script
echo 1) Active
echo 2) Idle
echo 3) Textmode

set /p CHOICE=[+] Type the number of choice: 
echo %CHOICE%

IF "%CHOICE%"=="1" echo [+] ACTIVE MODE SELECTED   & PowerShell.exe -Command ".\swamp_act.ps1" & GOTO :A
IF "%CHOICE%"=="2" echo [+] IDLE MODE SELECTED     & PowerShell.exe -Command ".\swamp_idl.ps1" & GOTO :A
IF "%CHOICE%"=="3" echo [+] TEXTMODE SELECTED      & PowerShell.exe -Command ".\swamp_textmode.ps1" & GOTO :A
timeout 60

GOTO :A
