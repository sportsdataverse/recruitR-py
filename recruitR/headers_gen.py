import requests
import json
import datetime
import re

def headers_gen():
    today = datetime.datetime.today()
    session = requests.session()

    url = "https://247sports.com/Season/2022-Football/TransferPortal/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"}

    raw = session.get(url, headers=headers).text
    user_token = re.search('window.__INITIAL_DATA__ = {"user":{"jwt":"(.*)","roleGroup', raw).groups(1)[0]
    TFS_HEADERS = {
        'Host': 'ipa.247sports.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Access-Control-Request-Method': 'GET',
        'Access-Control-Request-Headers': 'authorization,x-tfs-guest',
        'Referer': 'https://247sports.com/',
        'Origin': 'https://247sports.com',
        'authorization': 'Bearer {}'.format(user_token),
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
    return TFS_HEADERS


