@echo off

call scripts\test.bat
if %errorlevel% neq 0 (
    echo Error: tests failed
    exit /b %errorlevel%
)

call scripts\gen_docs.bat

if exist dist\ rmdir /s /q dist\

pip install --upgrade --disable-pip-version-check -qqq build
python -m build
