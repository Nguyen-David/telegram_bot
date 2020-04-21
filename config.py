from telebot import types
from menu import menu
from dialog import dialog


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


class Screen:
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    def get_current_screen(self, next_step, back):
        mass = list(menu[self.message.text].keys())
        markup = create_menu(mass, back=back)
        msg = self.bot.send_message(self.message.chat.id, dialog[self.message.text], reply_markup=markup, parse_mode="Markdown")
        self.bot.register_next_step_handler(msg, next_step)
