necessary_request={
    "appliance":{
        "air conditioner":{
            "on":['location','temperature'],
            "off":['location']
        }
    }
}

class service(object):
    def __init__(self,type):
        self.type=type

class appliance_service(object):
    def __init__(self,appliance_name):
        super(service,self).__init__('appliance')

class airConditioner_service(object):
    def __init__(self,intent):
        super(appliance_service,self).__init__('air conditioner')
        self.intent=intent

    def necessity_check(self):
        entities=self.intent.entities
        intent=entities['intent'][0]['value']
        if intent == 'open appliance':
            neces=necessary_request['appliance']['air conditioner']['on']
            for nece in neces:
                if not(nece in entities):
                    res={'type':'missing value'}
                    return

if __name__=='__main__':
    print necessary_request['appliance']['air conditioner']['on']

