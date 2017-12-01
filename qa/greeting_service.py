#coding=UTF-8
from service import Service

class GreetService(Service):
    def __init__(self):
        super(GreetService,self).__init__('greeting')

    def getName(self, entities):
        name = '赵德芳'
        return name