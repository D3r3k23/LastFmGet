@echo off
if "%1" == "--failfast" (
    set failfast="--failfast"
) else (
    set failfast=
)

if not exist test\venv\ call scripts\setuptest.bat

cd test

echo Running tests without cache
venv\Scripts\python test --use_src %failfast%
if NOT %errorlevel% == 0 (
    echo Tests failed without cache
    cd ..
    exit /b 1
)

echo Running tests with cache
venv\Scripts\python test --use_src %failfast% --use_cache
if NOT %errorlevel% == 0 (
    echo Tests failed with cache
    cd ..
    exit /b 1
)

echo Tests passed
cd ..
