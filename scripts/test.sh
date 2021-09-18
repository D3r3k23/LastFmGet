if [ "$1" == "--failfast" ]; then
    failfast="--failfast"
else
    failfast=""
fi

if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

cd test

echo Running tests without cache
venv/bin/python3 test --use_src $failfast
if [ $? -ne 0 ]; then
    echo Tests failed without cache
    cd ..
    exit 1
fi

echo Running tests with cache
venv/bin/python3 test --use_src $failtest --use_cache
if [ $? -ne 0 ]; then
    echo Tests failed with cache
    cd ..
    exit 1
fi

cd ..
echo Tests passed
