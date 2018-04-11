#coding=UTF-8

import requests

direction={
    'on': 'move forward instruction',
    'back': 'move backward instruction',
    'left': 'turn left instruction',
    'right': 'turn right instruction'
}


class MoveService():
    def __init__(self):
        self.url = 'http://192.168.31.112:'
        self.port = 5000
        pass

    def move(self, entities):
        if entities.get('location') is None:
            print direction['on']
        else:
            dirc = entities['location'][0]['value']
            print direction[dirc]
        res = {'err': None, 'text': '好的'}
        return res

    def shake_head(self):
        requests.get(self.url+str(self.port)+'/wavehand')


