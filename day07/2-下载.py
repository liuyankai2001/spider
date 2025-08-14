import requests

res = requests.get(
    url='https://music.jsbaidu.com/hot/2004/07-13/24357.mp3',
)

with open('爱在西元前.mp3',mode='wb') as f:
    f.write(res.content)