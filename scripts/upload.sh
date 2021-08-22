if [ -d dist ]; then
    pip install --upgrade -qqq twine
    python3 -m twine upload dist/*
fi
