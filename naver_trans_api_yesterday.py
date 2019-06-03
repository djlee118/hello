from requests import Request, Session
import codecs

NAVER_CLIENT_ID = 'HENlGU5KLu_scfObhSOG'
NAVER_CLIENT_SECRET = 'j1APNbDgjl'

s = Session()

headers = {
    'X-Naver-Client-Id': NAVER_CLIENT_ID,
    'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
}

eng_list = []

f = open('과제 1_첨부파일_yesterday.txt', 'r')
lines = f.readlines()
for line in lines:
    eng_list.append(line)

f.close()

eng_str = "".join(eng_list)

print(eng_str)

payload = {
    'source': 'en',
    'target': 'ko',
    'text': eng_str
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()
res = s.send(prepped)
res_json = res.json()

result = res_json['message']['result']['translatedText']
print(result)

with codecs.open('yesterday_translated.txt', 'w', 'utf-8-sig') as fw:
    fw.write(eng_str)
    fw.write('\n\n')
    fw.write(result)








# text = 'Yesterday all my troubles seemed so far away.'
#
# payload = {
#     'source': 'en',
#     'target': 'ko',
#     'text': text
# }
#
# url = 'https://openapi.naver.com/v1/language/translate'
#
# req = Request('POST', url, data=payload, headers=headers)
# prepped = req.prepare()
#
# res = s.send(prepped)
#
# res_json = res.json()
#
# result = res_json['message']['result']['translatedText']
# print(result)

