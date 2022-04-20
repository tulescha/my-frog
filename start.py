from token_bot import *
@bot.message_handler(commands=['start'])
def start(message):
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn2)
    sent = bot.send_message(message.chat.id,
                            'Привет, {0.first_name}. Рад тебя видеть. Вот твоя первая лягушка!'.format(
                                message.from_user), reply_markup=markup)
    bot.send_photo(chat_id=message.chat.id, photo=open('data/start_frog.png', 'rb'))
    # https://papik.pro/risunki/18647-milye-zhabki-risunki-69-foto.html
    sent = bot.send_message(message.chat.id, 'Чтобы узнать список команд, нажми на кнопку "❓ Задать вопрос"')