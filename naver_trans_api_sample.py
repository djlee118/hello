from requests import Request
from requests import Session

s = Session()

headers = {
    'X-Naver-Client-Id': 'HENlGU5KLu_scfObhSOG',
    'X-Naver-Client-Secret': 'j1APNbDgjl'
}

text = 'Yesterday all my troubles seemed so far away.'

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('post', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)
result = res.json()['message']['result']['translatedText']
print(result)

