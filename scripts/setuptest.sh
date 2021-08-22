if [ -d test/venv ]; then rm -r -f test/venv; fi

python3 -m venv test/venv
source test/venv/bin/activate
pip install --upgrade --disable-pip-version-check -q lastfmget
deactivate
