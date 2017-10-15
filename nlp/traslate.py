import requests
import hashlib
import random

appid = '20171011000087545'
secretKey = '3fKGqzXDd_TFHeiCPQQv'

httpClient = None
myurl = 'http://fanyi-api.baidu.com/api/trans/vip/translate'
q = 'apple'
fromLang = 'zh'
toLang = 'en'
salt = random.randint(32768, 65536)


def translate(q):
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign)
    sign = m1.hexdigest()
    params = {'appid': appid, 'q': q, 'from': fromLang, 'to': toLang, 'salt': str(salt), 'sign': sign}
    r = requests.get(myurl, params=params)
    print(r.json())
    return (r.json())['trans_result'][0]['dst']