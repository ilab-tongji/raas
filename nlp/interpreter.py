# encoding=utf-8
import jieba
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


def analyse(sentence):
    words = list(jieba.cut(sentence=sentence, cut_all=True))
    if "天气" in words:
        serv = 'qa'
        t = 'weather'
        city = 'shanghai'
        day = 0
        slots = {'city': city, 'day': day}
        return dict({'service': serv, 't': t, 'slots': slots})
    else:
        serv = None
        t = None
        return dict({'service': serv, 't': t})


