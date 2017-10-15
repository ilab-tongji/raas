from nlp.logic import Logic
from nlp.context import ContextManager
from nlp.intent import Intent

class Brain(object):
    def __init__(self):
        pass

    def listen(self, sentence):
        tras = sentence
        wit = tras
        intent = wit
        r = Logic().understand(intent)
        txt = ''
        storyid = ''
        for action in r.actions:
            if action.type == 'sendtext':
                txt = action.text
            if action.type == 'savecontext':
                storyid = ContextManager().save_context(action.context, action.intent_type, action.storyid)
        return {'text': txt, 'storyid': storyid}


if __name__ == '__main__':
    from nlp.mockdata import data, data2, data3
    intent1 = Intent(data)
    intent2 = Intent(data2)
    intent3 = Intent(data3)
    brain = Brain()
    r = brain.listen(intent1)
    print r['text']
    intent2.storyid = r['storyid']
    r = brain.listen(intent2)
    print r['text']
    intent3.storyid = r['storyid']
    r = brain.listen(intent3)
    print r['text']
