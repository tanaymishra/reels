import argparse
import os
from reels import download, download_retry, make_name, download_from_file, valid_url


def main():
    parser = argparse.ArgumentParser(description='download instagram reels')
    parser.add_argument('url', nargs='?')
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--folder', default='.')
    parser.add_argument('-l', '--list')
    parser.add_argument('-r', '--retry', action='store_true')
    parser.add_argument('--version', action='version', version='reels 1.0')
    args = parser.parse_args()
    if args.list:
        download_from_file(args.list, args.folder)
    elif args.url:
        if not valid_url(args.url):
            print('warning: does not look like a reel url')
        name = args.output or make_name(args.url)
        dest = os.path.join(args.folder, name)
        runner = download_retry if args.retry else download
        saved = runner(args.url, dest)
        print('saved ' + str(saved))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
