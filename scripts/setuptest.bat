@echo off

if exists venv (
    rmdir /s /q venv
)

python -m venv venv
call venv\Scripts\activate
pip install --upgrade -qqq lastfmget
deactivate
