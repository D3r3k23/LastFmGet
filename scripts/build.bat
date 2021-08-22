@echo off

if exist dist\ rmdir /s /q dist\

pip install --upgrade -qqq build
python -m build
