import re
import requests
from requests_html import HTMLSession


def download(url, params):
    """Download an Instagram reel from url and save it to the given path."""
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
        r = requests.get('https://scontent-bom1-1.cdninstagram.com/v/'+final, stream=True)
        with open(params, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    if __name__ == '__main__':
                        print("Done")


    except requests.exceptions.RequestException as e:
        raise RuntimeError(str(e))
def shortcode(url):
    if '/p/' not in url:
        return None
    return url.split('/p/')[1].split('/')[0]


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


def download_many(urls, folder='.'):
    import os
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    saved = []
    for u in urls:
        path = os.path.join(folder, clean_name(make_name(u)))
        download(u, path)
        saved.append(path)
    return saved


if __name__ == '__main__':
    download('https://www.instagram.com/p/CK1uKLVJMkC/?utm_source=ig_web_copy_link','video.mp4')
