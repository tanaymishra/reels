import argparse
import os
from reels import download, make_name


def main():
    parser = argparse.ArgumentParser(description='download instagram reels')
    parser.add_argument('url', nargs='?')
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--folder', default='.')
    args = parser.parse_args()
    if args.url:
        name = args.output or make_name(args.url)
        download(args.url, os.path.join(args.folder, name))


if __name__ == '__main__':
    main()
