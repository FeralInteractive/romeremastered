@echo off
.\xidx.exe -csf skeletons.idx < list.txt

python skelconverter.py
if errorlevel 1 goto :pythonerror

goto :caseyes


:caseyes

echo Renaming skeletons_new.idx to skeletons.idx

IF EXIST "skeletons.idx" del skeletons.idx
ren skeletons_new.idx skeletons.idx
echo Done!

echo Renaming skeletons_new.dat to skeletons.dat
IF EXIST "skeletons.dat" del skeletons.dat
ren skeletons_new.dat skeletons.dat
echo Done!
pause
exit

:caseno

exit

:pythonerror

pause
exit