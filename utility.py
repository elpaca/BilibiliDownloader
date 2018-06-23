import requests
import re
import json
import hashlib
import datetime
from pyaria2 import PyAria2

BILIBILI_APP_KEY = '84956560bc028eb7'
BILIBILI_APP_SECRET = '94aba54af9065f71de72f5508f1cd42e'

RE_VIDEOINFO = re.compile(r'window.__INITIAL_STATE__=(.*);\(function\(\){var s;')

def getPostInfo(avid):
    html = requests.get('https://www.bilibili.com/video/av%s' % avid).text
    match = RE_VIDEOINFO.search(html)
    if match:
        result = json.loads(match.group(1))
        if 'code' not in result['error'].keys():
            return result

def getVideoSegmentedLinks(cid):
    params = 'appkey=%s&cid=%s&otype=json&qn=80&quality=80' % (BILIBILI_APP_KEY, cid)
    sign = hashlib.md5((params + BILIBILI_APP_SECRET).encode('utf-8')).hexdigest()
    playurl = 'https://interface.bilibili.com/v2/playurl?%s&sign=%s' % (params, sign)

    hds = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Referer': 'https://www.bilibili.com/',
        'Origin': 'https://www.bilibili.com'
    }
    result = requests.get(playurl, headers=hds).json()
    links = []
    if result['result'] == 'suee':
        for durl in result['durl']:
            current_links = []
            current_links.append(durl['url'])
            for l in durl['backup_url']:
                current_links.append(l)
            links.append(current_links)
        return links

def durationToTime(duration):
    (min, sec) = divmod(duration, 60)
    (hrs, min) = divmod(min, 60)
    return datetime.time(hour=hrs, minute=min, second=sec)

def escapeFileName(fileName):
    return re.sub('[\/:*?"<>|]', ' ', fileName)

def getAria2cClientInstance():
    return PyAria2(host='localhost', port=6800)  # configure here