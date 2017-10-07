# encoding=utf-8
from qa import qa_service

service_map = {
    'qa': qa_service.get_answer
}


def distribute(inn):
    return service_map.get(inn['service'], no_service)


def no_service(question):
    return '对不起，我们不支持这种服务'
