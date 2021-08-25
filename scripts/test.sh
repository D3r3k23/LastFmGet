if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

test/venv/bin/python3 test/src/run.py --use_src
