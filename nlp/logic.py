from nlp.action import SendTextAction, SaveContextAction, Reaction
from nlp.context import ContextManager


class Service(object):
    def __init__(self):
        pass
    def open(self,intent):
        return 'need location', 'need location'

service = Service()


class Logic(object):
    def __init__(self):
        self.resolver = None

    def understand(self, intent):
        self.resolver = IntentResolverFactory.get_resolver(intent)
        reaction = self.resolver.resolve()
        return reaction


class IntentResolver(object):
    def __init__(self, intent):
        self.intent = intent
        self.contextmgr = ContextManager()
        former_context = self.contextmgr.get_context(intent.storyid)
        self.intent.entities.update(former_context)
        self.storyend = True

    def resolve(self):
        raise NotImplementedError


# class GetApplicanceLocationIntentResolver(IntentResolver):
#     def __init__(self, intent):
#         super(GetApplicanceLocationIntentResolver, self).__init__(intent)
#
#     def resolve(self):
#         actions = []
#         err, text = service.open(self.intent.entities)
#         actions.append(SendTextAction(text))
#         if
#
#
# class GetApplicanceTemperatureIntentResolver(IntentResolver):
#     def __init__(self, intent):
#         super(GetApplicanceTemperatureIntentResolver, self).__init__(intent)
#
#     def resolve(self):
#         return 2


class OpenApplicanceIntentResolver(IntentResolver):
    def __init__(self, intent):
        super(OpenApplicanceIntentResolver, self).__init__(intent)

    def resolve(self):
        actions = []
        err, text = service.open(self.intent.entities)
        actions.append(SendTextAction(text))
        if err:
            actions.append(SaveContextAction(self.intent.raw_intent['entities'],
                                             self.intent.intent_type,
                                             self.intent.storyid))
            self.storyend = False
        return Reaction(actions, self.intent, self.storyend)


class IntentResolverFactory(object):
    map = {
        'open_appliance': OpenApplicanceIntentResolver,
        'appliance_location': OpenApplicanceIntentResolver,
        'temperature': OpenApplicanceIntentResolver
    }

    def __init__(self):
        pass

    @classmethod
    def get_resolver(cls, intent):
        return cls.map.get(intent.intent_type, None)(intent)

if __name__ == '__main__':
    from mockdata import data, data2
    from nlp.intent import Intent
    intent1 = Intent(data)
    intent1.storyid = 'xxx'
    intent2 = Intent(data2)
    intent2.storyid = 'xxx'
    logic1 = Logic()
    print logic1.understand(intent1)
    logic2 = Logic()
    print logic2.understand(intent2)
    print 1
