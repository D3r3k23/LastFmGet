@echo off

pip install --upgrade --disable-pip-version-check -qqq pdoc

python -m pdoc -t docs\templates -o docs\pdoc src\lastfmget

@REM del docs\pdoc\index.html
