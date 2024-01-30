from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_city() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Калининград")
    kb.button(text="Абакан")
    kb.button(text="В главное меню")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)
