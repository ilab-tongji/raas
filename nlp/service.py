#coding=UTF-8
necessary_request={
    "appliance":{
        "air conditioner":{
            "on":['location','temperature'],
            "off":['location']
        }
    }
}

class Service(object):
    def __init__(self,type):
        self.type=type

class ApplianceService(Service):
    def __init__(self,name):
        super(ApplianceService,self).__init__('appliance')
        self.name=name
    def open(self):
        raise NotImplementedError


class AirConditionerService(ApplianceService):
    def __init__(self):
        super(AirConditionerService,self).__init__('air conditioner')

    def open(self,entities):
        neces=necessary_request['appliance']['air conditioner']['on']
        for nece in neces:
            if not(nece in entities.keys()):
                if nece == 'location':
                    text='请问是哪里的空调？'
                elif nece == 'temperature':
                    text='请问要调到多少度？'
                res={'err':'missing value','slot':nece,'text':text}
                return res
        res={'err':None,'text':'空调已打开'}
        print res
        return res


class ApplianceServiceFactory(object):
    def __init__(self):
        pass
    service_map={
        'open_airConditioner':AirConditionerService
    }

    @classmethod
    def get_service(cls,name):
        return cls.service_map[name]


if __name__=='__main__':
    entities={
      "intent": "open_airConditioner",
      "device": "air conditioner",
      "location":"bedroom",
      "temperature":'25 degrees'
    }
    handle=ApplianceServiceHandle().get_service('open_airConditioner')()
    print handle
    handle.open(entities)
    #print necessary_request['appliance']['air conditioner']['on']

