if [ -d dist ]; then
    pip install --upgrade --disable-pip-version-check -qqq twine
    python3 -m twine upload dist/*
fi
