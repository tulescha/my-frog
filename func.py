import random

from token_bot import *


@bot.message_handler(commands=['start'])
def start(message):
    btn = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn)
    sent = bot.send_message(message.chat.id,
                            'Привет, {0.first_name}. Рад тебя видеть. Вот твоя первая лягушка!'.format(
                                message.from_user), reply_markup=markup)
    num_foto = random.randint(1, 4)
    if num_foto == 1:
        bot.send_photo(chat_id=message.chat.id, photo=open('data/start_frog.png', 'rb'))
    elif num_foto == 2:
        bot.send_photo(chat_id=message.chat.id, photo=open('data/start_frog2.jpg', 'rb'))
    elif num_foto == 3:
        bot.send_photo(chat_id=message.chat.id, photo=open('data/start_frog3.jpg', 'rb'))
    else:
        bot.send_photo(chat_id=message.chat.id, photo=open('data/start_frog4.jpg', 'rb'))
    sent = bot.send_message(message.chat.id, 'Чтобы узнать список команд, нажми на кнопку "❓ Задать вопрос"')


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


@bot.message_handler(commands=['playrps'])
def fortune(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("🗿✂📃")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     '''Это всего лишь "камень-ножницы-бумага". Здесь все "на удачу". Начнем?'''.format(
                         name=message.text), reply_markup=markup)


@bot.message_handler(commands=['show'])
def show(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(back)
    bot.send_message(message.chat.id, '''
Имя:Kva
Сытость: 78
Состояние: 90
Букашки: 23
Класс: 3
Настроение: ок
Победы: 45
Поражения: 34'''.format(
        name=message.text), reply_markup=markup)


@bot.message_handler(commands=['feed'])
def feed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Покормить")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     '''а у нас будет что-то вроде обеда?'''.format(
                         name=message.text), reply_markup=markup)


@bot.message_handler(commands=['money'])
def money(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Собрать букашек")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     '''За сегодня накопилось столько букашек:'''.format(
                         name=message.text), reply_markup=markup)


class Game:
    def __init__(self):
        self.counter = 0

    def iterate(self):
        self.counter += 1

    def clear(self):
        self.counter = 0

gm = Game()

@bot.message_handler(content_types=['text'])
def func(message):
    rps = ['🗿', '✂', '📃']
    if (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, '''
/rules - показать правила
/show - показать твой аккаунт с лягушкой
/feed - покормить лягушку
/money - собрать букашек
/fortune - Сыграть в рулетку
/playrps - Сыграть в камень-ножницы-бумага
/area -	Отправить лягушку на арену, где можно драться с рандомными жабами и получать награды
/upclass - Повысить уровень класса'''.format(name=message.text))

    elif message.text == "Покормить":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        eggs = types.KeyboardButton("Яичница")
        meat = types.KeyboardButton("Шашлычок")
        cake = types.KeyboardButton("Тортик")
        markup.add(eggs, meat, cake)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text='''
У нас есть несколько блюд:
Яичница: 100 букашек, +50 к сытости, +30 к состоянию, настроение повышается на одну фазу
Шашлычок: 200 букашек, +100 к сытости, +50 к состоянию, настроение повышается на две фазы
Тортик: 500 букашек, +300 к сытости, +150 к состоянию, настроение повышается на 4 фазы''', reply_markup=markup)
    elif (message.text == "Собрать букашек"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Все букашки собраны! У тебя х букашек! Возвращайся в главное меню'.format(name=message.text),
                         reply_markup=markup)
    elif (message.text == "Начать"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Начать")
        markup.add(btn)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Если хочешь закончить, то нажми "Вернуться в главное меню"'.format(name=message.text),
                         reply_markup=markup)

        count_guarantee90 = []
        a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        if a == b == c:
            bot.send_message(message.chat.id, f'{a} {b} {c} Вот это удача!')
            count_guarantee90 = []
        elif len(count_guarantee90) == 15:
            bot.send_message(message.chat.id, f'{a} {b} {c} Это гарант😳')
            count_guarantee90 = []
        else:
            if gm.counter == 9:
                bot.send_message(message.chat.id, f'{a} {b} {c} Довольно неплохо!')
                gm.clear()
            else:
                if len(set([a, b, c])) == 2:
                    bot.send_message(message.chat.id, f'{a} {b} {c} Довольно неплохо!')
                    gm.clear()
                else:
                    bot.send_message(message.chat.id, f'{a} {b} {c} Мда...')
                    gm.iterate()
            count_guarantee90.append(1)
        print('fewjo',count_guarantee90)


    elif (message.text == "🗿✂📃"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        rock, paper, scissors = types.KeyboardButton("🗿"), types.KeyboardButton("📃"), types.KeyboardButton("✂")
        markup.add(rock, paper, scissors)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id,
                         'Если хочешь закончить, то нажми "Вернуться в главное меню"'.format(name=message.text),
                         reply_markup=markup)

    elif (message.text == "🗿"):
        frog = random.choice(rps)
        bot.send_message(message.chat.id, f'{frog}')
        if frog == "🗿":
            bot.send_message(message.chat.id, text='Ничья')
        elif frog == '✂':
            bot.send_message(message.chat.id, text='Ты выиграл')
        else:
            bot.send_message(message.chat.id, text='Ты проиграл')
    elif (message.text == '✂'):
        frog = random.choice(rps)
        bot.send_message(message.chat.id, f'{frog}')
        if frog == '✂':
            bot.send_message(message.chat.id, text='Ничья')
        elif frog == '📃':
            bot.send_message(message.chat.id, text='Ты выиграл')
        else:
            bot.send_message(message.chat.id, text='Ты проиграл')
    elif (message.text == '📃'):
        frog = random.choice(rps)
        bot.send_message(message.chat.id, f'{frog}')
        if frog == '📃':
            bot.send_message(message.chat.id, text='Ничья')
        elif frog == '🗿':
            bot.send_message(message.chat.id, text='Ты выиграл')
        else:
            bot.send_message(message.chat.id, text='Ты проиграл')

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
bot.polling()
