mkdir test/cfg
cfg_fn_no_cache=test/cfg/api_cfg_no_cache.yaml
cfg_fn_with_cache=test/cfg/api_cfg_with_cache.yaml
api_url=http://ws.audioscrobbler.com/2.0/
user_agent=LastFmGet
call_rate=5
enable_cache=false

pip install --disable-pip-version-check -qqq pyyaml
python3 scripts/gen_api_cfg_yaml.py $cfg_fn_no_cache   $api_url $TEST_API_KEY $user_agent $call_rate $enable_cache
python3 scripts/gen_api_cfg_yaml.py $cfg_fn_with_cache $api_url $TEST_API_KEY $user_agent $call_rate $enable_cache
