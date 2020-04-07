import telebot

# Начальная клавиатура
bot = telebot.TeleBot('1148414585:AAHNcAE3wct7lvvIPK4lHFosYu9nISa-nBk')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Про группу компаний', 'Связь с менеджером')
keyboard1.row('Контакты', 'Ответы на популярные вопросы')

# Клавиатура про GigaGroup
keyboard_companies = telebot.types.ReplyKeyboardMarkup(True)
keyboard_companies.row('Gigatrans', 'Gigacenter')
keyboard_companies.row('Gigacloud', 'Gigasafe')
keyboard_companies.row('Назад')

# Клавиатура про GigaTrans
keyboard_gigatrans= telebot.types.ReplyKeyboardMarkup(True)
keyboard_gigatrans.row('Послуги', 'Чому нас обирають')
keyboard_gigatrans.row('Назад')

@bot.message_handler(commands=['start'])
def start_message(message):
        print(message)
        bot.send_message(message.chat.id, 'Здравствуйте, здесь должна быть краткая информирования, что это за бот и команды', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def first_screen(message):
        if message.text.lower() == 'про группу компаний':
                msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_companies)
                bot.register_next_step_handler(msg, about_gigagroup)
        elif message.text.lower() == 'связь с менеджером':
                msg = bot.send_message(message.chat.id, 'Эта кнопка, пока еще в разработке',)
        elif message.text.lower() == 'контакты':
                msg = bot.send_message(message.chat.id, 'Наш адрес: адрес \nТелефон: телефон \nСайт: https://gigagroup.ua')
        elif message.text.lower() == 'ответы на популярные вопросы':
                msg = bot.send_message(message.chat.id, 'Выберите компанию: ', reply_markup=keyboard_companies)
        else:
                msg = bot.send_message(message.chat.id, 'Простите, я вас не понял :(')
        print(message.text)

def about_gigagroup(message):
        if message.text.lower() == 'gigatrans':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
            bot.register_next_step_handler(msg, about_gigatrans)
        elif message.text.lower() == 'gigacenter':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
        elif message.text.lower() == 'gigacloud':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
        elif message.text.lower() == 'gigasafe':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
        elif message.text.lower() == 'назад':
            msg = bot.send_message(message.chat.id,
                                   'Здравствуйте, здесь должна быть краткая информирования, что это за бот и команды',
                                   reply_markup=keyboard1)
            bot.register_next_step_handler(msg, first_screen)

        print(message.text)

def about_gigatrans(message):
    if message.text.lower() == 'послуги':
        msg = bot.send_message(message.chat.id, 'Обирайте послугу та отримуйте додаткову інформацію про неї.', reply_markup=keyboard_gigatrans)
    elif message.text.lower() == 'чому нас обирають':
        msg = bot.send_message(message.chat.id, 'Все дуже просто\n'
        '- У нас найкращі спеціалісти, які постійно вдосконалюють свої професійні навички\n'
        '- Маємо всі сертифікати якості, такі як ISO та КСЗІ\n'
        '- Наша технічна підтримка працює для вас 24/7/365\n'
        '- Для нашої команди немає нездійсненних проектів!\n'
        'Тому…\n'
        'GigaTrans – це необмежені можливості для розвитку вашого бізнесу!\n')
        bot.register_next_step_handler(msg, about_gigatrans)
    elif message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id,'Информация про групу компаний', reply_markup=keyboard_companies)
        bot.register_next_step_handler(msg, about_gigagroup)

    print(message.text)

bot.polling()