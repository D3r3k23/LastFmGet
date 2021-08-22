set -e

if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

test/venv/bin/python3 test/tests.py
