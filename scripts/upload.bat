@echo off

if exist dist\ (
    pip install --upgrade --disable-pip-version-check -qqq twine
    python -m twine upload dist/*
)
