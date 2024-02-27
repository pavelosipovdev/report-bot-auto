from aiogram import types


def get_buy_keyboard_page1():
    buttons = [
        [
            types.InlineKeyboardButton(text="Где купил", callback_data="num_buy_chosen_place"),
        ],
        [
            types.InlineKeyboardButton(text="Кто купил", callback_data="num_buy_chosen_college_fio"),
            types.InlineKeyboardButton(text="Кто писал ДКП", callback_data="num_buy_chosen_college_fio_dkp"),
        ],
        [
            types.InlineKeyboardButton(text="Цена", callback_data="num_buy_chosen_cost"),
            types.InlineKeyboardButton(text="Резина", callback_data="num_buy_chosen_wire_boolean"),
        ],
        [
            types.InlineKeyboardButton(text="VIN номер", callback_data="num_buy_chosen_vin_number"),
            types.InlineKeyboardButton(text="Гос номер", callback_data="num_buy_chosen_vin_gos_number"),
        ],
        [
            types.InlineKeyboardButton(text="Марка", callback_data="num_buy_chosen_vin_marka"),
            types.InlineKeyboardButton(text="Модель", callback_data="num_buy_chosen_vin_model"),
        ],
        [
            types.InlineKeyboardButton(text="Год", callback_data="num_buy_chosen_vin_year"),
            types.InlineKeyboardButton(text="Коммент", callback_data="num_buy_chosen_comment"),
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="start_editor")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_buy_keyboard_page2():
    buttons = [
        [

            types.InlineKeyboardButton(text="111111", callback_data="num_incr2"),
            types.InlineKeyboardButton(text="122222", callback_data="num_incr3"),
        ],
        [
            types.InlineKeyboardButton(text="14441144", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15551155", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14442244", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15552255", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14443344", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15553355", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14444444", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15544555", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14445544", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15556655", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="17755777", callback_data="num_incr8"),
            types.InlineKeyboardButton(text="18885588", callback_data="num_incr9")],
        [
            types.InlineKeyboardButton(text="←", callback_data="num_page1"),
            types.InlineKeyboardButton(text="→", callback_data="num_page1"),
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_comission_keyboard_page1():
    buttons = [
        [
            types.InlineKeyboardButton(text="Где купил", callback_data="num_comission_chosen_place"),
            types.InlineKeyboardButton(text="Вид расчета", callback_data="num_comission_typeraschet"),
        ],
        [
            types.InlineKeyboardButton(text="Кто купил", callback_data="num_comission_chosen_college_fio"),
            types.InlineKeyboardButton(text="Кто писал ДКП", callback_data="num_comission_chosen_college_fio_dkp"),
        ],
        [
            types.InlineKeyboardButton(text="Сколько собственнику", callback_data="num_comission_howmuchsobs"),
            types.InlineKeyboardButton(text="Комиссия собственнику", callback_data="num_comission_howmuchcomissiob"),
        ],
        [
            types.InlineKeyboardButton(text="VIN номер", callback_data="num_comission_chosen_vin_number"),
            types.InlineKeyboardButton(text="Гос номер", callback_data="num_comission_chosen_vin_gos_number"),
        ],
        [
            types.InlineKeyboardButton(text="Марка", callback_data="num_comission_chosen_vin_marka"),
            types.InlineKeyboardButton(text="Модель", callback_data="num_comission_chosen_vin_model"),
        ],
        [
            types.InlineKeyboardButton(text="Год", callback_data="num_comission_chosen_vin_year"),
            types.InlineKeyboardButton(text="Коммент", callback_data="num_comission_chosen_comment"),
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="start_editor")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_comission_keyboard_page2():
    buttons = [
        [

            types.InlineKeyboardButton(text="111111", callback_data="num_incr2"),
            types.InlineKeyboardButton(text="122222", callback_data="num_incr3"),
        ],
        [
            types.InlineKeyboardButton(text="14441144", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15551155", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14442244", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15552255", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14443344", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15553355", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14444444", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15544555", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14445544", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15556655", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="17755777", callback_data="num_incr8"),
            types.InlineKeyboardButton(text="18885588", callback_data="num_incr9")],
        [
            types.InlineKeyboardButton(text="←", callback_data="num_page1"),
            types.InlineKeyboardButton(text="→", callback_data="num_page1"),
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_sell_keyboard_page1():
    buttons = [
        [

            types.InlineKeyboardButton(text="111111", callback_data="num_incr2"),
            types.InlineKeyboardButton(text="122222", callback_data="num_incr3"),
        ],
        [
            types.InlineKeyboardButton(text="14441144", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15551155", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14442244", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15552255", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14443344", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15553355", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14444444", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15544555", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14445544", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15556655", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="17755777", callback_data="num_incr8"),
            types.InlineKeyboardButton(text="18885588", callback_data="num_incr9")],
        [
            types.InlineKeyboardButton(text="←", callback_data="num_page2"),
            types.InlineKeyboardButton(text="→", callback_data="num_page2"),
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_sell_keyboard_page2():
    buttons = [
        [

            types.InlineKeyboardButton(text="111111", callback_data="num_incr2"),
            types.InlineKeyboardButton(text="122222", callback_data="num_incr3"),
        ],
        [
            types.InlineKeyboardButton(text="14441144", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15551155", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14442244", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15552255", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14443344", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15553355", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14444444", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15544555", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="14445544", callback_data="num_incr5"),
            types.InlineKeyboardButton(text="15556655", callback_data="num_incr6"),
        ],
        [
            types.InlineKeyboardButton(text="17755777", callback_data="num_incr8"),
            types.InlineKeyboardButton(text="18885588", callback_data="num_incr9")],
        [
            types.InlineKeyboardButton(text="←", callback_data="num_page1"),
            types.InlineKeyboardButton(text="→", callback_data="num_page1"),
        ],
        [types.InlineKeyboardButton(text="Назад", callback_data="num_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
