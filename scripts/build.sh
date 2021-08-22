if [ -d dist ]; then rm -r -f dist; fi

pip install --upgrade -qqq build
python3 -m build
