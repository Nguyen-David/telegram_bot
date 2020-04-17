from telebot import types

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