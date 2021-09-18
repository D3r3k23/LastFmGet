if [ "$1" != "-notest" ]; then
    scripts/test.sh --failfast
    if [ $? -ne 0 ]; then exit 1 fi
fi

scripts/gen_docs.sh

if [ -d dist ]; then rm -rf dist; fi

pip install --upgrade --disable-pip-version-check -qqq build
python3 -m build
