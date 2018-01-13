#coding=UTF-8
from service import Service
import numpy as np
from hfr.face_reco import FaceRecog


class GreetService(Service):
    def __init__(self):
        super(GreetService,self).__init__('greeting')
        self.names = {'long': '成龙',
                      'fang': '赵德芳',
                      'Unknown':'Unknown'}

    def getName(self, entities=None):
        name = FaceRecog().face_recognition()
        # name = np.random.choice(self.names.keys(),1)
        return '你好,'+self.names[name]

    def detect(self):
        return self.names[FaceRecog().face_recognition()]