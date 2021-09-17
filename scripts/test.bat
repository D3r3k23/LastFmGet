@echo off

if not exist test\venv\ call scripts\setuptest.bat

cd test
venv\Scripts\python test --use_src
set retcode=%errorlevel%
cd ..
exit /b retcode
