# 一、浏览器初识

## 1.1 Network

**Headers：头信息**

* General
  * Request URL：请求地址
  * Status Code：请求状态
  * Remote Address：请求远程服务器IP
* Request Headers：请求头
  * User-Agent：浏览器标识
  * Refer：上次访问的网页
  * Content-Type：请求体格式
* Response Headers：返回头

**Response：返回内容**

* Set-Cookie：设置cookie

**Preview：预览Response内容**

**Payload：参数**

* Query String Parameters：URL中的参数
* Form Data：（post方式才有）请求体中携带的参数
* Request Payload：（post方式才有）请求体中携带的参数



User-Agent：`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36`

## 1.2 request模拟发送请求

```python
import requests

# get 请求
"""
res = requests.get(
    url='https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=0&limit=20&category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8',
    headers={
        'Usuer-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }
)
print(res.text)
print(res.headers)
"""
# post 请求
"""
res = requests.post(
    url='https://dig.ichouti.cn/login',
    # 如果是&格式
    data={
        'passwd': '123123',
        'jid': 'liuyankai'
    },
    headers={
        'Usuer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }
)
print(res.text)
print(res.headers)
"""

"""
res = requests.post(
    url='https://dig.ichouti.cn/login',
    # 如果是json格式
    json={
        'passwd': '123123',
        'jid': 'liuyankai'
    },
    headers={
        'Usuer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }
)
print(res.text)
print(res.headers)

"""
```



## 1.3 豆瓣网案例

请求方式：`GET`

请求地址：`https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?limit=50&category=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&type=%E5%85%A8%E9%83%A8`

## 1.4 抽屉新热榜案例

请求方式：`POST`（有请求体，Paload中的Form Data）

请求地址：`https://dig.ichouti.cn/login`



# 二、基础知识

## 2.1 URL参数

无论是在发送GET/POST请求时，网址URL都可能会携带参数，例如：http://www.XXXXX.com?age=11&name=liuyankai

```python
res = requests.get(
	url="http://www.XXXXX.com?age=11&name=liuyankai"
)
```

```python
res = requests.get(
	url="https://www.XXXXX.com",
    params={
        "age":11,
        "name":"liuyankai"
        "home":"河南省"
    } # 可以放中文
)
```

## 2.2 请求体格式

在发送POST请求时候，常见的请求体格式一般有二种：

* form表单格式（抽屉新热榜）

  ```python
  name=wupeiqi&age=18&size=99
  
  特征：
  	1.谷歌浏览器抓包 Form Data
      2.请求头 Content-Type:application/x-www-form-urlencoded; charset=UTF-8
  ```

* json格式（腾讯课堂）

  ```python
  {"name":"wupeiqi","age":18,"size":99}
  
  特征：
  	1.谷歌浏览器抓包 Request Payload
  	2.请求头 Content-Type:application/json;charset=utf-8
  ```

  

**form表单格式**

```python
res = requests.post(
    url="...",
    data="name=wupeiqi&age=18&size=99",
    headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
)
```

```python
res = requests.post(
    url="...",
    data={
        "name":"wupeiqi",
        "age":18,
        "size":19
    },
    headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
)
```

**json格式**

```python
res = requests.post(
    url="...",
    data=json.dumps(  {"name":"wupeiqi","age":18,"size":99}  ),
    headers={
        "Content-Type": "application/json;charset=utf-8"
    }
)
```

```python
res = requests.post(
    url="...",
    json={"name":"wupeiqi","age":18,"size":99},
)
```

## 2.3 cookie

Cookie本质上是浏览器存储的键值对，一般用于用户凭证的保存。

* 浏览器向后端发送请求时，后端可以返回cookie（自动保存在浏览器）。
* 后续浏览器再次返送请求时，会自动携带cookie。

读取返回的Cookie：

```python
import requests

res = requests.get(
    url="https://www.bilibili.com/"
)
cookie_dict = res.cookies.get_dict()
print(cookie_dict)   # {"v1":123,"v3":456}
```

发送请求时携带cookie：

```python
import requests

res = requests.get(
    url="https://www.bilibili.com/",
    headers={
        "Cookie":"innersign=0; buvid3=8427E089-F4D7-CCF7-4997-0087D04B3C9810575infoc"
    }
)
```

```python
import requests

res = requests.get(
    url="https://www.bilibili.com/",
    cookies={
        "innersign":"0",
        "buvid3":"8427E089-F4D7-CCF7-4997-0087D04B3C9810575infoc"
    }
)
```

## 2.4 响应体格式

基于requests发送请求后，返回的数据都封装在了res对象中

```python
import requests
import json

res = requests.get(
    url="https://api.huaban.com/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations"
)

# 原始响应体（字节类型）
res.content

# 原始文本，将字节转换成字符串形式
res.text

# 如果返回是JSON格式，可以自动转化json格式。   即：data = json.loads(res.text)   注意：{"xxx":123}       <html></asdfasdfadf</>
data = res.json()
```

**原始字节**：用于 图片、文件、视频 等下载时，获取原始数据。

```python
import requests

res = requests.get(
    url="https://gd-hbimg.huaban.com/b93fcc5bb4751934bbd56918bdab8184966dca2974df1-bo7qSF",
)
print(res.content)

with open("v1.png", mode='wb') as f:
    f.write(res.content)
```

```python
import requests

res = requests.get(
    url="https://v3-web.douyinvod.com/4f17c475df0a484a41fa1abe00f43aaa/65695cf6/video/tos/cn/tos-cn-ve-15c001-alinc2/oIrIAZg9ChRRquVyAYQdESIxNWAQzBACtzJemf/?a=6383&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1354&bt=1354&cs=0&ds=4&ft=GN7rKGVVyw3XRZ_8emo~xj7ScoAp9656EvrK-iBTkto0g3&mime_type=video_mp4&qs=0&rc=ZWU7NTo3NDc0ZDM2ODQ6OkBpM2c8ODw6Zm9qbjMzNGkzM0AxNS9eY2BjNTQxYGIvYDMwYSNgZzVpcjRnamxgLS1kLS9zcw%3D%3D&btag=e00030000&dy_q=1701400015&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20231201110655C26B991C0F271857AB12",
)
# print(res.content)

with open("v1.mp4", mode='wb') as f:
    f.write(res.content)
```

**普通文本**

```python
import requests

res = requests.get(
	url="....."
)
print(res.text)

# 输出
'''
<!DOCTYPE html>
<html lang="en">
<head>
...
'''
'''
{"subjects":[{"episodes_info":"","rate":"9.7","cover_x":2000,"title":"肖申克的救赎"...
'''
```

**转换格式**：对于json格式，为了更方便的获取内部元素，可以转换成python的字典或列表等类型。

```python
import requests

res = requests.get(
    url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
)

# 手动转换
import json
data_dict = json.loads(res.text)

# 内部自动转换
data_dict = res.json()
```

# 三、bs4的使用

## 3.1 安装

`pip install beautifulsoup4`

## 3.4 使用

首先初始html为：

```html
<div>
    <h1 class="item">武沛齐</h1>
    <ul class="item">
        <li>篮球</li>
        <li>足球</li>
    </ul>
    <div id='x3'>
        <span>5xclass.cn</span>
        <a href="www.xxx.com" class='info'>pythonav.com</a>
    </div>
</div>
```

根据**标签名称**，获取标签（只获取找到的第1个）

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_string, features="html.parser")
tag = soup.find(name='a')

print(tag)       # 标签对象
print(tag.name)  # 标签名字 a
print(tag.text)  # 标签中间文本 pythonav.com
print(tag.attrs) # 标签属性 {'href': 'www.xxx.com', 'class': ['info']}
```

根据**属性**获取标签（只获取找到的第1个）

```python
soup = BeautifulSoup(html_string, features="html.parser")
tag = soup.find(name='div', attrs={"id": "x3"})

print(tag)
```

嵌套读取，先找到某个标签，然后再去孩子标签中寻找

```python
soup = BeautifulSoup(html_string, features="html.parser")
parent_tag = soup.find(name='div', attrs={"id": "x3"})

child_tag = parent_tag.find(name="span", attrs={"class": "xx1"})

print(child_tag)
```

读取所有标签（多个）

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_string, features="html.parser")
tag_list = soup.find_all(name="li")
print(tag_list)

# 输出
# [<li>篮球</li>, <li>足球</li>]
```

# 四、自动登录

## 4.1  表单请求和ajax请求

当看到页面上有一个表单时，当输入账号+点击登录/注册提交，数据提交就两种方式：

* 表单提交，特征：提交数据页面刷新
* ajax提交，特征：提交页面不刷新，“偷偷”提交。

Ajax请求的底层是基于XMLHttpRequest对象实现，所以在抓包时发现两个特征：页面不刷新 + 请求类型是xhr 。

例如：北京大学BBS论坛 https://bbs.pku.edu.cn/v2/home.php

## 4.2 常见登录流程

常见的登录流程一般有两种，情况不同，在基于爬虫实现自动登录时，也需要做不同的调整。

**方式1**

正常请求流程：

* **第1次访问**，后台会返回内容+Cookie，在cookie中保存当前用户凭证（此时凭证没啥用）
* **第2次访问**，输入用户名+密码提交，此时浏览器会自动将第1次返回的凭证携带到后台； 后台校验成功，此时给凭证赋予登录权限（还是原来的凭证，只不过此时的凭证是用户已登录的标识了）。
* **第n次访问**，携带Cookie中的凭证去访问，后台就会根据凭证（用户标识）返回词用户的相关信息。

基于爬虫去模拟请求实现时：

* 第1次访问，读取返回Cookie并保存
* 第2次访问，携带用户名+密码+上次的Cookie进行登录
* 第n次访问，携带Cookie去访问，获取当前用户信息。

**方式2**

正常请求流程：

* **第1次访问**，后台仅返回页面。
* **第2次访问**，输入**用户名+密码**提交，后台校验成功后，在  **响应体** 或 **Cookie** 返回 用户登录凭证。【网页一般在Cookie中居多】
* **第n次访问**，携带之前返回的凭证去访问，后台就会根据凭证（用户标识）返回词用户的相关信息。

基于爬虫去模拟请求实现时：

* 第2次访问，携带用户名+密码去登录，在 响应体 或 Cookie中读取用户凭证。【网页一般在Cookie中居多】
* 第n次访问，携带凭证去访问，获取当前用户信息。



# 五、图片验证码识别

## 5.1 本地识别ddddorc

```
pip install ddddocr==1.4.9  -i https://mirrors.aliyun.com/pypi/simple/
pip install Pillow==9.5.0
```

```python
import ddddocr

ocr = ddddocr.DdddOcr(show_ad=False)
with open("img/v1.jpg", mode='rb') as f:
    body = f.read()
code = ocr.classification(body)
print(code)
```

## 5.2 在线识别

直接请求获取图片，然后直接识别：

```python
import ddddocr
import requests

res = requests.get(url="https://console.zbox.filez.com/captcha/create/reg?_t=1701511836608")

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)
```

```python
import ddddocr
import requests


res = requests.get(
    url=f"https://api.ruanwen.la/api/auth/captcha?captcha_token=n5A6VXIsMiI4MTKoco0VigkZbByJbDahhRHGNJmS"
)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)
```

有些平台的图片是以base64编码形式存在，需要处理下在识别。

```python
import base64
import ddddocr

content = base64.b64decode("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")

# with open('x.png', mode='wb') as f:
#     f.write(content)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(content)
print(code)
```



# 案例

## 1.花瓣网

**请求方式：**`GET`

**请求地址：**`https://huaban.com/v3/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN%7Ctotal,facets,split_words,relations,rec_topic_material,topics`

**User-Agent：**`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36`

```python
import requests
import json

res = requests.get(
    url='https://huaban.com/v3/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN%7Ctotal,facets,split_words,relations,rec_topic_material,topics',
    headers={
        'Usuer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }
)
print(json.loads(res.text))
```

## 2.豆瓣高分电影

## 3.易车网获取所有汽车品牌

