from requests import Request, Session
import pprint

NAVER_CLIENT_ID = 'HENlGU5KLu_scfObhSOG'
NAVER_CLIENT_SECRET = 'j1APNbDgjl'


s = Session()
headers = {
    'X-Naver-Client-Id': NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': NAVER_CLIENT_SECRET,
}

text = "Somewhere over the rainbow way up high"

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

res_json = res.json()
pprint.pprint(res_json)
pprint.pprint(res_json['message']['result']['translatedText'])
