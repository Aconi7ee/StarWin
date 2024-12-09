import telebot
from telebot import types

bot = telebot.Telebot("token")

web_app_url = "https://aconi7ee.github.io/StarWin/"

text = "Bet stars and win ⭐️"

button = types.InlineKeyboardButton('Open', url=web_app_url)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)

@button.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text=text,
    reply_markup=keyboard)

    bot.polling()