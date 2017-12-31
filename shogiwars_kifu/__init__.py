import requests
from bs4 import BeautifulSoup
import urllib
import time
import os
import argparse

URL = 'http://swks.sakura.ne.jp/wars/kifusearch/'


def download_kifu(kifu_url, save_dir):
    file_path = os.path.join(save_dir, os.path.basename(kifu_url))
    if os.path.exists(file_path):
        return False
    print(os.path.basename(kifu_url))
    try_count = 0
    while True:
        try:
            r = requests.get(kifu_url)
            kifu_data = r.content.decode('shift-jis')
            if kifu_data.startswith('開始日時'):
                with open(file_path, 'wb') as f:
                    f.write(r.content)
                return True
        except Exception as e:
            print('server error', e)
            time.sleep(1)
            try_count += 1
            if try_count > 10:
                exit()


def get_kifu_from_wars(user_name, gtype='10', save_dir='./', latest_only=False):
    print('username :', user_name)
    print('game type :', {'10': '10切れ', '3': '3切れ', '10s': '10秒'}[gtype])
    try_count = 0
    while True:
        try:
            client = requests.session()

            # Retrieve the CSRF token first
            client.get(URL)  # sets cookie
            csrftoken = client.cookies['csrftoken']

            data = {
                'csrfmiddlewaretoken': csrftoken,
                'name1': user_name,
                'name2': '',
                'gtype': gtype
            }

            r = client.post(URL, data=data, headers=dict(Referer=URL))
            break
        except Exception as e:
            print('server error', e)
            time.sleep(1)
            try_count += 1
            if try_count > 10:
                exit()

    soup = BeautifulSoup(r.content, 'lxml')
    print('save kifu')
    if latest_only:
        tr = soup.findAll('tr')[0]
        kifu_url = urllib.parse.urljoin(URL, tr.findAll('a')[1]['href'])
        print(kifu_url)
        res = download_kifu(kifu_url, save_dir)
        c = 1 if res else 0
    else:
        c = 0
        for tr in soup.findAll('tr')[::-1]:
            kifu_url = urllib.parse.urljoin(URL, tr.findAll('a')[1]['href'])
            res = download_kifu(kifu_url, save_dir)
            if res:
                c += 1
    print('get {} new kifu'.format(c))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_name')
    parser.add_argument('-t', '--game_type', choices=['10', '3', '10s'], default='10')
    parser.add_argument('-d', '--save_dir', default='./')
    args = parser.parse_args()

    get_kifu_from_wars(args.user_name, gtype=args.game_type, save_dir=args.save_dir)
