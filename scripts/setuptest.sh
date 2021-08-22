if [ -d test/venv ]; then rmdir -r -f test/venv; fi

python -m venv test/venv
test/venv/bin/activate
pip install --upgrade lastfmget
deactivate
