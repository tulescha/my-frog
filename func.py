from bd import *
from token_bot import *


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
/upclass - Повысить уровень класса
'''.format(name=message.text))


@bot.message_handler(commands=['start'])
def start(message):
    if not (add_new_profile(message.chat.id)):
        rules(message)
        return
    btn = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn)
    sent = bot.send_message(message.chat.id,
                            'Привет, {0.username}. Рад тебя видеть. Вот твоя первая лягушка!'.format(
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
    frog = take_frog(message.chat.id)
    sp = [f'🐸 Имя: {message.from_user.first_name}',
          f'🍀 Здоровье: {frog[0]}',
          f'🦟 Сытость: {frog[1]}',
          f'💚 Состояние: {frog[2]}',
          f'🐞 Букашки: {frog[3]}',
          f'🛠 Класс: {frog[4]}',
          f'🚬 Настроение: {frog[5]}',
          f'💪 Сила атаки: {frog[6]}',
          f'✅ Победы: {frog[7]}',
          f'❌ Поражения: {frog[8]}']
    bot.send_message(message.chat.id, ('\n').join(sp).format(name=message.text), reply_markup=markup)


@bot.message_handler(commands=['upclass'])
def up_class(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Повысить класс")
    markup.add(btn)
    bot.send_message(message.chat.id, '''
Всего 4 класса. Ты также можешь их купить за букашек.
"Новичок": дается каждому игроку бесплатно
"Боец": 1.000 букашек
"Маг": 5.000 букашек
"Эльф": 15.000 букашек
'''.format(name=message.text), reply_markup=markup)


@bot.message_handler(commands=['feed'])
def feed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Покормить")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     '''а у нас будет что-то вроде обеда?'''.format(
                         name=message.text), reply_markup=markup)


@bot.message_handler(commands=['area'])
def area(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("В бой!")
    markup.add(btn)
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(back)
    bot.send_message(message.chat.id,
                     '''Удачи'''.format(
                         name=message.text), reply_markup=markup)
    bot.send_photo(chat_id=message.chat.id, photo=open('data/fight.png', 'rb'))


@bot.message_handler(commands=['money'])
def money(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Собрать букашек")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     '''За сегодня накопилось столько букашек: '''.format(
                         name=message.text), reply_markup=markup)


class Game:
    def __init__(self):
        self.counter10 = 0
        self.counter90 = 0

    def iterate10(self):
        self.counter10 += 1

    def iterate90(self):
        self.counter90 += 1

    def clear90(self):
        self.counter90 = 0

    def clear10(self):
        self.counter10 = 0


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
Яичница: 100 букашек, +50 к сытости, живая, настроение повышается на одну фазу

Шашлычок: 200 букашек, +100 к сытости, живая, настроение повышается на две фазы

Тортик: 500 букашек, +300 к сытости, живая, настроение повышается на 4 фазы''', reply_markup=markup)

    elif message.text == "Яичница":
        if not (feed_frog(message.chat.id, 100)):
            bot.send_message(message.chat.id, text="У вас нет букашек")
            return
        bg = 100
        count_satiety = 50
        md = 1
        take_away_bugs(message.chat.id, bg)
        satiety(message.chat.id, count_satiety)
        condition(message.chat.id)
        mood(message.chat.id, md)

    elif message.text == "Шашлычок":
        if not (feed_frog(message.chat.id, 200)):
            bot.send_message(message.chat.id, text="У вас нет букашек")
            return
        bg = 200
        count_satiety = 100
        md = 2
        take_away_bugs(message.chat.id, bg)
        satiety(message.chat.id, count_satiety)
        condition(message.chat.id)
        mood(message.chat.id, md)

    elif message.text == 'Тортик':
        if not (feed_frog(message.chat.id, 500)):
            bot.send_message(message.chat.id, text="У вас нет букашек")
            return
        bg = 500
        count_satiety = 300
        md = 4
        take_away_bugs(message.chat.id, bg)
        satiety(message.chat.id, count_satiety)
        condition(message.chat.id)
        mood(message.chat.id, md)

    elif (message.text == "Собрать букашек"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        print_list = [f'Все букашки собраны! У тебя {show_bugs(message.chat.id)} букашек!',
                      'Возвращайся в главное меню']
        bot.send_message(message.chat.id, '\n'.join(print_list).format(name=message.text),
                         reply_markup=markup)

    elif message.text == 'Повысить класс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        fighter, wizard, elf = types.KeyboardButton("🥷"), types.KeyboardButton("🧙🏻‍♂"), types.KeyboardButton("🧝")
        markup.add(fighter, wizard, elf)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, 'А денег хватит? 👺'.format(name=message.text),
                         reply_markup=markup)

    elif message.text == "🥷":
        if upclass(message.chat.id, 1000, 'Боец'):
            bot.send_message(message.chat.id, 'Блин, хватило( очень жаль, что ты боец'.format(name=message.text))
        else:
            bot.send_message(message.chat.id, 'АХАХАХАХ! Я ТАК И ЗНАЛ! ИДИ РАБОТАЙ!'.format(name=message.text))
    elif message.text == '🧙🏻‍♂':
        if upclass(message.chat.id, 5000, 'Маг'):
            bot.send_message(message.chat.id, 'Блин, хватило( очень жаль, что ты маг'.format(name=message.text))
        else:
            bot.send_message(message.chat.id, 'АХАХАХАХ! Я ТАК И ЗНАЛ! ИДИ РАБОТАЙ!'.format(name=message.text))
    elif message.text == "🧝":
        if upclass(message.chat.id, 15000, 'Эльф'):
            bot.send_message(message.chat.id, 'Блин, хватило( очень жаль, что ты эльф'.format(name=message.text))
        else:
            bot.send_message(message.chat.id, 'АХАХАХАХ! Я ТАК И ЗНАЛ! ИДИ РАБОТАЙ!'.format(name=message.text))

    elif message.text == "В бой!":
        bot.send_message(message.chat.id, 'Твой враг:'.format(name=message.text))
        heal, attack, class_enemy, enemy = get_enemy(message.chat.id)
        bot.send_message(message.chat.id, f'''
Здоровье:{heal}
Сила атаки: {attack}
Класс: {class_enemy}''')
        res_fight = fight(message.chat.id, heal, attack, enemy)
        bot.send_message(message.chat.id, res_fight)



    elif (message.text == "Начать"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Начать")
        markup.add(btn)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        a, b, c = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
        if a == b == c:
            bot.send_message(message.chat.id, f'{a} {b} {c} Вот это удача!')
            bg = 500
            result_of_game(message.chat.id, 1, 0)
            mood(message.chat.id, 3)
            gm.clear90()
        elif gm.counter90 == 50:
            bot.send_message(message.chat.id, f'{a} {b} {c} Но это гарант😳')
            bg = 500
            result_of_game(message.chat.id, 1, 0)
            mood(message.chat.id, 3)
            gm.clear90()
        else:
            if gm.counter10 == 9:
                bot.send_message(message.chat.id, f'{a} {b} {c} Довольно неплохо!')
                bg = 250
                mood(message.chat.id, 2)
                gm.clear10()
            else:
                if len(set([a, b, c])) == 2:
                    bot.send_message(message.chat.id, f'{a} {b} {c} Довольно неплохо!')
                    bg = 250
                    mood(message.chat.id, 2)
                    gm.clear10()
                else:
                    bot.send_message(message.chat.id, f'{a} {b} {c} Мда...')
                    bg = -20
                    result_of_game(message.chat.id, 0, 1)
                    mood(message.chat.id, 0)
                    gm.iterate10()
                    gm.iterate90()
        add_bugs(message.chat.id, bg)


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
            add_bugs(message.chat.id, 0)
            mood(message.chat.id, 1)
            result_of_game(message.chat.id, 0, 0)
        elif frog == '✂':
            bot.send_message(message.chat.id, text='Ты выиграл')
            add_bugs(message.chat.id, 100)
            mood(message.chat.id, 2)
            result_of_game(message.chat.id, 1, 0)
        else:
            bot.send_message(message.chat.id, text='Ты проиграл')
            add_bugs(message.chat.id, -10)
            mood(message.chat.id, -1)
            result_of_game(message.chat.id, 0, 1)
    elif (message.text == '✂'):
        frog = random.choice(rps)
        bot.send_message(message.chat.id, f'{frog}')
        if frog == '✂':
            bot.send_message(message.chat.id, text='Ничья')
            add_bugs(message.chat.id, 0)
            mood(message.chat.id, 1)
            result_of_game(message.chat.id, 0, 0)
        elif frog == '📃':
            bot.send_message(message.chat.id, text='Ты выиграл')
            add_bugs(message.chat.id, 100)
            mood(message.chat.id, 2)
            result_of_game(message.chat.id, 1, 0)
        else:
            bot.send_message(message.chat.id, text='Ты проиграл')
            add_bugs(message.chat.id, -10)
            mood(message.chat.id, -1)
            result_of_game(message.chat.id, 0, 1)
    elif (message.text == '📃'):
        frog = random.choice(rps)
        bot.send_message(message.chat.id, f'{frog}')
        if frog == '📃':
            bot.send_message(message.chat.id, text='Ничья')
            add_bugs(message.chat.id, 0)
            mood(message.chat.id, 1)
            result_of_game(message.chat.id, 0, 0)
        elif frog == '🗿':
            bot.send_message(message.chat.id, text='Ты выиграл')
            add_bugs(message.chat.id, 100)
            mood(message.chat.id, 2)
            result_of_game(message.chat.id, 1, 0)
        else:
            bot.send_message(message.chat.id, text='Ты проиграл')
            add_bugs(message.chat.id, -10)
            mood(message.chat.id, -1)
            result_of_game(message.chat.id, 0, 1)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
bot.polling()
