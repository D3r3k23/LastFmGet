if [[ ! -d venv/test/venv ]; then scripts/setuptest.bat; fi

test/venv/bin/python test/tests.py
