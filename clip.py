# -*- coding: utf-8 -*-
import os, re
from time import sleep

run_every_seconds=1
regex=r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(([‌ ^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))"""

def hosted_url_finder(raw):
    urls = []
    for i in raw.split('\n'):
        url_matches = re.findall(regex, i, re.DOTALL)
        if url_matches:
            url = url_matches[0][0]
            urls.push(url)
    return urls
                       



while True:
    sleep(run_every_seconds)
    s = os.popen('xsel').read()
    urls = hosted_url_finder(s)
    if urls:
        

