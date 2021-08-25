@echo off

if exist test\venv\ rmdir /s /q test\venv\

python -m venv test\venv
call test\venv\Scripts\activate
pip install --upgrade --disable-pip-version-check -q -r requirements.txt
deactivate
