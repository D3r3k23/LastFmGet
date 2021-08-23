@echo off

scripts\test.bat

if exist dist\ rmdir /s /q dist\

pip install --upgrade --disable-pip-version-check -qqq build
python -m build
