scripts/test.sh
# scripts/gen_docs.sh

if [ -d dist ]; then rm -r -f dist; fi

pip install --upgrade --disable-pip-version-check -qqq build
python3 -m build
