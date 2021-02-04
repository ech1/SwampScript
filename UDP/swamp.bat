@ECHO OFF

GOTO :A
:A
PowerShell.exe -Command "%~dp0\swamp.ps1" 
timeout 60
GOTO :A
