from wit import Wit

def wit_ai(message):
    client = Wit('FYVFNVKD6B6UNRB24AWOTB4726YBNXKT')
    resp = client.message(message)
    return resp