# 作者：liuyankai
# 时间：2025年08月10日16时49分03秒
# liuyankai23@mails.ucas.ac.cn
import requests

res = requests.post(
    url='https://passport.china.com/logon',
    data={
        'userName': '18630087660',
        'passwd': '123123'
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Referer": "https://www.china.com/"
    }
)

print(res.text)
