import urllib.request
from bs4 import BeautifulSoup
import os


origin = "http://imas.gamedbs.jp/"

def get_html(url):
    return urllib.request.urlopen(url)


def save_images(url, dst_dir):
    # HTMLを取得し、soupに変換
    try:
        html = get_html(url)
    except:
        return -1
    soup = BeautifulSoup(html, 'lxml')

    # アイドル名を取得
    page_title = soup.find('title').string
    idol_name, _ = page_title.split(' | ')

    dst_dir_ = os.path.join(dst_dir, idol_name)
    os.makedirs(dst_dir_, exist_ok=True)

    # 画像のurlを取得していく
    index = 0
    image_titles = []
    for table in soup.find_all('table'):
        for link in table.find_all('a'):
            image_url = link.get('href')
            image_title = link.get('title')
            _, ext = os.path.splitext(image_url)
            if ext == '.jpg':
                try:
                    if not image_title in image_titles:
                        dst_path = os.path.join(dst_dir_, "{0}.jpg".format(index))
                        dst_path = dst_path.replace(os.sep, '/')
                        index += 1
                        print(origin + image_url)
                        urllib.request.urlretrieve(origin + image_url, dst_path)
                        image_titles.append(image_title)
                        print(dst_path)
                except:
                    pass


def main():
        dst_dir = "./data"

        for i in range(200):
            url = origin + "cg/idol/detail/{}".format(i)
            save_images(url, dst_dir)


if __name__ == "__main__":
    main()
