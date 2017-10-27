# encoding=UTF-8
from nlp.logic import Logic
from nlp.intent import Intent
from nlp.traslate import Translate
from nlp.witai import WitAi
from nlp.response import Response


class Brain(object):
    def __init__(self):
        pass

    def listen(self, sentence, storyid=None):
        tras = Translate().translate(sentence)
        print(tras)
        wit = WitAi().wit_ai(tras)
        print(wit)
        intent = Intent(wit)
        if storyid is not None:
            intent.storyid = storyid
        r = Logic().understand(intent)
        resp = Response().handle_reaction(r)

        return resp


if __name__ == '__main__':
    brain = Brain()
    r = brain.listen('今天天气怎么样？')
    print (r['text'])
    r = brain.listen('把空调打开')
    print(r['text'])
    r = brain.listen('卧室', r['storyid'])
    print(r['text'])
    r = brain.listen('25度', r['storyid'])
    print(r['text'])

