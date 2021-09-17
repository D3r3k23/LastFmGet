@echo off

call scripts\test.bat
set retcode=%errorlevel%
if %retcode% neq 0 (
    echo Error: tests failed
    exit /b %retcode%
)

call scripts\gen_docs.bat

if exist dist\ rmdir /s /q dist\

pip install --upgrade --disable-pip-version-check -qqq build
python -m build
