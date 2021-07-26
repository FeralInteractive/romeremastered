@echo off
set "PATH=1942\data\animals"

for /f %%f in ('dir /b %PATH%\*.fbx') do casconv.exe -i %PATH%/%%f -f cas --ignore-textures --debug --verbose
pause
cmd /k