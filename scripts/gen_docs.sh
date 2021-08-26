pip install --upgrade --disable-pip-version-check -qqq pdoc

python3 -m pdoc -t docs/templates -o docs/pdoc src/lastfmget

rm docs/pdoc/index.html
