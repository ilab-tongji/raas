from nlp.action import SendTextAction, SaveContextAction, Reaction
from nlp.context import ContextManager
from appliance.appliance_service import ApplianceServiceFactory
from qa.weather_service import WeatherService
from move.move_service import MoveService
from qa.greeting_service import GreetService




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
        self.overall_intent_entities = self.intent.entities.copy()
        self.overall_intent_entities.update(former_context)
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


class OpenAirConditionerIntentResolver(IntentResolver):
    def __init__(self, intent):
        super(OpenAirConditionerIntentResolver, self).__init__(intent)

    def resolve(self):
        actions = []
        r = ApplianceServiceFactory.get_service('open_airConditioner')().open(self.overall_intent_entities)
        err = r['err']
        text = r['text']
        actions.append(SendTextAction(text))
        if err:
            actions.append(SaveContextAction(self.intent.raw_intent['entities'],
                                             self.intent.intent_type,
                                             self.intent.storyid))
            self.storyend = False
        return Reaction(actions, self.intent, self.storyend)

class GetWeatherIntentResolver(IntentResolver):
    def __init__(self, intent):
        super(GetWeatherIntentResolver,self).__init__(intent)

    def resolve(self):
        actions = []
        r = WeatherService().getWeather(self.overall_intent_entities)
        actions.append(SendTextAction(r))
        self.storyend = True
        return Reaction(actions, self.intent, self.storyend)

class MoveIntentResolver(IntentResolver):
    def __init__(self, intent):
        super(MoveIntentResolver, self).__init__(intent)

    def resolve(self):
        actions = []
        r = MoveService().move(self.overall_intent_entities)
        err = r['err']
        text = r['text']
        actions.append(SendTextAction(text))

class GreetIntentResolver(IntentResolver):
    def __init__(self, intent):
        super(GreetIntentResolver, self).__init__(intent)

    def resolve(self):
        actions = []
        r = GreetService().getName(self.overall_intent_entities)
        actions.append(SendTextAction(r))
        self.storyend = True
        return Reaction(actions, self.intent, self.storyend)



class IntentResolverFactory(object):
    map = {
        'open_airConditioner': OpenAirConditionerIntentResolver,
        'location': OpenAirConditionerIntentResolver,
        'temperature': OpenAirConditionerIntentResolver,
        'get_weather': GetWeatherIntentResolver,
        'move': MoveIntentResolver,
        'greeting':GreetIntentResolver
    }

    def __init__(self):
        pass

    @classmethod
    def get_resolver(cls, intent):
        return cls.map.get(intent.intent_type, None)(intent)

if __name__ == '__main__':
    from mockdata import data, data2
    from nlp.intent import Intent
    from uuid import uuid4
    intent1 = Intent(data)
    logic1 = Logic()
    r = logic1.understand(intent1)
    intent2 = Intent(data2)
    logic2 = Logic()
    a =  logic2.understand(intent2)
    print 1
