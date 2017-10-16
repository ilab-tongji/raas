from wit import Wit


class WitAi(object):
    def __init__(self):
        pass

    def wit_ai(self, message):
        client = Wit('TXONRQB3KTHTF57HOXPNTM3N5ED3CBXY')
        resp = client.message(message)
        return resp
