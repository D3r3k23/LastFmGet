@echo off

if exist test\venv\ rmdir /s /q test\venv

python -m venv test\venv
call test\venv\Scripts\activate
pip install --upgrade lastfmget
deactivate
