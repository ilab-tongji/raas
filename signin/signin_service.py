#coding=UTF-8
import service


class SigninService(service.Service):
    def __init__(self):
        super(SigninService, self).__init__('signin')


    def check(self):
        return {'detail': '...', 'text':'你好，这是今天的签到情况'}


