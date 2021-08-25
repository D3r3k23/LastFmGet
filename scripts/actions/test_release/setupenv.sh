cfg_fn=test/api_cfg.yaml
api_url=http://ws.audioscrobbler.com/2.0/
user_agent=D3r3k23
call_rate=5
enable_cache=false

pip install --disable-pip-version-check -qqq pyyaml
python3 scripts/gen_api_cfg_yaml.py $cfg_fn $api_url $TEST_API_KEY $user_agent 5 $enable_cache

pip install --upgrade --disable-pip-version-check -q lastfmget
