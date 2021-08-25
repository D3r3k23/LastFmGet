import argparse
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fn')
    parser.add_argument('api_url')
    parser.add_argument('api_key')
    parser.add_argument('user_agent')
    parser.add_argument('call_rate', type=int)
    parser.add_argument('enable_cache', type=lambda s: s.lower() == 'true')
    args = parser.parse_args()

    cfg = {
        'api_url'    : args.api_url,
        'api_key'    : args.api_key,
        'user_agent' : args.user_agent,
        'call_rate'  : args.call_rate,
        'cache': {'enable': args.enable_cache}
    }

    with open(args.fn, 'w') as f:
        yaml.dump(cfg, f, sort_keys=False)

if __name__ == '__main__':
    main()
