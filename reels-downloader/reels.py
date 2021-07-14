def download(url,params):
    import requests
    import re
    from requests_html import HTMLSession
    try:
        params=str(params)
        verify=re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",url)
    except:
        return ValueError("Invalid params!")
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
        # print(response)
        import requests
        r = requests.get('https://scontent-bom1-1.cdninstagram.com/v/'+final, stream=True)
        with open(params, "wb") as f:
            for c in r.iter_content(chunk_size=1024 * 1024):
                if c:
                    f.write(c)
                    if __name__ == '__main__':
                        print("Done")


    except requests.exceptions.RequestException as e:
        raise str(e)
if __name__ == '__main__':
    download('https://www.instagram.com/p/CK1uKLVJMkC/?utm_source=ig_web_copy_link','video.mp4')
