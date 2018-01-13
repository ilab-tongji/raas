#coding=UTF-8
import service
from qa.greeting_service import GreetService


class SigninService(service.Service):
    def __init__(self):
        super(SigninService, self).__init__('signin')


    def check(self):
        name = GreetService().detect()
        if name != 'Unknown':
            return {'detail': '...', 'text':'你好，'+name+',这是今天的签到情况'}
        else:
            return {'detail': '...', 'text':'这是今天的签到情况，请问你是谁啊'}


