import uuid
from bson import UUIDLegacy
from db import conn


class ContextManager(object):
    def __init__(self):
        # stories : {"stortid": {'intent_type': xxx, 'contexts': [context]}}
        self.stories = conn['story']

    def save_context(self, context, intent_type, storyid=None):
        if storyid is None:
            new_storyid = str(uuid.uuid4())
            self.stories.insert_one(dict(storyid=new_storyid, intent_type=intent_type, contexts=[context]))
            return new_storyid
        else:
            self.stories.update_one({'storyid': storyid}, {'$push': {'contexts': context}})
            return storyid

    def get_context(self, storyid):
        def heap(x, y):
            x.update(y)
            return x
        if storyid is None:
            story = None
        else:
            story = self.stories.find_one({'storyid': storyid})
        if story is None:
            return {}
        contexts = reduce(lambda x, y: heap(x, y), story['contexts'])
        return contexts

if __name__ == '__main__':
    print ContextManager().get_context('a144df92-666b-40c4-9038-c8679b8b40d1')
    #print ContextManager().save_context({'location': 'restroom'}, 'open', 'a144df92-666b-40c4-9038-c8679b8b40d1')
    # a144df92-666b-40c4-9038-c8679b8b40d1





