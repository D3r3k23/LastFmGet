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
python3 test --failfast
if [ $? -ne 0 ]; then
    echo Tests failed without cache
    cd ..
    exit 1
fi

echo Running tests with cache
python3 test --failtest --use_cache
if [ $? -ne 0 ]; then
    echo Tests failed with cache
    cd ..
    exit 1
fi

cd ..
echo Tests passed
