import telebot

bot = telebot.TeleBot('1148414585:AAHNcAE3wct7lvvIPK4lHFosYu9nISa-nBk')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Про группу компаний', 'Связь с менеджером')
keyboard1.row('Контакты', 'Ответы на популярные вопросы')

keyboard2 = telebot.types.InlineKeyboardMarkup()
key_gigatrans = telebot.types.InlineKeyboardButton(text='Gigatrans', callback_data='gigatans')
keyboard2.add(key_gigatrans)
key_gigacenter = telebot.types.InlineKeyboardButton(text='Gigacenter', callback_data='gigacenter')
keyboard2.add(key_gigacenter)

keyboard3 = telebot.types.InlineKeyboardMarkup()
key_company = telebot.types.InlineKeyboardButton(text='Компания', callback_data='gigatans_company')
keyboard3.add(key_company)
key_service = telebot.types.InlineKeyboardButton(text='Услуги', url="https://gigatrans.ua/ru/services")
keyboard3.add(key_service)

@bot.message_handler(commands=['start'])
def start_message(message):
        print(message)
        bot.send_message(message.chat.id, 'Здравствуйте, здесь должна быть краткая информирования, что это за бот и команды', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
        if message.text.lower() == 'про группу компаний':
                bot.send_message(message.chat.id, 'Информация про групу компаний')
        elif message.text.lower() == 'связь с менеджером':
                bot.send_message(message.chat.id, 'Эта кнопка, пока еще в разработке')
        elif message.text.lower() == 'контакты':
                bot.send_message(message.chat.id, 'Наш адрес: адрес \nТелефон: телефон \nСайт: https://gigagroup.ua ')
        elif message.text.lower() == 'ответы на популярные вопросы':
                print(message)
                bot.send_message(message.chat.id, 'Выберите компанию: ',reply_markup=keyboard2)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "gigatans": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Разделы компании Gigatrans', reply_markup=keyboard3)
    elif call.data == "gigatans_company":
        bot.send_message(call.message.chat.id, 'Тут информация о компании')

bot.polling()