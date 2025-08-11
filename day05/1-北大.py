import time
import hashlib

import requests

res = requests.get(
    url='https://bbs.pku.edu.cn/v2/login.php',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        # 'Referer':'https://cn.bing.com/',
        # 'Upgrade-Insecure-Requests':'1',
        # 'Host':'bbs.pku.edu.cn'
    }
)
cookie = res.cookies.get_dict()
# print(res.text)
print(cookie)
user = 'liuyankai'
pwd = '123123'
ctime = int(time.time())
datastr = f'{pwd}{user}{ctime}{pwd}'
obj = hashlib.md5()
obj.update(datastr.encode('utf-8'))
md5_sreing = obj.hexdigest()

res = requests.post(
    url='https://bbs.pku.edu.cn/v2/ajax/login.php',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    },
    data={
        'username':user,
        'password':pwd,
        'keepalive':'0',
        'time':ctime,
        't':md5_sreing
    },
    cookies = cookie
)
print(res.text)