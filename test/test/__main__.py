import argparse
import sys
import os.path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--use_src',   action='store_true')
    parser.add_argument('--use_cache', action='store_true')
    parser.add_argument('--failfast',  action='store_true')
    args = parser.parse_args()

    if args.use_src:
        # Add src dir to Python path to use local lastfmget source code
        # Otherwise lastfmget should be installed with pip
        add_src_to_path()

    # Import after potentially adding src dir to path
    import tests

    if args.use_cache:
        cfg_fn = 'cfg/api_cfg_with_cache.yaml'
    else:
        cfg_fn = 'cfg/api_cfg_no_cache.yaml'

    passed = tests.run(cfg_fn, args.failfast)
    return 0 if passed else 1

def add_src_to_path():
    sys.path.append(os.path.join('..', 'src'))

if __name__ == '__main__':
    sys.exit(main())
