@echo off

if exist dist\ (
    pip install --upgrade -qqq twine
    python -m twine upload dist/*
)
