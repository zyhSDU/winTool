@echo off
rd /s/q .\..\app\app1
md .\..\app\app1
cd .\..\app\app1
pyinstaller -w .\..\..\app1.py

xcopy /e .\dist\app1  .\..\app1
rd /s/q .\..\app1\build
rd /s/q .\..\app1\dist
