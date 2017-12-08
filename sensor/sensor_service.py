#coding=UTF-8

from service import Service
import PM
import light


class SensorService(Service):
    def __init__(self, type):
        super(SensorService, self).__init__('sensor')
        self.type = type

    def get_data(self):
        raise NotImplementedError


class PMService(SensorService):
    def __init__(self):
        super(PMService, self).__init__('PM')

    def get_data(self):
        pm = PM.my_pm()
        #re_pm = 'pm2.5含量为'+pm['pm2.5']+'pm10含量为'+pm['pm10']
        return pm

class LightService(SensorService):
    def __init__(self):
        super(LightService, self).__init__('Light')

    def get_data(self):
        li = light.my_sensor()
        return li


class SensorServiceFactory(object):
    def __init__(self):
        pass
    service_map = {
        'get_pm': PMService,
        'get_light': LightService
    }

    @classmethod
    def get_service(cls, name):
        return cls.service_map[name]
