import telebot
from config import Screen, bot, markdown
from menu import menu, inline_menu
from dialog import dialog
import db_users

# Клавиатура заказа услуги
keyboard_service_order = telebot.types.ReplyKeyboardMarkup(True)
keyboard_service_order.row('Замовити послугу')
keyboard_service_order.row('⬅️Назад')


@bot.message_handler(commands=['start'])
def start_message(message):
        db_users.add_user(message)
        print(message)
        mass = list(menu.keys())
        screen_item = Screen(bot, message)
        screen_item.get_first_screen(mass, first_screen, False, 'Почати')


@bot.message_handler(content_types=['text', 'contact', 'audio', 'document', 'photo', 'sticker',
                                    'video', 'video_note', 'voice', 'location', 'new_chat_members',
                                    'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
                                    'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                                    'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def first_screen(message):
        screen_item = Screen(bot, message)
        try:
            if message.text.lower() == 'про gigagroup':
                mass = list(menu['ПРО GIGAGROUP'])
                screen_item.get_current_screen(mass, about_gigagroup, True)
            elif message.text.lower() == 'топ-послуги 🏆':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_current_screen(mass, top_service, True)
            elif message.text.lower() == 'підключити менеджера ✍️':
                screen_item.get_add_manager_screen(add_manager)
            elif message.text.lower() == '📩 контакти 📞':
                screen_item.get_recursive_screen(first_screen)
            elif message.text.lower() == 'найпопулярніші питання':
                mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
                screen_item.get_current_screen(mass, top_question, True)
            elif message.text.lower() == 'кар\'єра':
                screen_item.get_recursive_screen(first_screen)
            elif message.text.lower() == 'повернутися до питань':
                mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
                screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
            else:
                mass = list(menu.keys())
                screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')
            print(message.text)
        except Exception:
            print('Ошибка формата')
            mass = list(menu.keys())
            screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def about_gigagroup(message):
        screen_item = Screen(bot, message)
        try:
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
                mass = list(menu['ПРО GIGAGROUP']['GIGASAFE'])
                screen_item.get_current_screen(mass, about_gigasafe, True)
            elif message.text.lower() == 'повернутися до питань':
                mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
                screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
            elif message.text.lower() == '⬅️назад':
                mass = list(menu.keys())
                screen_item.get_previous_screen(mass, first_screen, False, 'Почати')
            else:
                screen_item.get_error_screen(about_gigagroup)

            print(message.text)
        except Exception:
            print('Ошибка формата')
            mass = list(menu.keys())
            screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def about_gigatrans(message):
    screen_item = Screen(bot, message)

    try:
        if message.text.lower() == 'послуги':
            mass = list(menu['ПРО GIGAGROUP']['GIGATRANS']['ПОСЛУГИ'])
            screen_item.get_current_screen(mass, service_gigatrans, True)
        elif message.text.lower() == 'чому нас обирають':
            msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGATRANS'], parse_mode="Markdown")
            bot.register_next_step_handler(msg, about_gigatrans)
        elif message.text.lower() == 'повернутися до питань':
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            screen_item.get_error_screen(about_gigatrans)
        print(message.text)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def service_gigatrans(message):
    screen_item = Screen(bot, message)

    try:
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
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP']['GIGATRANS'])
            screen_item.get_previous_screen(mass, about_gigatrans, True, 'GIGATRANS')
        else:
            screen_item.get_error_screen(service_gigatrans)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def about_gigacenter(message):
    screen_item = Screen(bot, message)

    try:
        if message.text.lower() == 'послуги':
            mass = list(menu['ПРО GIGAGROUP']['GIGACENTER']['ПОСЛУГИ'])
            screen_item.get_current_screen(mass, service_gigacenter, True)
        elif message.text.lower() == 'чому нас обирають':
            msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGACENTER'], parse_mode="Markdown")
            bot.register_next_step_handler(msg, about_gigacenter)
        elif message.text.lower() == 'повернутися до питань':
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            screen_item.get_error_screen(about_gigacenter)
        print(message.text)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def service_gigacenter(message):
    screen_item = Screen(bot, message)
    try:
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
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP']['GIGACENTER'])
            screen_item.get_previous_screen(mass, about_gigacenter, True, 'GIGACENTER')
        else:
            screen_item.get_error_screen(service_gigacenter)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def about_gigacloud(message):
    screen_item = Screen(bot, message)
    try:
        if message.text.lower() == 'послуги':
            mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD']['ПОСЛУГИ'])
            screen_item.get_current_screen(mass, service_gigacloud, True)
        elif message.text.lower() == 'чому нас обирають':
            msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGACLOUD'], parse_mode="Markdown")
            bot.register_next_step_handler(msg, about_gigacloud)
        elif message.text.lower() == 'повернутися до питань':
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            screen_item.get_error_screen(about_gigacloud)
        print(message.text)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

def service_gigacloud(message):
    screen_item = Screen(bot, message)
    try:
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
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD'])
            screen_item.get_previous_screen(mass, about_gigacloud, True, 'GIGACLOUD')
        else:
            screen_item.get_error_screen(service_gigacloud)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

def about_gigasafe(message):
    screen_item = Screen(bot, message)

    try:
        if message.text.lower() == 'послуги':
            mass = list(menu['ПРО GIGAGROUP']['GIGASAFE']['ПОСЛУГИ'])
            screen_item.get_current_screen(mass, service_gigasafe, True)
        elif message.text.lower() == 'чому нас обирають':
            msg = bot.send_message(message.chat.id, dialog['ЧОМУ НАС ОБИРАЮТЬ GIGASAFE'], parse_mode="Markdown")
            bot.register_next_step_handler(msg, about_gigasafe)
        elif message.text.lower() == 'повернутися до питань':
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP'])
            screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
        else:
            screen_item.get_error_screen(about_gigasafe)
        print(message.text)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

def service_gigasafe(message):
    screen_item = Screen(bot, message)
    try:
        if message.text.lower() == 'ідентифікація загроз':
            msg = bot.send_message(message.chat.id, dialog['ІДЕНТИФІКАЦІЯ ЗАГРОЗ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_order, 'GIGASAFE', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
        elif message.text.lower() == 'налаштування захисту':
            msg = bot.send_message(message.chat.id, dialog['НАЛАШТУВАННЯ ЗАХИСТУ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_order, 'GIGASAFE', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
        elif message.text.lower() == 'моніторинг аномалій':
            msg = bot.send_message(message.chat.id, dialog['МОНІТОРИНГ АНОМАЛІЙ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_order, 'GIGASAFE', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
        elif message.text.lower() == 'реагування на інциденти':
            msg = bot.send_message(message.chat.id, dialog['РЕАГУВАННЯ НА ІНЦИДЕНТИ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_order, 'GIGASAFE', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
        elif message.text.lower() == 'відновлення на покращення':
            msg = bot.send_message(message.chat.id, dialog['ВІДНОВЛЕННЯ НА ПОКРАЩЕННЯ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_order, 'GIGASAFE', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ПРО GIGAGROUP']['GIGASAFE'])
            screen_item.get_previous_screen(mass, about_gigasafe, True, 'GIGASAFE')
        else:
            screen_item.get_error_screen(service_gigasafe)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

def service_order(message, company, service):
    print(company)
    screen_item = Screen(bot, message)
    try:
        if company == 'GIGATRANS':
            if message.text.lower() == 'замовити послугу':
                mass = list(menu['ПРО GIGAGROUP'])
                screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
            else:
                mass = list(menu['ПРО GIGAGROUP']['GIGATRANS']['ПОСЛУГИ'])
                screen_item.get_previous_screen(mass, service_gigatrans, True, 'ПОСЛУГИ')
        elif company == 'GIGACENTER':
            if message.text.lower() == 'замовити послугу':
                mass = list(menu['ПРО GIGAGROUP'])
                screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
            else:
                mass = list(menu['ПРО GIGAGROUP']['GIGACENTER']['ПОСЛУГИ'])
                screen_item.get_previous_screen(mass, service_gigacenter, True, 'ПОСЛУГИ GIGACENTER')
        elif company == 'GIGACLOUD':
            if message.text.lower() == 'замовити послугу':
                mass = list(menu['ПРО GIGAGROUP'])
                screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
            else:
                mass = list(menu['ПРО GIGAGROUP']['GIGACLOUD']['ПОСЛУГИ'])
                screen_item.get_previous_screen(mass, service_gigacloud, True, 'ПОСЛУГИ')
        elif company == 'GIGASAFE':
            if message.text.lower() == 'замовити послугу':
                mass = list(menu['ПРО GIGAGROUP'])
                screen_item.get_previous_screen(mass, about_gigagroup, True, 'ПРО GIGAGROUP')
            else:
                mass = list(menu['ПРО GIGAGROUP']['GIGASAFE']['ПОСЛУГИ'])
                screen_item.get_previous_screen(mass, service_gigasafe, True, 'ПОСЛУГИ')
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

def top_service(message):
    screen_item = Screen(bot, message)
    try:
        if message.text.lower() == 'інтернет для бізнесу':
            msg = bot.send_message(message.chat.id, dialog['ІНТЕРНЕТ ДЛЯ БІЗНЕСУ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_top_order, 'GIGATRANS', 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ')
        elif message.text.lower() == 'оренда екранованої шафи':
            msg = bot.send_message(message.chat.id, dialog['ОРЕНДА ЕКРАНОВАНОЇ ШАФИ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_top_order, 'GIGACENTER', 'ОРЕНДА ЕКРАНОВАНОЇ ШАФИ')
        elif message.text.lower() == 'private cloud':
            msg = bot.send_message(message.chat.id, dialog['PRIVATE CLOUD'], reply_markup=keyboard_service_order, parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_top_order, 'GIGACLOUD', 'PRIVATE CLOUD')
        elif message.text.lower() == 'гібридні рішення':
            msg = bot.send_message(message.chat.id, dialog['ГІБРИДНІ РІШЕННЯ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_top_order, 'GIGACLOUD', 'ГІБРИДНІ РІШЕННЯ')
        elif message.text.lower() == 'ідентифікація загроз':
            msg = bot.send_message(message.chat.id, dialog['ІДЕНТИФІКАЦІЯ ЗАГРОЗ'], reply_markup=keyboard_service_order, parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_top_order, 'GIGASAFE', 'ІДЕНТИФІКАЦІЯ ЗАГРОЗ')
        elif message.text.lower() == 'будівництво волз':
            msg = bot.send_message(message.chat.id, dialog['БУДІВНИЦТВО ВОЛЗ'], reply_markup=keyboard_service_order,parse_mode="Markdown")
            bot.register_next_step_handler(msg, service_top_order, 'GIGATRANS', 'БУДІВНИЦТВО ВОЛЗ')
        elif message.text.lower() == 'повернутися до питань':
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu.keys())
            screen_item.get_previous_screen(mass, first_screen, False, 'Почати')
        else:
            screen_item.get_error_screen(top_service)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def service_top_order(message, company, service):
    print(company)
    screen_item = Screen(bot, message)
    try:
        if message.text.lower() == 'замовити послугу':
            if service == 'ІНТЕРНЕТ ДЛЯ БІЗНЕСУ':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
            elif service == 'ОРЕНДА ЕКРАНОВАНОЇ ШАФИ':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
            elif service == 'PRIVATE CLOUD':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
            elif service == 'ГІБРИДНІ РІШЕННЯ':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
            elif service == 'ІДЕНТИФІКАЦІЯ ЗАГРОЗ':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
            elif service == 'БУДІВНИЦТВО ВОЛЗ':
                mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
                screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu['ТОП-ПОСЛУГИ 🏆'])
            screen_item.get_previous_screen(mass, top_service, True, 'ТОП-ПОСЛУГИ 🏆')
        else:
            screen_item.get_error_screen(service_top_order)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

def add_manager(message):
    print(message)
    screen_item = Screen(bot, message)
    try:
        if (message.contact):
            print(1)
            db_users.add_message_from_contact(message)
            mass = list(menu.keys())
            screen_item.get_previous_screen(mass, first_screen, False, 'ЗАЯВА МЕНЕДЖЕРУ')
        else:
            if message.text.lower() != '⬅️назад':
                db_users.add_message(message)
                mass = list(menu.keys())
                screen_item.get_previous_screen(mass, first_screen, False, 'ЗАЯВА МЕНЕДЖЕРУ')
            else:
                mass = list(menu.keys())
                screen_item.get_previous_screen(mass, first_screen, False, 'Почати')
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')


def top_question(message):
    screen_item = Screen(bot, message)
    try:
        if message.text.lower() == 'gigatrans':
            mass = list(inline_menu['GIGATRANS'])
            screen_item.get_popular_question_screen(mass, 'gigatrans', top_question)
        elif message.text.lower() == 'gigacenter':
            mass = list(inline_menu['GIGACENTER'])
            screen_item.get_popular_question_screen(mass, 'gigacenter', top_question)
        elif message.text.lower() == 'gigacloud':
            mass = list(inline_menu['GIGACLOUD'])
            screen_item.get_popular_question_screen(mass, 'gigacloud', top_question)
        elif message.text.lower() == 'gigasafe':
            mass = list(inline_menu['GIGASAFE'])
            screen_item.get_popular_question_screen(mass, 'gigasafe', top_question)
        elif message.text.lower() == 'повернутися до питань':
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'НАЙПОПУЛЯРНІШІ ПИТАННЯ')
        elif message.text.lower() == '⬅️назад':
            mass = list(menu.keys())
            screen_item.get_previous_screen(mass, first_screen, False, 'Почати')
        else:
            screen_item.get_error_screen(about_gigagroup)
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

    print(message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    screen_item = Screen(bot, call.message)
    print(call.message)
    # GIGATRANS QUESTION
    try:
        if call.data == "gigatrans1":
            screen_item.get_popular_question_edit_screen('ЯКІ ДІЮТЬ ТАРИФИ НА ПІДКЛЮЧЕННЯ ІНТЕРНЕТУ?', False)
        elif call.data == "gigatrans2":
            screen_item.get_popular_question_edit_screen('ЧИ МОЖЕТЕ ВИ ВИКОНАТИ МІЖНАРОДНЕ ПІДКЛЮЧЕННЯ?', False)
        elif call.data == "gigatrans3":
            screen_item.get_popular_question_edit_screen('ЯКІ ТЕРМІНИ ПІДКЛЮЧЕННЯ ІНТЕРНЕТУ?', False)
        elif call.data == "gigatrans4":
            screen_item.get_popular_question_edit_screen('ЧИ ГАРАНТУЄТЕ ВИ ШВИДКІСТЬ ІНТЕРНЕТУ 100 ГБІТ/С?', False)
        elif call.data == "gigatrans5":
            screen_item.get_popular_question_edit_screen('ЯКУ Я ОТРИМАЮ ІР-АДРЕСУ, СТАТИЧНУ ЧИ ДИНАМІЧНУ?', False)
        elif call.data == "gigatrans6":
            screen_item.get_popular_question_edit_screen('ЯКІ ЛІНІЇ ЗВ\'ЯЗКУ ВИ ВИКОРИСТОВУЄТЕ ДЛЯ ПІДКЛЮЧЕННЯ?', False)
        elif call.data == "gigatrans7":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС СЕРТИФІКАТ БЕЗПЕКИ КСЗІ?', False)
        elif call.data == "gigatrans8":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС СЕРТИФІКАТ ISO?', False)

        # GIGACENTER QUESTION

        elif call.data == "gigacenter1":
            screen_item.get_popular_question_edit_screen('ЯКІ ТАРИФИ НА КАЛОКЕЙШН?', False)
        elif call.data == "gigacenter2":
            screen_item.get_popular_question_edit_screen('ЯКИЙ РІВЕНЬ ВІДМОВОСТІЙКОСТІ ОБЛАДНАННЯ?', False)
        elif call.data == "gigacenter3":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС РЕЗЕРВУВАННЯ ІНФРАСТРУКТУРИ?', False)
        elif call.data == "gigacenter4":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС СЕРТИФІКАТИ ЯКОСТІ ISO?', False)
        elif call.data == "gigacenter5":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС ПОСЛУГА SMART HANDS?', False)
        elif call.data == "gigacenter6":
            screen_item.get_popular_question_edit_screen('ЧИ МОЖУ Я ВІДВІДАТИ ДАТА-ЦЕНТР?', False)
        elif call.data == "gigacenter7":
            screen_item.get_popular_question_edit_screen('ЧИ ВІДПОВІДАЄТЕ ВИ СТАНДАРТУ НБУ?', False)

            # GIGACLOUD QUESTION

        elif call.data == "gigacloud1":
            screen_item.get_popular_question_edit_screen('НА ЧОМУ ПОБУДОВАНА ІНФРАСТРУКТУРА ХМАРИ?', False)
        elif call.data == "gigacloud2":
            screen_item.get_popular_question_edit_screen('ДЕ РОЗМІЩЕНА ІНФРАСТРУКТУРА GIGACLOUD?', False)
        elif call.data == "gigacloud3":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС СЕРТИФІКАТИ КСЗІ ТА ISO?', False)
        elif call.data == "gigacloud4":
            screen_item.get_popular_question_edit_screen('ЧИ МОЖУ Я САМОСТІЙНО УПРАВЛЯТИ ПРАВАМИ ДОСТУПУ ДО ВІРТУАЛЬНИХ СЕРВЕРІВ?', False)
        elif call.data == "gigacloud5":
            screen_item.get_popular_question_edit_screen('ЧИ ДОПОМАГАЄТЕ ВИ З ПЕРЕНЕСЕННЯМ СЕРВІСІВ ДО ХМАРИ?', False)
        elif call.data == "gigacloud6":
            screen_item.get_popular_question_edit_screen('ЧИ НАДАЄТЕ ВИ ТЕСТОВИЙ ПЕРІОД?', False)
        elif call.data == "gigacloud7":
            screen_item.get_popular_question_edit_screen('ЧИ Є У ВАС РЕЗЕРВУВАННЯ ІНФРАСТРУКТУРИ?GIGACLOUD', False)

        # GIGASAFE QUESTION

        elif call.data == "gigasafe1":
            screen_item.get_popular_question_edit_screen('ЯКИМИ ДОСВІДОМ ВОЛОДІЄ КОМАНДА?', False)
        elif call.data == "gigasafe2":
            screen_item.get_popular_question_edit_screen('ЯКІ СЕРТИФІКАТИ МАЮТЬ СПЕЦІАЛІСТИ GIGASAFE?', False)
        elif call.data == "gigasafe3":
            screen_item.get_popular_question_edit_screen('ЯК ПЕРЕВІРИТИ ЧИ Є КІБЕРЗАГРОЗИ ДЛЯ МОГО БІЗНЕСУ?', False)
        elif call.data == "gigasafe4":
            screen_item.get_popular_question_edit_screen('ЯК GIGASAFE ЗАБЕЗПЕЧУЄ БЕЗПЕКУ ДАНИХ ЗАМОВНИКА?', False)
        elif call.data == "gigasafe5":
            screen_item.get_popular_question_edit_screen('ЯК БІЗНЕС МОЖЕ ЗАХИСТИТИСЯ ВІД ЗАГРОЗ ПРИ ВІДДАЛЕНІЙ РОБОТІ?', False)
        elif call.data == "gigasafe6":
            screen_item.get_popular_question_edit_screen('ЯКА ВАРТІСТЬ ВАШИХ ПОСЛУГ?', False)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=dialog['ОШИБКА ВОПРОСА'])
            mass = list(menu['НАЙПОПУЛЯРНІШІ ПИТАННЯ'])
            screen_item.get_previous_screen(mass, top_question, True, 'Почати')
    except Exception:
        print('Ошибка формата')
        mass = list(menu.keys())
        screen_item.get_first_screen(mass, first_screen, False, 'ОШИБКА')

bot.polling()