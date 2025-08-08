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

## 3.腾讯课堂