from nlp.context import ContextManager

class Response(object):
    def __init__(self):
        pass

    def handle_reaction(self, reaction):
        resps = {}
        for action in reaction.actions:
            handler = ActionHandlerFactory.get_handler(action.type)()
            resp = handler.handle(action)
            resps.update(resp)
        return resps


class ActionHandler(object):
    def __init__(self, t):
        self.type = t

    def handle(self,action):
        raise NotImplementedError


class SendTextActionHandler(ActionHandler):
    def __init__(self):
        super(SendTextActionHandler, self).__init__('sendtext')

    def handle(self,action):
        return {'text': action.text}


class SaveContextActionHandler(ActionHandler):
    def __init__(self):
        super(SaveContextActionHandler, self).__init__('savecontext')

    def handle(self, action):
        storyid = ContextManager().save_context(action.context, action.intent_type, action.storyid)
        return {'storyid': storyid}


class ActionHandlerFactory(object):
    action_map = {
        'sendtext': SendTextActionHandler,
        'savecontext': SaveContextActionHandler
    }

    def __init__(self):
        pass

    @classmethod
    def get_handler(cls, t):
        return cls.action_map[t]





