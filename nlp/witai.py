from wit import Wit
from db import conn


class WitAi(object):
    def __init__(self):
        self.cache = conn['cache']
        self.client = Wit('TXONRQB3KTHTF57HOXPNTM3N5ED3CBXY')

    def wit_ai(self, message):
        cache = self.cache.find_one({'msg': message})
        if cache is not None:
            print('wit ai used cache')
            resp = cache['result']
            self.cache.update_one({'msg': message}, {'$inc': {'times': 1}})
            return resp
        print('connect to wit ai server')
        resp = self.client.message(message)
        self.cache.insert_one({'msg': message, 'result': resp, 'times': 1})
        return resp



