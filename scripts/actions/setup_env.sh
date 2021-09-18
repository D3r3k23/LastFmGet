scripts/actions/gen_api_cfg_yaml.sh

if [ "$1" == "-src" ]; then
    pip install --upgrade --disable-pip-version-check -q -r requirements.txt
elif [ "$1" == "-release" ]; then
    pip install --upgrade --disable-pip-version-check -q lastfmget
else
    echo Error: Choose either src or release
    exit 1
fi
