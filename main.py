import telebot

# Начальная клавиатура
bot = telebot.TeleBot('1148414585:AAHNcAE3wct7lvvIPK4lHFosYu9nISa-nBk')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('ПРО GIGAGROUP', 'Связь с менеджером')
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

# Клавиатура услуг Gigatrans
keyboard_service_gigatrans= telebot.types.ReplyKeyboardMarkup(True)
keyboard_service_gigatrans.row('ІНТЕРНЕТ ДЛЯ БІЗНЕСУ', 'КАНАЛИ ПЕРЕДАЧІ ДАНИХ ')
keyboard_service_gigatrans.row('ІР-ТЕЛЕФОНІЯ ТА ВІРТУАЛЬНА АТС', 'ЗАХИСТ ВІД DDoS-АТАК')
keyboard_service_gigatrans.row('МІЖОПЕРАТОРСЬКИЙ БІЗНЕС', 'БУДІВНИЦТВО ВОЛЗ')
keyboard_service_gigatrans.row('Назад')

# Клавиатура заказа услуги
keyboard_service_order= telebot.types.ReplyKeyboardMarkup(True)
keyboard_service_order.row('Замовити послугу')
keyboard_service_order.row('Назад')


@bot.message_handler(commands=['start'])
def start_message(message):
        print(message)
        bot.send_message(message.chat.id, 'Супер, тепер ти з нами :) Тут ти знайдешь відповіді на свої запитання та зможеш зєднатися з менеджером у разі виникнення додаткових питань. Починаємо!', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def first_screen(message):
        if message.text.lower() == 'про gigagroup':
                msg = bot.send_message(message.chat.id, '   GIGAGROUP існує на ринку телекомунікаційних послуг більше 13 років  та представляє собою синергію масштабних ІТ-рішень: телеком-оператор GigaTrans, дата-центр GigaCenter, хмарний оператор GigaCloud та агент з кібербезпеки GigaSafe. Все для надійного зберігання, передачі та резервування ваших даних.', reply_markup=keyboard_companies)
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
            msg = bot.send_message(message.chat.id, '   Телеком-оператор GigaTrans заснований у 2006 році. Ми надаємо послуги доступу до мережі Інтернет з захищеним вузлом інтернет доступу (ЗВІД) і організації каналів передачі даних для корпоративних клієнтів. З нами ви отримаєте:'
            '- Необмежений швидкісний інтернет;\n'
            '- Включення в міжнародну точку обміну трафіком DECIX;\n'
            '- Виділені канали передачі даних та захищений вузол інтернет-зв’язку (КСЗІ);\n'
            'GigaTrans – це необмежені можливості для розвитку вашого бізнесу!\n'
            , reply_markup=keyboard_gigatrans)
            bot.register_next_step_handler(msg, about_gigatrans)
        elif message.text.lower() == 'gigacenter':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
        elif message.text.lower() == 'gigacloud':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
        elif message.text.lower() == 'gigasafe':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans)
        elif message.text.lower() == 'назад':
            msg = bot.send_message(message.chat.id,
                                   '    Супер, тепер ти з нами :) Тут ти знайдешь відповіді на свої запитання та зможеш зєднатися з менеджером у разі виникнення додаткових питань. ',
                                   reply_markup=keyboard1)
            bot.register_next_step_handler(msg, first_screen)

        print(message.text)

def about_gigatrans(message):
    if message.text.lower() == 'послуги':
        msg = bot.send_message(message.chat.id, '   Обирайте послугу та отримуйте додаткову інформацію про неї.', reply_markup=keyboard_service_gigatrans)
        bot.register_next_step_handler(msg, service_gigatrans)
    elif message.text.lower() == 'чому нас обирають':
        msg = bot.send_message(message.chat.id, '   Все дуже просто\n'
        '- У нас найкращі спеціалісти, які постійно вдосконалюють свої професійні навички\n'
        '- Маємо всі сертифікати якості, такі як ISO та КСЗІ\n'
        '- Наша технічна підтримка працює для вас 24/7/365\n'
        '- Для нашої команди немає нездійсненних проектів!\n'
        'Тому…\n'
        'GigaTrans – це необмежені можливості для розвитку вашого бізнесу!\n')
        bot.register_next_step_handler(msg, about_gigatrans)
    elif message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, '   GIGAGROUP існує на ринку телекомунікаційних послуг більше 13 років  та представляє собою синергію масштабних ІТ-рішень: телеком-оператор GigaTrans, дата-центр GigaCenter, хмарний оператор GigaCloud та агент з кібербезпеки GigaSafe. Все для надійного зберігання, передачі та резервування ваших даних.', reply_markup=keyboard_companies)
        bot.register_next_step_handler(msg, about_gigagroup)

    print(message.text)

def service_gigatrans(message):
    if message.text.lower() == 'інтернет для бізнесу':
        msg = bot.send_message(message.chat.id, '   Переваги послуги Інтернет від GigaTrans для бізнесу:\n'

            ' - Максимальна швидкість до 100 Гбіт/с \n'
            '- Сервіс і підтримка 24/7/365 \n'
            '- Гарантія якості SLA 99,5%,ISO 27001:2013 та атестат КСЗІ \n'
            '- З нами вже 1000+ партнерів \n'
            '- Підключення в точку обміну трафіком DECIX \n'
            '- UA-IX і GigaNet \n',
                               reply_markup=keyboard_service_order)
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'канали передачі даних':
        msg = bot.send_message(message.chat.id, '   Ви можете створити свою внутрішню комунікаційну інфраструктуру із допомогою фахівців GigaTrans. Така мережа доступна для обєднання різних підрозділів або філій компанії клієнта (незалежно від їх кількості).Переваги:'
            '- Висока швидкість передачі інформації\n'
            '- Інформація захищена від несанкціонованого доступу\n'
            '- Несприйнятливість до електромагнітних наведень\n'
            '- Стійкість до агресивних середовищ\n'
            '- Гнучкість оптичних волокон\n'
            '- Можливість прокладки кабелю на великі відстані\n',
                               reply_markup=keyboard_service_order)
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'ір-телефонія та віртуальна атс':
        msg = bot.send_message(message.chat.id,'    IP-телефонія - технологія, яка обєднує в собі переваги телефонії та мережі Інтернет. Переваги послуги:'
            '- Внутрішні короткі номери'
            '- Підключаємо будь-яке обладнання'
            '- Інтерактивне голосове меню'
            '- Послуга 0-800'
            '- Багатоканальні номери'
            '- Маршрутизація дзвінків',
                               reply_markup=keyboard_service_order)
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, '   Телеком-оператор GigaTrans заснований у 2006 році. Ми надаємо послуги доступу до мережі Інтернет з захищеним вузлом інтернет доступу (ЗВІД) і організації каналів передачі даних для корпоративних клієнтів. З нами ви отримаєте:'
            '- Необмежений швидкісний інтернет;\n'
            '- Включення в міжнародну точку обміну трафіком DECIX;\n'
            '- Виділені канали передачі даних та захищений вузол інтернет-зв’язку (КСЗІ);\n'
            'GigaTrans – це необмежені можливості для розвитку вашого бізнесу!\n',
                               reply_markup=keyboard_companies)
        bot.register_next_step_handler(msg, about_gigatrans)


def service_order(message):
    if message.text.lower() == 'замовити послугу':
        msg = bot.send_message(message.chat.id, 'Залиште свої контакти і наш менеджер вам зателефонує протягом години!', reply_markup=keyboard_gigatrans)
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Обирайте послугу та отримуйте додаткову інформацію про неї.',
                               reply_markup=keyboard_service_gigatrans)
        bot.register_next_step_handler(msg, service_gigatrans)


bot.polling()