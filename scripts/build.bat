@echo off

if exist dist\ rmdir /s /q dist\

pip install --upgrade build
python -m build
