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
