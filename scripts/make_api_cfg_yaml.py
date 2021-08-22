import yaml
import argparse

#key = os.environ['TEST_API_KEY']

#with open('example_api-cfg.yaml', 'r') as f:
#    cfg = yaml.safe_load(f)

#cfg['api_key'] = key

parser = argparse.ArgumentParser()
parser.add_argument('fn')
parser.add_argument('api_url')
parser.add_argument('api_key')
parser.add_argument('user_agent')
parser.add_argument('use_cache', type=lambda s: s.lower() == 'true')
parser.add_argument('call_rate', type=int)
args = parser.parse_args()
print(args.api_key)
fn = args.fn
cfg = { key: val for key, val in list(vars(args).items())[1:] }

with open(fn, 'w') as f:
    yaml.dump(cfg, f, sort_keys=False)
