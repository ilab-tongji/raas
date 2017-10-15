# encoding=UTF-8
from nlp.logic import Logic
from nlp.intent import Intent
from nlp.traslate import translate
from nlp.witai import wit_ai
from nlp.response import Response


class Brain(object):
    def __init__(self):
        pass

    def listen(self, sentence, storyid=None):
        tras = translate(sentence)
        print(tras)
        wit = wit_ai(tras)
        intent = Intent(wit)
        if storyid is not None:
            intent.storyid = storyid
        r = Logic().understand(intent)
        resp = Response().handle_reaction(r)
        return resp


if __name__ == '__main__':
    # from nlp.mockdata import data, data2, data3
    # intent1 = Intent(data)
    # intent2 = Intent(data2)
    # intent3 = Intent(data3)
    brain = Brain()
    r = brain.listen('把空调打开')
    print(r['text'])
    r = brain.listen('卧室', r['storyid'])
    print(r['text'])
    r = brain.listen('25度', r['storyid'])
    print(r['text'])



    # intent2.storyid = r['storyid']
    # r = brain.listen(intent2)
    # print r['text']
    # intent3.storyid = r['storyid']
    # r = brain.listen(intent3)
    # print r['text']