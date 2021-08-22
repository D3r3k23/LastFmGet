@echo off

if exist dist\ (
    pip install --upgrade -qqq --disable-pip-version-check twine
    python -m twine upload dist/*
)
