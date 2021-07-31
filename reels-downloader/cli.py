import argparse
from reels import download, make_name


def main():
    parser = argparse.ArgumentParser(description='download instagram reels')
    parser.add_argument('url', nargs='?')
    args = parser.parse_args()
    if args.url:
        download(args.url, make_name(args.url))


if __name__ == '__main__':
    main()
