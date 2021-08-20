@echo off

if exist dist\ (
    pip install --upgrade twine
    python -m twine upload dist/*
)
