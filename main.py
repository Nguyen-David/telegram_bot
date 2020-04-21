import telebot
from config import create_menu, Screen
from menu import menu
from dialog import dialog
import db_users

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

markdown = """
    *bold text*
    _italic text_
    [text](URL)
    """

@bot.message_handler(commands=['start'])
def start_message(message):
        db_users.add_user(message)
        print(message)
        mass = list(menu.keys())
        markup = create_menu(mass, back=False)
        bot.send_message(message.chat.id, dialog['Почати'], reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def first_screen(message):
        if message.text.lower() == 'про gigagroup':
                screen_item = Screen(bot, message)
                screen_item.get_current_screen(about_gigagroup, True)
        elif message.text.lower() == 'связь с менеджером':
                msg = bot.send_message(message.chat.id, 'Эта кнопка, пока еще в разработке', parse_mode="Markdown")
        elif message.text.lower() == 'контакты':
                msg = bot.send_message(message.chat.id, 'Наш адрес: адрес \nТелефон: телефон \nСайт: https://gigagroup.ua', parse_mode="Markdown")
        elif message.text.lower() == 'ответы на популярные вопросы':
                msg = bot.send_message(message.chat.id, 'Выберите компанию: ', reply_markup=keyboard_companies, parse_mode="Markdown")
        else:
                msg = bot.send_message(message.chat.id, 'Простите, я вас не понял :(', parse_mode="Markdown")
        print(message.text)

def about_gigagroup(message):
        if message.text.lower() == 'gigatrans':
            mass = list(menu['ПРО GIGAGROUP']['GIGATRANS'].keys())
            markup = create_menu(mass, back=True)
            msg = bot.send_message(message.chat.id, dialog['GIGATRANS'], reply_markup=markup, parse_mode="Markdown")
            bot.register_next_step_handler(msg, about_gigatrans)
        elif message.text.lower() == 'gigacenter':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans, parse_mode="Markdown")
        elif message.text.lower() == 'gigacloud':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans, parse_mode="Markdown")
        elif message.text.lower() == 'gigasafe':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans, parse_mode="Markdown")
        elif message.text.lower() == 'назад':
            mass = list(menu.keys())
            markup = create_menu(mass, back=False)
            msg = bot.send_message(message.chat.id, dialog['Почати'], reply_markup=markup, parse_mode="Markdown")
            bot.register_next_step_handler(msg, first_screen)
        else:
            msg = bot.send_message(message.chat.id, 'Простите, я вас не понял :(', parse_mode="Markdown")
        print(message.text)

def about_gigatrans(message):
    if message.text.lower() == 'послуги':
        mass = list(menu['ПРО GIGAGROUP']['GIGATRANS']['ПОСЛУГИ'])
        markup = create_menu(mass, back=True)
        msg = bot.send_message(message.chat.id, dialog['ПОСЛУГИ'], reply_markup=keyboard_service_gigatrans, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_gigatrans)
    elif message.text.lower() == 'чому нас обирають':
        msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ'], parse_mode="Markdown")
        bot.register_next_step_handler(msg, about_gigatrans)
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP'].keys())
        markup = create_menu(mass, back=True)
        msg = bot.send_message(message.chat.id, dialog['ПРО GIGAGROUP'], reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(msg, about_gigagroup)
    else :
        msg = bot.send_message(message.chat.id, 'Простите, я вас не понял :(', parse_mode="Markdown")
    print(message.text)

def service_gigatrans(message):
    if message.text.lower() == 'інтернет для бізнесу':
        msg = bot.send_message(message.chat.id, dialog['ІНТЕРНЕТ ДЛЯ БІЗНЕСУ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'канали передачі даних':
        msg = bot.send_message(message.chat.id, '   Ви можете створити свою внутрішню комунікаційну інфраструктуру із допомогою фахівців GigaTrans. Така мережа доступна для обєднання різних підрозділів або філій компанії клієнта (незалежно від їх кількості).Переваги:'
            '- Висока швидкість передачі інформації\n'
            '- Інформація захищена від несанкціонованого доступу\n'
            '- Несприйнятливість до електромагнітних наведень\n'
            '- Стійкість до агресивних середовищ\n'
            '- Гнучкість оптичних волокон\n'
            '- Можливість прокладки кабелю на великі відстані\n',
                               reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'ір-телефонія та віртуальна атс':
        msg = bot.send_message(message.chat.id,'    IP-телефонія - технологія, яка обєднує в собі переваги телефонії та мережі Інтернет. Переваги послуги:'
            '- Внутрішні короткі номери'
            '- Підключаємо будь-яке обладнання'
            '- Інтерактивне голосове меню'
            '- Послуга 0-800'
            '- Багатоканальні номери'
            '- Маршрутизація дзвінків',
                               reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, '   Телеком-оператор GigaTrans заснований у 2006 році. Ми надаємо послуги доступу до мережі Інтернет з захищеним вузлом інтернет доступу (ЗВІД) і організації каналів передачі даних для корпоративних клієнтів. З нами ви отримаєте:'
            '- Необмежений швидкісний інтернет;\n'
            '- Включення в міжнародну точку обміну трафіком DECIX;\n'
            '- Виділені канали передачі даних та захищений вузол інтернет-зв’язку (КСЗІ);\n'
            'GigaTrans – це необмежені можливості для розвитку вашого бізнесу!\n',
                               reply_markup=keyboard_companies, parse_mode="Markdown")
        bot.register_next_step_handler(msg, about_gigatrans)


def service_order(message):
    if message.text.lower() == 'замовити послугу':
        msg = bot.send_message(message.chat.id, 'Залиште свої контакти і наш менеджер вам зателефонує протягом години!', reply_markup=keyboard_gigatrans, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order)
    elif message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Обирайте послугу та отримуйте додаткову інформацію про неї.',
                               reply_markup=keyboard_service_gigatrans, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_gigatrans)

bot.polling()