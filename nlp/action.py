class Action(object):
    def __init__(self, t):
        self.type = t


class SendTextAction(Action):
    def __init__(self, text):
        super(SendTextAction, self).__init__('sendtext')
        self.text = text


class SaveContextAction(Action):
    def __init__(self, context, storyid):
        super(SaveContextAction, self).__init__('savecontext')
        self.context = context
        self.storyid = storyid

