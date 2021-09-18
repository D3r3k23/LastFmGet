if [ "$1" != "-notest" ]; then
    scripts/test.sh
    ret_code=$?
    if [ $ret_code -ne 0 ]; then
        echo Error: tests failed
        exit $ret_code
    fi
fi

scripts/gen_docs.sh

if [ -d dist ]; then rm -rf dist; fi

pip install --upgrade --disable-pip-version-check -qqq build
python3 -m build
