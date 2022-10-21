@echo off
rd /s/q .\..\app\app1
md .\..\app\app1
cd .\..\app\app1
pyinstaller -w .\..\..\app1.py
