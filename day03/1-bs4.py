# 作者：liuyankai
# 时间：2025年08月10日15时22分38秒
# liuyankai23@mails.ucas.ac.cn
from bs4 import BeautifulSoup

html_string = """<div>
    <h1 class="item x1" id="x2">武沛齐</h1>
    <ul class="item">
        <li>篮球</li>
        <li>足球</li>
    </ul>
    <div id='x3'>
        <span>5xclass.cn</span>
        <a href="www.xxx.com" class='info'>pythonav.com</a>
        
    </div>
</div>"""

soup = BeautifulSoup(html_string,features='html.parser')

parent_tag = soup.find(attrs={'id':'x3'})

parent_tag = soup.find(name='x3')
parent_tag.find_all(recursive=False)


# tag_list = soup.find_all(name='li')
# print(tag_list)

# tag = parent_tag.find(name='a')
# print(tag)
# print(tag.name)
# print(tag.text)
# print(tag.attrs)

# tag = soup.find(name='h1')
# print(tag)
# print(tag.name)
# print(tag.text)
# print(tag.attrs)

# tag = soup.find(name='a')
# print(tag)
# print(tag.name)
# print(tag.text)
# print(tag.attrs)

# tag = soup.find(name='ul',attrs={'class':"item"})
# print(tag)
# print(tag.name)
# print(tag.text)
# print(tag.attrs)