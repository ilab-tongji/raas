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
    def __init__(self):
        pass

class ApplianceService(object):
    def __init__(self):
        pass
    def open(self):
        raise NotImplementedError


class AirConditionerService(object):
    def __init__(self):
        pass

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

if __name__=='__main__':
    ss=AirConditionerService()
    entities={
      "intent": "open_appliance",
      "device": "air condition",
      "location":"bedroom",
      "temperature":'25 degrees'
    }
    ss.open(entities)
    #print necessary_request['appliance']['air conditioner']['on']

