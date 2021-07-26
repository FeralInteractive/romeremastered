@echo off
set "PATH="

for /f %%f in ('dir /b %PATH%\*.cas') do casconv.exe -i %PATH%/%%f -f fbx"
pause
cmd /k