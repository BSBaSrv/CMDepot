import requests, os
import sys
from tqdm import tqdm
from urllib.parse import urlencode
from pathlib import Path

def sizeof_fmt(num: int | float) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%.1f %s" % (num, x)

        num /= 1024.0

    return "%.1f %s" % (num, 'TB')

def download(url: str, name: str):
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    public_key = url

    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)
    download_url = response.json()['href']

    download_response = requests.get(download_url, stream=True)

    total_size = int(download_response.headers.get('content-length', 0))
    print('Загрузка:', sizeof_fmt(total_size))

    chunk_size = 1024
    num_bars = int(total_size / chunk_size)

    with open(f"C:/Files/{name}", mode='wb') as f:
        for data in tqdm(download_response.iter_content(chunk_size), total=num_bars, unit='KB', file=sys.stdout):
            f.write(data)

#download("https://disk.yandex.ru/i/wkvl-fMlqqAHTg", "NewFile.mp4")