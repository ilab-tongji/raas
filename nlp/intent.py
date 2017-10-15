
class Intent(object):
    def __init__(self, raw=None, storyid=None):
        self.raw_intent = raw
        self.storyid = storyid
        self.intent_type = raw['entities'].get('intent', None)
        if self.intent_type is not None:
            raw['entities'].pop('intent')
            self.entities = raw['entities']


if __name__ == '__main__':
    from mockdata import data
    print Intent(data).entities
