import argparse
import os
from reels import download, make_name, download_from_file


def main():
    parser = argparse.ArgumentParser(description='download instagram reels')
    parser.add_argument('url', nargs='?')
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--folder', default='.')
    parser.add_argument('-l', '--list')
    args = parser.parse_args()
    if args.list:
        download_from_file(args.list, args.folder)
    elif args.url:
        name = args.output or make_name(args.url)
        download(args.url, os.path.join(args.folder, name))


if __name__ == '__main__':
    main()
