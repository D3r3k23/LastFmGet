if [ -d dist/ ]; then rmdir -r -f dist; fi

pip install --upgrade -qqq build
python -m build
