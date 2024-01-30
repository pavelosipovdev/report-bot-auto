import asyncio
import logging
import os
import utils.connectors
from dotenv import load_dotenv

import psycopg2
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers import questions, reports, template_use, sellpath, buypath, comissionpath
from texts import texts
from utils import api, convert

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.DEBUG)
# Диспетчер
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Запуск процесса поллинга новых апдейтов
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_1_SELL,
#         callback_data="bt_constructor_1_sell")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_1_BUY,
#         callback_data="bt_constructor_1_buy")
#     )
#     # builder.row(types.InlineKeyboardButton(
#     #     text=texts.CB_BUY_BUTTON31,
#     #     callback_data="main_menu_button5")
#     # )
#
#     await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


@dp.message(Command("start"))
@dp.callback_query(F.data == "main_menu23232")
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardRemove()
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_1_SELL,
        callback_data=texts.BT_CONSTRUCTOR_1_SELL)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_1_BUY,
        callback_data=texts.BT_CONSTRUCTOR_1_BUY)
    )

    # builder.row(types.InlineKeyboardButton(
    #     text=texts.BT_CONSTRUCTOR_2_COMISSION,
    #     callback_data="bt_constructor_2_comission")
    # )
    keyboard_to_delete = types.ReplyKeyboardRemove()
    await message.answer(text="Пожалуйста подождите, идет проверка баз данных", reply_markup=markup)
    await utils.connectors.db_sql_start(message.chat.username, message.chat.first_name, message.chat.last_name)
    await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


dp.include_routers(sellpath.router)
dp.include_routers(buypath.router)
dp.include_routers(comissionpath.router)

if __name__ == "__main__":
    asyncio.run(main())
