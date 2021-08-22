if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

test/venv/bin/python3 test/src/tests.py
