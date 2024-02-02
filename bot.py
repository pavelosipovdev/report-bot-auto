import os
import logging
import requests
import asyncio
import atexit

import handlers
import utils.connectors

from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F

from handlers.sellpath import router
from handlers.buypath import router
from handlers.comissionpath import router

from aiogram.fsm.storage.memory import MemoryStorage

from texts import texts

load_dotenv()


class NotHandledHandler(logging.Handler):
    def emit(self, record):
        if "is not handled" in record.msg:
            print(f"Необработанное обновление: {record.msg}")
            logging.error(f"Необработанное обновление: {record.msg}")


class LoggingManager:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, filename="bot_log.log", filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
        logging.info("===================START_BOT===================")
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        logging.getLogger().addHandler(console_handler)
        logging.getLogger("aiogram").addHandler(NotHandledHandler())

    def finish_bot(self):
        logging.info("===================FINISH_BOT===================")
        url = f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/sendMessage'
        message_text = "+++++++++++++FINISH_BOT+++++++++++++"
        params = {
            'chat_id': os.getenv('ERROR_CHAT_ID'),
            'text': message_text,
        }
        response = requests.post(url, params=params)
        print(response.json())


logging_manager = LoggingManager()
bot = Bot(os.getenv('BOT_TOKEN'))

atexit.register(logging_manager.finish_bot)

# Диспетчер
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


@dp.message(Command("start"))
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

    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_COMISSION,
        callback_data="bt_constructor_2_comission")
    )
    keyboard_to_delete = types.ReplyKeyboardRemove()
    await message.answer(text="Пожалуйста подождите, идет проверка баз данных", reply_markup=markup)
    await utils.connectors.db_sql_start(message.chat.username, message.chat.first_name, message.chat.last_name, bot)
    logging.info("Success login for " + message.chat.first_name + " " + message.chat.last_name + " " + message.chat.username)
    await bot.send_message(os.getenv('ERROR_CHAT_ID'),
                           "Success login for " + message.chat.first_name + " " + message.chat.last_name)
    await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


dp.include_routers(handlers.sellpath.router)
dp.include_routers(handlers.buypath.router)
dp.include_routers(handlers.comissionpath.router)


async def main():
    await bot.send_message(os.getenv('ERROR_CHAT_ID'), "=======BOT_START=======")
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
#
# import asyncio
# import logging
# import os
#
# import handlers
# import utils.connectors
# from dotenv import load_dotenv
#
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.filters.command import Command
# from aiogram.fsm.storage.memory import MemoryStorage
#
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# import requests
#
# from handlers.sellpath import router
# from handlers.buypath import router
# from handlers.comissionpath import router
# from texts import texts
# import atexit
#
# load_dotenv()
# bot = Bot(token=os.getenv('BOT_TOKEN'))
# ERROR_CHAT_ID = os.getenv('ERROR_CHAT_ID')
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.DEBUG, filename="bot_log.log", filemode="a",
#                     format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
# logging.info("===================START_BOT===================")
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)
# logging.getLogger().addHandler(console_handler)
#
#
# class NotHandledHandler(logging.Handler):
#     def emit(self, record):
#         if "is not handled" in record.msg:
#             print(f"Необработанное обновление: {record.msg}")
#             logging.error(f"Необработанное обновление: {record.msg}")
#
#
# not_handled_handler = NotHandledHandler()
# logging.getLogger("aiogram").addHandler(not_handled_handler)
#
#
# def finish_sender():
#     logging.info("===================FINISH_BOT===================")
#     url = f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/sendMessage'
#     message_text = "=======FINISH_BOT======="
#     params = {
#         'chat_id': ERROR_CHAT_ID,
#         'text': message_text,
#     }
#     response = requests.post(url, params=params)
#     print(response.json())
#
#
# atexit.register(finish_sender)
#
# # Диспетчер
# storage = MemoryStorage()
# dp = Dispatcher(storage=storage)
#
#
# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await bot.delete_webhook(drop_pending_updates=True)
#     await bot.send_message(ERROR_CHAT_ID, "=======BOT_START=======")
#     await dp.start_polling(bot)
#
#
# # @dp.message(Command("start"))
# # async def cmd_start(message: types.Message):
# #     builder = InlineKeyboardBuilder()
# #     builder.add(types.InlineKeyboardButton(
# #         text=texts.BT_CONSTRUCTOR_1_SELL,
# #         callback_data="bt_constructor_1_sell")
# #     )
# #     builder.add(types.InlineKeyboardButton(
# #         text=texts.BT_CONSTRUCTOR_1_BUY,
# #         callback_data="bt_constructor_1_buy")
# #     )
# #     # builder.row(types.InlineKeyboardButton(
# #     #     text=texts.CB_BUY_BUTTON31,
# #     #     callback_data="main_menu_button5")
# #     # )
# #
# #     await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())
#
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     markup = types.ReplyKeyboardRemove()
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_1_SELL,
#         callback_data=texts.BT_CONSTRUCTOR_1_SELL)
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_1_BUY,
#         callback_data=texts.BT_CONSTRUCTOR_1_BUY)
#     )
#
#     builder.row(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_2_COMISSION,
#         callback_data="bt_constructor_2_comission")
#     )
#     keyboard_to_delete = types.ReplyKeyboardRemove()
#     await message.answer(text="Пожалуйста подождите, идет проверка баз данных", reply_markup=markup)
#     await utils.connectors.db_sql_start(message.chat.username, message.chat.first_name, message.chat.last_name)
#     await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())
#
#
# dp.include_routers(handlers.sellpath.router)
# dp.include_routers(handlers.buypath.router)
# dp.include_routers(handlers.comissionpath.router)
#
# if __name__ == "__main__":
#     asyncio.run(main())
