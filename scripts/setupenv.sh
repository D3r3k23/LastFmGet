cfg_fn=test/api_cfg.yaml
api_url=http://ws.audioscrobbler.com/2.0/
user_agent=D3r3k23
use_cache=false
call_rate=5

pip install --disable-pip-version-check -qqq pyyaml
python3 scripts/gen_api_cfg_yaml.py $cfg_fn $api_url $TEST_API_KEY $user_agent $use_cache $call_rate

scripts/setuptest.sh
