import requests
import json

res = requests.get(
    url='https://huaban.com/v3/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN%7Ctotal,facets,split_words,relations,rec_topic_material,topics',
    headers={
        'Usuer-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Cookie': "canary_uuid=8816753f2b7e4c877115c5a639f581dc; canary=.?base; user_device_id=2c52ae9628e3498a91fe73f2b8ee084d; user_device_id_timestamp=1754636160475; _clck=q46jak%7C2%7Cfya%7C0%7C2046; Hm_lvt_d4a0e7c3cd16eb58a65472f40e7ee543=1754636161; Hm_lpvt_d4a0e7c3cd16eb58a65472f40e7ee543=1754636161; HMACCOUNT=77F4707280A48279; huaban-page-setting={%22cols%22:6%2C%22columnSize%22:248}; fd_id=a0c7c75a0c3d224427ba8a077b96ec6b; fd_id_timestamp=1754636161648; _clsk=1boj2kp%7C1754636161660%7C1%7C0%7Cd.clarity.ms%2Fcollect",
        'Guest-token':'2c52ae9628e3498a91fe73f2b8ee084d',
        'Referer':'https://huaban.com/search?q=%E7%BE%8E%E5%A5%B3&original=%E7%BE%8E%E5%A5%B3'
    }

)
print(res.text)
