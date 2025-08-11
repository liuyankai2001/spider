import requests
import ddddocr


res = requests.post(
    url='https://api.ruanwen.la/api/auth/captcha/generate',
)
res_dict = res.json()
# print(res.text)
print(res_dict)
captcha_token = res_dict['data']['captcha_token']
src = res_dict['data']['src']
res = requests.get(url=src)
with open('img/xx.png',mode='wb') as f:
    f.write(res.content)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)
print(code)

res = requests.post(
    url='https://api.ruanwen.la/api/auth/authenticate',
    json={
        'mobile':'liuyankai',
        'password':'123456',
        'captcha':code,
        'captcha_token':captcha_token,
        'device':'pc',
        'identity':'advertiser'
    }
)
print(res.json())