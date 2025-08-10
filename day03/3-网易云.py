# 作者：liuyankai
# 时间：2025年08月10日15时56分35秒
# liuyankai23@mails.ucas.ac.cn
import requests
from bs4 import BeautifulSoup

res = requests.get(
    url="https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD",
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Referer": "https://music.163.com/"
    }
)
# print(res.text)
soup = BeautifulSoup(res.text,features='html.parser')
parent_tag = soup.find(name='ul',attrs={'id':'m-pl-container'})
# print(parent_tag)
for child in parent_tag.find_all(recursive=False):
    title = child.find(name='a',attrs={'class':'tit f-thide s-fc0'}).text
    image_url = child.find(name='img').attrs['src']
    # print(title,image_url)
    img_res = requests.get(url=image_url)
    file_name = title.split()[0]
    with open(f'./pic/{file_name}.jpg',mode='wb') as f:
        f.write(img_res.content)