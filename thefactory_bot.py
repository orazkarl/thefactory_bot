import telebot
bot = telebot.TeleBot('1088972154:AAH10CkfPAvkK22dJxx-ILrl-qUvtY6LRDo')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/yourid')
    bot.send_message(message.from_user.id, text='hello', reply_markup=user_markup)


@bot.message_handler(commands=['yourid'])
def handle_token(message):
    bot.send_message(message.from_user.id, text='Your Telegram User ID: ' + str(message.from_user.id))

bot.polling(none_stop=True)
