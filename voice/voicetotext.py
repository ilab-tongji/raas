# -*- coding: utf-8 -*-

import urllib2
import json
import base64
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class ToText:
    def __init__(self, cu_id, api_key, api_secert):

        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"

        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"

        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):

        token_url = self.token_url % (api_key,api_secert)
        # print token_url
        r_str = urllib2.urlopen(token_url).read()
        # print r_str
        token_data = json.loads(r_str)
        # print token_data
        self.token_str = token_data['access_token']
        pass

    def getText(self, filename):

        data = {}

        data['format'] = 'wav'
        data['rate'] = 16000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib2.urlopen(self.upvoice_url, data=post_data.encode("utf-8")).read()
        print r_data
        return json.loads(r_data)['result']


