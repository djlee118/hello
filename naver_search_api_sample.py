import requests
import pprint

headers = {
    'X-Naver-Client-Id': 'HENlGU5KLu_scfObhSOG',
    'X-Naver-Client-Secret': 'j1APNbDgjl'
}

payload = {
    'query': '파이썬',
    'display': 100
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
print('request sended..')
#pprint.pprint(res.json())

result = res.json()['items'][2]['title']
print(result)
