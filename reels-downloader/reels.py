import os
import re
import requests
from requests_html import HTMLSession

HEADERS = {'User-Agent': 'Mozilla/5.0'}


def download(url, params):
    try:
        params=str(params)
        verify=re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",url)
    except Exception:
        raise ValueError("Invalid params!")
    if __name__ == '__main__':
        print(verify)
    if verify[0][0]==url:
        pass
    else:
        raise ValueError("Wrong url Supplied")
    try:

        session = HTMLSession()
        response = session.get(url).text
        final= re.findall(r'content="https://scontent-bom1-1.cdninstagram.com/v/(.*?)[\"\']',response)[-1]
        print('https://scontent-bom1-1.cdninstagram.com/v/'+final)
        r = requests.get('https://scontent-bom1-1.cdninstagram.com/v/'+final, stream=True, headers=HEADERS, timeout=30)
        total = 0
        tmp = params + '.part'
        with open(tmp, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    total += len(chunk)
                    if __name__ == '__main__':
                        print("Done")
        os.replace(tmp, params)
        print('got ' + str(total) + ' bytes')
        return params
    except requests.exceptions.RequestException as e:
        raise RuntimeError(str(e))
def shortcode(url):
    if '/p/' not in url:
        return None
    return url.split('/p/')[1].split('/')[0]


def valid_url(url):
    return 'instagram.com' in url and '/p/' in url


def make_name(url):
    code = shortcode(url)
    if code:
        return code + '.mp4'
    return 'video.mp4'


def clean_name(name):
    bad = '<>:"/\\|?*'
    for ch in bad:
        name = name.replace(ch, '_')
    return name


def download_many(urls, folder='.', skip=True):
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    saved = []
    total = len(urls)
    for i, u in enumerate(urls, 1):
        print('[' + str(i) + '/' + str(total) + ']')
        path = os.path.join(folder, clean_name(make_name(u)))
        if skip and os.path.exists(path):
            print('already have ' + path)
            saved.append(path)
            continue
        download(u, path)
        saved.append(path)
    return saved


def download_from_file(path, folder='.'):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path) as f:
        urls = [line.strip() for line in f if line.strip()]
    print('found ' + str(len(urls)) + ' urls')
    return download_many(urls, folder)


def download_retry(url, params, tries=3):
    last = None
    for i in range(tries):
        try:
            return download(url, params)
        except Exception as e:
            last = e
            print('retry ' + str(i + 1))
    raise last


if __name__ == '__main__':
    download('https://www.instagram.com/p/CK1uKLVJMkC/?utm_source=ig_web_copy_link','video.mp4')
