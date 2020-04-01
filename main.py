import telebot

bot = telebot.TeleBot('1148414585:AAHNcAE3wct7lvvIPK4lHFosYu9nISa-nBk')

@bot.message_handler(commands=['start'])
def start_message(message):
        print(message)
        bot.send_message(message.chat.id, 'Здравствуйте, здесь должна быть краткая информирования, что это за бот и команды', reply_markup=keyboard1)

bot.polling()