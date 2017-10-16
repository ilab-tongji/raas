from wit import Wit


class WitAi(object):
    def __init__(self):
        pass

    def wit_ai(self, message):
        client = Wit('FYVFNVKD6B6UNRB24AWOTB4726YBNXKT')
        resp = client.message(message)
        return resp
