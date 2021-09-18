cd test
python3 test
retcode=$?
cd ..
exit $retcode
cd test

echo Running tests without cache
venv/bin/python3 test
ret_code=$?

if [ $ret_code -eq 0 ]; then
    echo Running tets with cache
    venv/bin/python3 test --use_cache
    ret_code=$?
fi

cd ..
exit $ret_code