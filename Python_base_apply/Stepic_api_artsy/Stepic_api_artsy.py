'''
Получение токена
'''
import requests
import json
client_id = '1fdb2c99197c5093dfc9'
client_secret = '24a2dba05c5ba8f3d63981276bb677ab'
r = requests.post(
    'https://api.artsy.net/api/tokens/xapp_token',
    data = {"client_id": client_id,
            "client_secret": client_secret
                  })

j = json.loads(r.text)
token = j['token']
'''
Get запрос и получение информации
о деятелях искусства
'''
answer = {}
headers = {"X-Xapp-Token" : token}
with open('dataset_24476_4.txt', encoding='UTF-8') as f:
#f = ['4d8b92b34eb68a1b2c0003f4', '537def3c139b21353f0006a6', '4e2ed576477cc70001006f99']
    for i in f:
        i = i.strip()
        req = requests.get(
            'https://api.artsy.net/api/artists/{}'.format(i),
            headers = headers)
        rq = json.loads(req.text)
        if rq['birthday'] in answer:
            answer[rq['birthday']].append(rq["sortable_name"] + '\n')
        else:
            answer[rq['birthday']] = [rq["sortable_name"] + '\n']
with open('ans.txt', 'w', encoding='UTF-8') as d:
    for i in sorted(answer):
        answer[i].sort()
        for k in answer[i]:
            d.write(k)
        

