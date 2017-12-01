#coding=UTF-8
from service import Service
from hfr.face_reco import FaceRecog

class GreetService(Service):
    def __init__(self):
        super(GreetService,self).__init__('greeting')
        self.names = {'long': '成龙',
                      'fang': '赵德芳'}

    def getName(self, entities):
        name = FaceRecog().face_recognition()
        return '你好,'+self.names[name]