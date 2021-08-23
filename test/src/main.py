import argparse
import os.path
import sys
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg_fn',  default=os.path.join('test', 'api_cfg.yaml'))
    parser.add_argument('--use_src', action='store_true')
    args = parser.parse_args()
    
    if args.use_src:
        # Add src to Python path to use current lastfmget source code
        # Otherwise lastfmget should be installed with pip
        sys.path.append('src')

    from Tests import Tests
    Tests.run_all(args.cfg_fn)
