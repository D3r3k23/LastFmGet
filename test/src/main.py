import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg_fn',  '-cfg', default='test/api_cfg.yaml')
    parser.add_argument('--use_src', '-src', action='store_true')
    args = parser.parse_args()
    
    if args.use_src:
        # Add src dir to Python path to use local lastfmget source code
        # Otherwise lastfmget should be installed with pip
        add_src_to_path()

    from Tests import Tests # Import after potentially adding src dir to path
    Tests.run(args.cfg_fn)

def add_src_to_path():
    sys.path.append('src')
    
if __name__ == '__main__':
    main()
