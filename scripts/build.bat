@echo off

if exist dist\ rmdir /s /q dist\

pip install --upgrade -qqq --disable-pip-version-check build
python -m build
