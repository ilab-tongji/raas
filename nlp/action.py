class Action(object):
    def __init__(self, t):
        self.type = t


class SendTextAction(Action):
    def __init__(self, text):
        super(SendTextAction, self).__init__('sendtext')
        self.text = text


class SaveContextAction(Action):
    def __init__(self, context, intent_type, storyid=None):
        super(SaveContextAction, self).__init__('savecontext')
        self.context = context
        self.intent_type = intent_type
        self.storyid = storyid


class Reaction(object):
    def __init__(self, actions, intent, storyend=True):
        self.actions = actions
        self.intent = intent
        self.storyend = storyend




