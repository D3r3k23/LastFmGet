@echo off

if exist test\venv\ rmdir /s /q test\venv\
pip install --upgrade pip
python -m venv test\venv
call test\venv\Scripts\activate
pip install --upgrade lastfmget
deactivate
