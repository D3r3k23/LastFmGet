if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg_fn',  default='test/api_cfg.yaml')
    parser.add_argument('--use_src', action='store_true')
    args = parser.parse_args()

    if args.use_src:
        # Add src to Python path to use current lastfmget source code
        # Otherwise lastfmget should be installed with pip
        import sys
        sys.path.append('src')

    import tests
    tests.run(args.cfg_fn)
