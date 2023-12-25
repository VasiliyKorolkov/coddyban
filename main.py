import vk_api
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType

TOKEN='vk1.a.V7P_kbAYWKcaGSTF4dzX_zL265ydoWn6o7ebhTMRe-lAAgTq70H8JENisjoo6Q8jGJkQRlgNMio87-jE7D-iqLeXqW_sclxXrkcXAvMNyxhJpY2yECwA1rpxBN4r2OCj_EUUeaaBAsOxIISUBHBO9u0S_xhfVyaxU07Xhp0TMZ6636tkliVO9_SSmZZbcv5g4Q54_eBn5kpZStjfsWTHLQ'
vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

vars = ['камень','ножницы','бумага']
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.text.lower() in vars:
        bot = choice(vars)
        if event.from_user:
            vk.messages.send(user_id=event.user_id,message=bot, random_id=randrange(1,100000))
            if bot == 'ножницы':
                if event.text.lower() =='ножницы':
                    user = 'ничья. Это печально.'
                elif event.text.lower() == 'камень':
                    user = 'ты победил! Но я отыграюсь'
                else:
                    user = 'ты проиграл, лузер!'
            elif bot =='бумага':
                if event.text.lower() =='ножницы':
                    user = 'Ты победил! Но я отыграюсь'
                elif event.text.lower() == 'камень':
                    user = 'Ты проиграл, лузер!'
                else:
                    user = 'ничья. Это печально.'
            else:
                if event.text.lower() =='ножницы':
                    user = 'Ты проиграл, лузер!'
                elif event.text.lower() == 'камень':
                    user = 'ничья. Это печально.'
                else:
                    user = 'Ты победил! Но я отыграюсь'
            vk.messages.send(user_id=event.user_id,message=user,random_id=randrange(1,100000))

