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
        screen_item = Screen(bot, message)
        screen_item.get_first_screen(mass, first_screen, False, 'Почати')

@bot.message_handler(content_types=['text'])
def first_screen(message):
        if message.text.lower() == 'про gigagroup':
                mass = list(menu['ПРО GIGAGROUP'])
                screen_item = Screen(bot, message)
                screen_item.get_current_screen(mass, about_gigagroup, True)
        elif message.text.lower() == 'связь с менеджером':
                msg = bot.send_message(message.chat.id, 'Эта кнопка, пока еще в разработке', parse_mode="Markdown")
        elif message.text.lower() == 'контакты':
                msg = bot.send_message(message.chat.id, 'Наш адрес: адрес \nТелефон: телефон \nСайт: https://gigagroup.ua', parse_mode="Markdown")
        elif message.text.lower() == 'ответы на популярные вопросы':
                msg = bot.send_message(message.chat.id, 'Выберите компанию: ', reply_markup=keyboard_companies, parse_mode="Markdown")
        else:
                screen_item = Screen(bot, message)
                screen_item.get_error_screen(first_screen)
        print(message.text)

def about_gigagroup(message):
        screen_item = Screen(bot, message)

        if message.text.lower() == 'gigatrans':
            mass = list(menu['ПРО GIGAGROUP']['GIGATRANS'])
            screen_item.get_current_screen(mass, about_gigatrans, True)
        elif message.text.lower() == 'gigacenter':
            mass = list(menu['ПРО GIGAGROUP']['GIGACENTER'])
            screen_item.get_current_screen(mass, about_gigacenter, True)
        elif message.text.lower() == 'gigacloud':
            mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD'])
            screen_item.get_current_screen(mass, about_gigacloud, True)
        elif message.text.lower() == 'gigasafe':
            msg = bot.send_message(message.chat.id, 'Информация про групу компаний', reply_markup=keyboard_gigatrans, parse_mode="Markdown")
        elif message.text.lower() == 'назад':
            mass = list(menu.keys())
            screen_item.get_previous_screen(mass, first_screen, False, 'Почати')
        else:
            screen_item.get_error_screen(about_gigagroup)

        print(message.text)

def about_gigatrans(message):
    if message.text.lower() == 'послуги':
        mass = list(menu['ПРО GIGAGROUP']['GIGATRANS']['ПОСЛУГИ'])
        screen_item = Screen(bot, message)
        screen_item.get_current_screen(mass, service_gigatrans, True)
    elif message.text.lower() == 'чому нас обирають':
        msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGATRANS'], parse_mode="Markdown")
        bot.register_next_step_handler(msg, about_gigatrans)
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP'])
        screen_item = Screen(bot, message)
        screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
    else:
        screen_item = Screen(bot, message)
        screen_item.get_error_screen(about_gigatrans)
    print(message.text)

def service_gigatrans(message):
    if message.text.lower() == 'інтернет для бізнесу':
        msg = bot.send_message(message.chat.id, dialog['ІНТЕРНЕТ ДЛЯ БІЗНЕСУ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGATRANS', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'канали передачі даних':
        msg = bot.send_message(message.chat.id, dialog['КАНАЛИ ПЕРЕДАЧІ ДАНИХ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGATRANS', 'КАНАЛИ ПЕРЕДАЧІ ДАНИХ')
    elif message.text.lower() == 'ір-телефонія та віртуальна атс':
        msg = bot.send_message(message.chat.id, dialog['ІР-ТЕЛЕФОНІЯ ТА ВІРТУАЛЬНА АТС'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGATRANS', 'ІР-ТЕЛЕФОНІЯ ТА ВІРТУАЛЬНА АТС')
    elif message.text.lower() == 'захист від ddos-атак':
        msg = bot.send_message(message.chat.id, dialog['ЗАХИСТ ВІД DDoS-АТАК'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGATRANS', 'ЗАХИСТ ВІД DDoS-АТАК')
    elif message.text.lower() == 'міжоператорський бізнес':
        msg = bot.send_message(message.chat.id, dialog['МІЖОПЕРАТОРСЬКИЙ БІЗНЕС'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGATRANS', 'ЗАХИСТ ВІД DDoS-АТАК')
    elif message.text.lower() == 'будівництво волз':
        msg = bot.send_message(message.chat.id, dialog['БУДІВНИЦТВО ВОЛЗ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGATRANS', 'БУДІВНИЦТВО ВОЛЗ')
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP']['GIGATRANS'])
        screen_item = Screen(bot, message)
        screen_item.get_previous_screen(mass, about_gigatrans, True, 'GIGATRANS')
    else:
        screen_item = Screen(bot, message)
        screen_item.get_error_screen(service_gigatrans)

def about_gigacenter(message):
    if message.text.lower() == 'послуги':
        mass = list(menu['ПРО GIGAGROUP']['GIGACENTER']['ПОСЛУГИ'])
        screen_item = Screen(bot, message)
        screen_item.get_current_screen(mass, service_gigacenter, True)
    elif message.text.lower() == 'чому нас обирають':
        msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGACENTER'], parse_mode="Markdown")
        bot.register_next_step_handler(msg, about_gigacenter)
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP'])
        screen_item = Screen(bot, message)
        screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
    else:
        screen_item = Screen(bot, message)
        screen_item.get_error_screen(about_gigacenter)
    print(message.text)

def service_gigacenter(message):
    if message.text.lower() == 'по-юнітне розміщення':
        msg = bot.send_message(message.chat.id, dialog['ПО-ЮНІТНЕ РОЗМІЩЕННЯ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACENTER', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'оренда 1/2 серверної шафи':
        msg = bot.send_message(message.chat.id, dialog['ОРЕНДА 1/2 СЕРВЕРНОЇ ШАФИ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACENTER', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'оренда серверної шафи':
        msg = bot.send_message(message.chat.id, dialog['ОРЕНДА СЕРВЕРНОЇ ШАФИ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACENTER', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'оренда модуля':
        msg = bot.send_message(message.chat.id, dialog['ОРЕНДА МОДУЛЯ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACENTER', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'оренда екранованої шафи':
        msg = bot.send_message(message.chat.id, dialog['ОРЕНДА ЕКРАНОВАНОЇ ШАФИ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACENTER', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP']['GIGACENTER'])
        screen_item = Screen(bot, message)
        screen_item.get_previous_screen(mass, about_gigacenter, True, 'GIGACENTER')
    else:
        screen_item = Screen(bot, message)
        screen_item.get_error_screen(service_gigacenter)

def about_gigacloud(message):
    if message.text.lower() == 'послуги':
        mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD']['ПОСЛУГИ'])
        screen_item = Screen(bot, message)
        screen_item.get_current_screen(mass, service_gigacloud, True)
    elif message.text.lower() == 'чому нас обирають':
        msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGACLOUD'], parse_mode="Markdown")
        bot.register_next_step_handler(msg, about_gigacloud)
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP'])
        screen_item = Screen(bot, message)
        screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
    else:
        screen_item = Screen(bot, message)
        screen_item.get_error_screen(about_gigacloud)
    print(message.text)

def service_gigacloud(message):
    if message.text.lower() == 'private cloud':
        msg = bot.send_message(message.chat.id, dialog['PRIVATE CLOUD'], reply_markup=keyboard_service_order, parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACLOUD', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'public cloud':
        msg = bot.send_message(message.chat.id, dialog['PUBLIC CLOUD'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACLOUD', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'кластери kubernetes':
        msg = bot.send_message(message.chat.id, dialog['КЛАСТЕРИ KUBERNETES'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACLOUD', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'draas':
        msg = bot.send_message(message.chat.id, dialog['DRaaS'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACLOUD', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'baas':
        msg = bot.send_message(message.chat.id, dialog['BaaS'], reply_markup=keyboard_service_order,parse_mode="Markdown")
        bot.register_next_step_handler(msg, service_order, 'GIGACLOUD', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
    elif message.text.lower() == 'назад':
        mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD'])
        screen_item = Screen(bot, message)
        screen_item.get_previous_screen(mass, about_gigacenter, True, 'GIGACLOUD')
    else:
        screen_item = Screen(bot, message)
        screen_item.get_error_screen(service_gigacloud)


def service_order(message, company, service):
    print(company)
    if company == 'GIGATRANS':
        if message.text.lower() == 'замовити послугу':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item = Screen(bot, message)
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            mass = list(menu['ПРО GIGAGROUP']['GIGATRANS']['ПОСЛУГИ'])
            screen_item = Screen(bot, message)
            screen_item.get_previous_screen(mass, service_gigatrans, True, 'ПОСЛУГИ')
    elif company == 'GIGACENTER':
        if message.text.lower() == 'замовити послугу':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item = Screen(bot, message)
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            mass = list(menu['ПРО GIGAGROUP']['GIGACENTER']['ПОСЛУГИ'])
            screen_item = Screen(bot, message)
            screen_item.get_previous_screen(mass, service_gigacenter, True, 'ПОСЛУГИ GIGACENTER')
    elif company == 'GIGACLOUD':
        if message.text.lower() == 'замовити послугу':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item = Screen(bot, message)
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD']['ПОСЛУГИ'])
            screen_item = Screen(bot, message)
            screen_item.get_previous_screen(mass, service_gigacloud, True, 'ПОСЛУГИ')


bot.polling()