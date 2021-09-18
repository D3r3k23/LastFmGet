if [ "$1" == "-src" ]; then
    use_src="--use_src"
elif [ "$1" == "-release" ]; then
    use_src=""
else
    echo Error: Choose either src or release
    exit 1
fi

cd test

echo Running tests without cache
python3 test $use_src
ret_code=$?

if [ $ret_code -eq 0 ]; then
    echo Running tests with cache
    python3 test $use_src --use_cache
    ret_code=$?
fi

cd ..

if [ $ret_code -eq 0 ]; then
    echo Tests passed
else
    echo Tests failed
fi
exit $ret_code
