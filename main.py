import telebot
from telebot import types

from func import func

TOKEN = '5180182887:AAED3c25qCTsrCuSOSChSM6W_C2cTa7FkwQ'  # полученный у @BotFather

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

func()

bot.polling(none_stop=True)
bot.polling()
