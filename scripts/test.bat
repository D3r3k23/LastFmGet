@echo off

if not exist test\venv\ call scripts\setuptest.bat

test\venv\Scripts\python test\src\main.py --use_src
