import requests

res = requests.post(
    url='https://zz123.com/ajax/',
    data={
        'act':'search',
        'key':'周杰伦',
        'lang':'',
        'page':1
    }
)

dict = res.json()
print(dict)
dlist = dict['data']
for item in dlist:
    print(item)

# res = requests.get(
#     'https://music.jsbaidu.com/hot/2005/11-01/72064.mp3'
# )