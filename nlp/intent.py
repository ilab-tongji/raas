
class Intent(object):
    def __init__(self, raw=None, storyid=None):
        self.raw_intent = raw
        self.storyid = storyid
        intent = raw['entities'].get('intent', None)
        if intent is None:
            self.intent_type = None
        else:
            self.intent_type = intent[0].get('value')
        if self.intent_type is not None:
            raw['entities'].pop('intent')
            self.entities = raw['entities']



if __name__ == '__main__':
    from mockdata import data
    print Intent(data).entities
