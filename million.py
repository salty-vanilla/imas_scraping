import urllib.request
from bs4 import BeautifulSoup
import os
import re


realities = ['sr', 'hr', 'r', 'hn', 'n']
idol_table = "http://imas-million.zukan-jp.com/idol_table/"
uploader = "http://imas-million.zukan-jp.com/wp-content/uploads/"


def get_html(url):
    return urllib.request.urlopen(url)


def get_idol_profiles(table_url):
    html = get_html(table_url)
    soup = BeautifulSoup(html, 'lxml')
    urls = []
    for tbody in soup.find_all('tbody'):
        for link in tbody.find_all('a', href=re.compile("profile")):
            url = link.get('href')
            urls.append(url)
    return urls


def get_idol_names(table_url):
    idol_profiles = get_idol_profiles(idol_table)
    names = []
    for ip in idol_profiles:
        elements = ip.split('/')
        for e in elements:
            if 'profile' in e:
                names.append(e.replace('profile_', ''))
    return names


def get_images_from_uploader(name, dst_dir):
    _dst_dir = os.path.join(dst_dir, name)
    os.makedirs(_dst_dir, exist_ok=True)
    index = 0
    for r in realities:
        for i in range(1, 100):
            if i == 1:
                url = uploader + r + '_' + name + '.jpg'
            else:
                url = uploader + r + '_' + name + '_' + str(i) + '.jpg'
            try:
                dst_path = os.path.join(_dst_dir, '{}.jpg'.format(index))
                urllib.request.urlretrieve(url, dst_path)
                index += 1
            except:
                break


def main():
    dst_dir = "./million"
    idol_names = get_idol_names(table_url=idol_table)
    for name in idol_names:
        get_images_from_uploader(name, dst_dir)


if __name__ == "__main__":
    main()
