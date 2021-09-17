import argparse
import sys
import os.path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg_fn',  '-cfg', default='api_cfg.yaml')
    parser.add_argument('--use_src', '-src', action='store_true')
    args = parser.parse_args()

    if args.use_src:
        # Add src dir to Python path to use local lastfmget source code
        # Otherwise lastfmget should be installed with pip
        add_src_to_path()

    import tests # Import after potentially adding src dir to path
    success = tests.run(args.cfg_fn)
    return 0 if success else 1

def add_src_to_path():
    sys.path.append(os.path.join('..', 'src'))

if __name__ == '__main__':
    sys.exit(main())
