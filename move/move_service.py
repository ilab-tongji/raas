#coding=UTF-8


direction={
    'on': 'move forward instruction',
    'back': 'move backward instruction',
    'left': 'turn left instruction',
    'right': 'turn right instruction'
}


class MoveService():
    def __init__(self):
        pass

    def move(self, entities):
        if entities.get('location') is None:
            print direction['on']
        else:
            dirc = entities['location'][0]['value']
            print direction[dirc]
        res = {'err': None, 'text': '好的'}
        return res
