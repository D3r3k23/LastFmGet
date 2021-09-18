cd test

echo Running tests without cache
venv/bin/python3 test --use_src
ret_code=$?

if [ $ret_code -eq 0 ]; then
    echo Running tets with cache
    venv/bin/python3 test --use_src --use_cache
    ret_code=$?
fi

cd ..
exit $ret_code
