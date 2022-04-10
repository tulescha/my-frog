import random

import telebot
from telebot import types  # для указание типов

TOKEN = '5180182887:AAED3c25qCTsrCuSOSChSM6W_C2cTa7FkwQ'  # полученный у @BotFather

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


@bot.message_handler(commands=['start'])
def start(message):
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn2)
    sent = bot.send_message(message.chat.id,
                            'Привет, {0.first_name}. Рад тебя видеть. Вот твоя первая лягушка!'.format(
                                message.from_user), reply_markup=markup)
    bot.send_photo(chat_id=message.chat.id, photo=open('data/start_frog.png',
                                                       'rb'))  # https://papik.pro/risunki/18647-milye-zhabki-risunki-69-foto.html
    sent = bot.send_message(message.chat.id, 'Чтобы узнать список команд, нажми на кнопку "❓ Задать вопрос"')
    # bot.register_next_step_handler(sent, rules)


@bot.message_handler(commands=['rules'])
def rules(message):
    bot.send_message(message.chat.id, '''
/rules - показать правила
/show - показать твой аккаунт с лягушкой
/feed - покормить лягушку
/money - собрать букашек
/fortune - Сыграть в рулетку
/playrps - Сыграть в камень-ножницы-бумага
/area -	Отправить лягушку на арену, где можно драться с рандомными жабами и получать награды
/shop -	Покупка дополнительных бонусов, которые используются сразу же
/upclass - Повысить уровень класса
'''.format(name=message.text))


@bot.message_handler(commands=['fortune'])
def fortune(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Начать")
    markup.add(btn)
    bot.send_message(message.chat.id, '''Это обычное казино. Здесь все "на удачу". Начнем?'''.format(name=message.text),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id,
                         '''/rules - показать правила
                         /show - показать твой аккаунт с лягушкой
                         /feed - покормить лягушку
                         /money - собрать букашек
                         /fortune - Сыграть в рулетку
                         /playrps - Сыграть в камень-ножницы-бумага
                         /area -	Отправить лягушку на арену, где можно драться с рандомными жабами и получать награды
                         /shop -	Покупка дополнительных бонусов, которые используются сразу же
                         /upclass - Повысить уровень класса'''.format(name=message.text))
    elif (message.text == "Начать"):
        a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        if a == b == c:
            bot.send_message(message.chat.id, f'''{a}{b}{c} Вот это удача!'''.format(name=message.text))
        elif len(set(a, b, c)) == 2:
            bot.send_message(message.chat.id, f'''{a}{b}{c} Довольно неплохо!'''.format(name=message.text))
        else:
            bot.send_message(message.chat.id, f'''{a}{b}{c} Мда...'''.format(name=message.text))

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
bot.polling()
