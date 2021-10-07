import time
import http.client
import urllib.request
import requests
from urllib.error import URLError, HTTPError, ContentTooShortError
from datetime import datetime
from itertools import chain, starmap

try:
    from recruitR.library.debug import RECRUIT_HEADERS
except ImportError:
    RECRUIT_HEADERS = {
        'Host': '247sports.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-tfs-guest': 'true',
        'Connection': 'keep-alive',
        'Referer': 'https://247sports.com/',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

def download(url, num_retries=5):
    try:
        html = requests.get(url, headers=RECRUIT_HEADERS).text
    except (URLError, HTTPError, ContentTooShortError, http.client.HTTPException, http.client.IncompleteRead) as e:
        print('Download error:', url)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                time.sleep(10)
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
        if num_retries > 0:
            if e == http.client.IncompleteRead:
                time.sleep(10)
                return download(url, num_retries - 1)
    return html