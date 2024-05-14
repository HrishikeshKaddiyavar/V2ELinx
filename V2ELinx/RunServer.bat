@echo off
start /MIN /d "C:\Program Files\Google\Chrome\Application" chrome.exe http://127.0.0.1:8000/
py manage.py runserver