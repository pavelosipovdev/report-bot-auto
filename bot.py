import asyncio
import logging
import os

import handlers
import utils.connectors
from dotenv import load_dotenv

import psycopg2
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.utils.keyboard import InlineKeyboardBuilder

# from handlers import sellpath, buypath, comissionpath
from handlers.sellpath import router
from handlers.buypath import router
from handlers.comissionpath import router
from texts import texts
import atexit

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.DEBUG, filename="bot_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")
logging.info("===================START_BOT===================")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger().addHandler(console_handler)


class NotHandledHandler(logging.Handler):
    def emit(self, record):
        if "is not handled" in record.msg:
            print(f"Необработанное обновление: {record.msg}")
            logging.error(f"Необработанное обновление: {record.msg}")


not_handled_handler = NotHandledHandler()
logging.getLogger("aiogram").addHandler(not_handled_handler)


# Отправка сообщения при завершении бота
def finish_bot():
    logging.info("===================FINISH_BOT===================")


# Регистрация обработчика atexit
atexit.register(finish_bot)

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

    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_COMISSION,
        callback_data="bt_constructor_2_comission")
    )
    keyboard_to_delete = types.ReplyKeyboardRemove()
    await message.answer(text="Пожалуйста подождите, идет проверка баз данных", reply_markup=markup)
    await utils.connectors.db_sql_start(message.chat.username, message.chat.first_name, message.chat.last_name)
    await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


dp.include_routers(handlers.sellpath.router)
dp.include_routers(handlers.buypath.router)
dp.include_routers(handlers.comissionpath.router)

if __name__ == "__main__":
    asyncio.run(main())
