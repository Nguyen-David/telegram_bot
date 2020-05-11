from telebot import types
from menu import menu
from dialog import dialog, question


def create_menu(mass, back=True):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if len(mass) == 1:
        markup.row(mass[0])
    else:
        while len(mass) > 0:
            try:
                cut = mass[:2]
                markup.row(cut[0], cut[1])
                del mass[:2]

                if len(mass) == 1:
                    markup.row(mass[0])
                    break
            except:
                print('WTF')

    if back == True:
        markup.row('Назад')

    return markup

def create_inline_menu(mass, company):
    markup = types.InlineKeyboardMarkup(row_width=1)

    index = 1
    while len(mass) > 0:
        try:
            cut = mass[:1]
            callback_button = types.InlineKeyboardButton(text=cut[0], callback_data=company + str(index))
            markup.add(callback_button)
            del mass[:1]
            index += 1
        except:
            print('WTF')

    return markup


class Screen:
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    def get_first_screen(self, mass, next_step, back, msg_text):
        print(msg_text)
        markup = create_menu(mass, back=back)
        msg = self.bot.send_message(self.message.chat.id, dialog[msg_text], reply_markup=markup, parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, next_step)

    def get_current_screen(self, mass, next_step, back):
        markup = create_menu(mass, back=back)
        msg = self.bot.send_message(self.message.chat.id, dialog[self.message.text], reply_markup=markup, parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, next_step)

    def get_previous_screen(self, mass, prev_step, back, msg_text):
        markup = create_menu(mass, back=back)
        msg = self.bot.send_message(self.message.chat.id, dialog[msg_text], reply_markup=markup, parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, prev_step)

    def get_recursive_screen(self, current_step):
        msg = self.bot.send_message(self.message.chat.id, dialog[self.message.text], parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, current_step)

    def get_error_screen(self, current_step):
        msg = self.bot.send_message(self.message.chat.id, 'Простите я вас не понял(', parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, current_step)

    def get_add_manager_screen(self, next_step):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        button_back = types.KeyboardButton(text="Назад")
        keyboard.add(button_phone, button_back)
        msg = self.bot.send_message(self.message.chat.id, dialog[self.message.text], reply_markup=keyboard,
                               parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, next_step)

    def get_popular_question_screen(self, mass, company, next_step):
        markup = create_inline_menu(mass, company)
        msg = self.bot.send_message(self.message.chat.id, "*НАЙПОПУЛЯРНІШІ ПИТАННЯ *" + "*" + self.message.text + "*", reply_markup=markup, parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, next_step)

    def get_popular_question_edit_screen(self,  msg_text, back):
        mass = list(['ПОВЕРНУТИСЯ ДО ПИТАНЬ'])
        markup = create_menu(mass, back=back)
        self.bot.edit_message_text(chat_id=self.message.chat.id, message_id=self.message.message_id,
                              text=question[msg_text], parse_mode="Markdown")
        self.bot.send_message(self.message.chat.id, dialog['ПОВЕРНУТИСЯ ДО ПИТАНЬ'], reply_markup=markup, parse_mode="Markdown")