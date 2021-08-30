if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

cd test
venv/bin/python3 test --use_src
cd ..
