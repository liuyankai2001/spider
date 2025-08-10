# 作者：liuyankai
# 时间：2025年08月10日15时40分31秒
# liuyankai23@mails.ucas.ac.cn
import requests
from bs4 import BeautifulSoup

res = requests.get(
    url="https://car.yiche.com/xuanchegongju/?l=63"
)
# print(res.text)
soup = BeautifulSoup(res.text,features='html.parser')
# tag_list = soup.find_all(name='div',attrs={'class':'item-brand'})
# for tag in tag_list:
#     print(tag.attrs['data-name'])
tag_list = soup.find_all(name='div',attrs={'class':'item-brand'})
for tag in tag_list:
    child = tag.find(name='div',attrs={'class':'brand-name'})
    print(child.text)