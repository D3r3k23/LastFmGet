if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

test/venv/bin/python3 test/src/main.py --use_src
