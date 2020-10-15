import vk_api
import vk_api.bot_longpoll
from vk_api.longpoll import VkEventType, VkLongPoll
import locale
from datetime import datetime
from settings import GROUP_ID, TOKEN


class NBot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.api = self.vk.get_api()
        self.longpoller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

    def write_msg(self, user_id, message, random_id):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

    def get_date(self):
        locale.setlocale(locale.LC_ALL, "ru")
        self.today = datetime.today().strftime("%A, %d.%m.%Y")
        return self.today

    def get_time(self):
        self.cur_time = datetime.now()
        self.ct = self.cur_time.strftime("%X")
        return self.ct

    def run(self):
        longpoll = VkLongPoll(self.vk)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.from_user:
                    req = event.text
                    print(f'новое событие: {req}')
                    if req == 'дата' and 'Дата':
                        self.write_msg(event.user_id, (f'текущая дата: {self.get_date()} :-*'), 0)
                        continue
                    if req == 'время' and 'Время':
                        self.write_msg(event.user_id, (f'текущее время: {self.get_time()} 8-)'), 0)
                        continue
                    elif req == 'Привет':
                        self.write_msg(event.user_id, "хай ;-) ", 0)
                        continue
                    elif req == 'Пока':
                        self.write_msg(event.user_id, 'пока :-)', 0)
                        continue
                    else:
                        self.write_msg(event.user_id, "\nЯ - бот,который подсказыает тебе текущую дату и время!"
                                                     "\nНапиши мне 'Дата' или 'Время', и я отвечу тебе)"
                                                     "\nДааа, я суперполезный :-D", 0)

if __name__ == '__main__':
    nbot = NBot(group_id=GROUP_ID, token=TOKEN)
    nbot.run()
