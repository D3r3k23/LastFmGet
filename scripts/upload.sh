if [ -d dist ] then
    pip install --upgrade -qqq twine
    python -m twine upload dist/*
fi
