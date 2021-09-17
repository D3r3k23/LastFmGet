scripts/test.sh
retcode=$?
if [ $retcode -ne 0 ]; then
    echo Error: tests failed
    exit $retcode
fi

scripts/gen_docs.sh

if [ -d dist ]; then rm -rf dist; fi

pip install --upgrade --disable-pip-version-check -qqq build
python3 -m build
