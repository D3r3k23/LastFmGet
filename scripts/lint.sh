pip install --disable-pip-version-check -qqq flake8
flake8 src/lastfmget test/src scripts --select=E9,F63,F7,F82 --show-source --statistics
