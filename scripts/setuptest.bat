@echo off

if exist testvenv\ rmdir /s /q testvenv

python -m venv testvenv
call testvenv\Scripts\activate
pip install --upgrade -qqq lastfmget
deactivate
