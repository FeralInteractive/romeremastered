@echo off

python rsdpacker.py
if errorlevel 1 goto :pythonerror

goto :caseyes


:caseyes

echo.
echo Repack Done!
pause
exit

:caseno

exit

:pythonerror

pause
exit