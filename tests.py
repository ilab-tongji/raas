# encoding=utf-8
import app
import unittest
import json
from qa.qa_service import weather


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def ask(self, question):
        request_body = {
            'question': question
        }
        rv = json.loads(self.app.post('/ask', data=json.dumps(request_body), content_type='application/json').data)
        return rv['instructions']['say']

    def test_ask(self):
        say = self.ask('xxxx')
        assert say == '对不起，我们不支持这种服务'
        today_weather = weather.today_weather()['weather']
        say = self.ask('今天天气怎么样')
        print say, today_weather
        assert say == today_weather


if __name__ == '__main__':
    unittest.main()