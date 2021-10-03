@echo off

if NOT "%1" == "--notest" (
    call scripts\test.bat --failfast
    if NOT %errorlevel% == 0 exit /b 1
)

call scripts\gen_docs.bat
if NOT %errorlevel% == 0 exit /b 1

if exist dist\ rmdir /s /q dist\

python -m build
