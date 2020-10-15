import unittest
from log_bot import NBot
import log_bot
from unittest.mock import Mock

_us_id = '123456'
_mes = 'hello'
_rand = '0'

class MyTestCase(unittest.TestCase):
    def test_wrt_msg(self):
        bot_mock = NBot(group_id='', token='')
        fake_user = _us_id
        fake_msg = _mes
        fake_rand = _rand
        fake_get_send = Mock(return_value=fake_user, return_value1=fake_msg, return_value2=fake_rand)
        log_bot.messages.send = fake_get_send
        result = bot_mock.write_msg(_us_id, _mes, _rand)
        self.assertEqual(result, '123456')


if __name__ == '__main__':
    unittest.main()
