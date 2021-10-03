@echo off

if exist dist\ (
    python -m twine upload dist/*
)
