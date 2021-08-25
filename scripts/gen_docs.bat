@echo off

pip install --upgrade --disable-pip-version-check -qqq pdoc

python -m pdoc -t docs\templates -o docs\pdoc ^
  src\lastfmget\core.py        ^
  src\lastfmget\methods.py     ^
  src\lastfmget\raw_methods.py ^
  src\lastfmget\errors.py
