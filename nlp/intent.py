

class Intent(object):
    def __init__(self, raw=None, storyid=None):
        self.raw_intent = raw
        self.storyid = storyid
        self.intent_type = raw['entities'].get('intent', None)
        self.entities = [k for k, v in raw['entities'].items() if k != 'intent']


# for test
if __name__ == '__main__':
    data = {
    "msg_id": "387b8515-0c1d-42a9-aa80-e68b66b66c27",
    "_text": "how many people between Tuesday and Friday",
    "entities": {
      "metric": [ {
        "metadata": "{'code': 324}",
        "value": "metric_visitor",
        "confidence": 0.9231
      } ],
      "datetime": [ {
        "value": {
          "from": "2014-07-01T00:00:00.000-07:00",
          "to": "2014-07-02T00:00:00.000-07:00"
        },
        "confidence": 1
      }, {
        "value": {
          "from": "2014-07-04T00:00:00.000-07:00",
          "to": "2014-07-05T00:00:00.000-07:00"
        },
        "confidence": 1
      }]
    }
  }
    intent = Intent(data, None)
    print(intent.intent_type)
    print(intent.entities)


