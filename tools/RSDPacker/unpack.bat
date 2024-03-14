@echo off

python rsdunpacker.py
if errorlevel 1 goto :pythonerror

goto :caseyes


:caseyes

echo.
echo Unpack Done!
pause
exit

:caseno

exit

:pythonerror

pause
exit