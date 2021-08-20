@echo off

if not exists venv (
    call scripts\setuptest.bat
)

venv\Scripts\python test\tests.py
