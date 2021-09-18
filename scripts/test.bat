@echo off

if not exist test\venv\ call scripts\setuptest.bat

cd test

echo Running tests without cache
venv\Scripts\python test --use_src
set ret_code=%errorlevel%

if %ret_code% EQU 0 (
    echo Running tests with cache
    venv\Scripts\python test --use_src --use_cache
    set ret_code=%errorlevel%
)

cd ..
exit /b %ret_code%
