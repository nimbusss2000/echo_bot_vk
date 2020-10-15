import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.longpoll import VkEventType, VkLongPoll
import logging

try:
    from echo_bot.settings import TOKEN, GROUP_ID
except ImportError:
    exit('do cp settings.py.default settings.py and set.token!!')

log = logging.getLogger('bot')                                           # создали объект логирования
log.setLevel(logging.DEBUG)                                              # устанавливаем уровень логирования

def logg():

    stream_heandler = logging.StreamHandler()                            # выбрали тип логирования стрим
    stream_heandler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    stream_heandler.setLevel(logging.DEBUG)                              # установили ур логирования и на лог и на обработчик
    log.addHandler(stream_heandler)                                      # добавили к обработчику

    file_heandler = logging.FileHandler('bot.log', 'a','utf8')
    file_heandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    file_heandler.setLevel(logging.DEBUG)
    log.addHandler(file_heandler)

class NBot:
    """
    echo bot for vk.com
    use python 3.8
    """

    def __init__(self, group_id, token):

        """
        :param group_id: group id из группы вконтакте
        :param token: токен из группы вк
        """
        self.group_id = group_id
        self.token = token

        self.vk = vk_api.VkApi(token=token)
        self.api = self.vk.get_api()
        self.longpoller = VkBotLongPoll(self.vk, self.group_id)

    def write_msg(self, user_id, message, random_id):
        """
         отправляет текстовое сообщение обратно
        """
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

    def run(self):
        """
        запуск бота
        """
        longpoll = VkLongPoll(self.vk)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                log.info('отправляем сообщение назад')
                if event.from_user:
                    req = event.text
                    print(f'новое событие: {req}')
                    self.write_msg(event.user_id, req, 0)
            else:
                log.info(f'не можем обработать сообщение этого типа {event.type}')

if __name__ == '__main__':
    logg()
    nbot = NBot(GROUP_ID, TOKEN)
    nbot.run()
