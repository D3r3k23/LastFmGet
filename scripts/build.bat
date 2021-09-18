@echo off

if NOT "%1" == "-notest" (
    call scripts\test.bat
    set ret_code=%errorlevel%
    if %ret_code% neq 0 (
        echo Error: tests failed
        exit /b %ret_code%
    )
)

call scripts\gen_docs.bat

if exist dist\ rmdir /s /q dist\

pip install --upgrade --disable-pip-version-check -qqq build
python -m build
