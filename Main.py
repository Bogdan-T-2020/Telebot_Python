import telebot
from telebot import types

bot = telebot.TeleBot("1261684826:AAGoDmg2G0plkHccSH6v1PgEdt43Im6gftY")


def menu():
    glavmenu = types.InlineKeyboardMarkup(row_width=1)


@bot.message_handler(commands=['start'])
def startpg(message):
    startmenu = types.ReplyKeyboardMarkup(True, False)
    startmenu.row('О нас', 'Менеджеры')
    startmenu.row('Наш Телеграм канал с отзывами')
    bot.send_message(message.chat.id,
                     'Привет\nты попал на бота магазина "The Шмот УКРАИНА"\nтут ты найдешь информацию о нас и об обратной связи',
                     reply_markup=startmenu)


@bot.message_handler(content_types=['text'])
def osnov(message):
    if message.text == 'О нас':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('О нас', 'Менеджеры')
        back.row('Наш Телеграм канал с отзывами')
        bot.send_message(message.chat.id, 'Привет странник телеграма'
'Тут собрались люди которые ресейлят вещи из Секонд-Хенда \n \n'

'(Также иногда будут всплывать вещи с чеками взятые у покупателя с оригинального магазина) \n \n'

'Если есть свой шмот на продажу пиши, не стесняйся'
'( Процент от продажи будет невелик ) \n \nПриводи друзей новым людям мы всегда рады \n'

'Так что покупай шмот и радуйся жизни. 😘',
                         reply_markup=back)

    elif message.text == 'Менеджеры':
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('О нас', 'Менеджеры')
        back.row('Наш Телеграм канал с отзывами')
        bot.send_message(message.chat.id, 'Менеджер Богдан\n@Bohdan_Bykov\nМенеджер Кирилл\n@Go_1x1_lalka',
                         reply_markup=back)

    elif message.text == "Наш Телеграм канал с отзывами":
        back = types.ReplyKeyboardMarkup(True, False)
        back.row('О нас', 'Менеджеры')
        back.row('Наш Телеграм канал с отзывами')
        bot.send_message(message.chat.id, 'Дружише лови ссылку\nhttps://t.me/joinchat/IEzG1BN3PRfEA03T9DRMAQ',
                         reply_markup=back)

bot.polling(none_stop=False, interval=0, timeout=20)
