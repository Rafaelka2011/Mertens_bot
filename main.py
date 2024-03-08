import config

import telebot

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi, I am Mertnes_bot created by Mamiev Raphael.I am glad to welcome you! At your service, Mertens_bot.\
""")

@bot.message_handler(commands=['how_are_you?'])
def send_welcome(message):
    bot.reply_to(message, """\
I am fine, thanks\
""")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, """\
— Ну ладно, зачем дракону именно девственница, можно понять. А вот почему девица должна быть самой красивой? Дракону не все равно какой формы мясо жрать?
— А чтоб не стыдно было свою еду в соцсеть выложить.\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()

