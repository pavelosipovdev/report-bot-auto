import asyncio
import logging
import os
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

async def db_sql_start(username, firstname, lastname):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_count_tg_user_info = "select count(*) from bot_planeta_avto.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
        cur.execute(sql_count_tg_user_info.format(value_teg_name_tg="@" + username))
        count_tg_user_info = cur.fetchall()
        print(count_tg_user_info[0][0])

        if count_tg_user_info[0][0] == 0:
            sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.tg_info_user(teg_name_tg, user_name_tg) VALUES (%s,%s)'
            cur.execute(sql_insert_tg_info_user, ("@" + username, firstname + " " + lastname,))
    else:
        print(f'База недоступна, статус {conn.closed}')
    conn.commit()
    conn.close()


@dp.message(Command("start"))
@dp.callback_query(F.data == "main_menu23232")
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardRemove()
    builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text=texts.BT_CONSTRUCTOR_1_SELL,
    #     callback_data=texts.BT_CONSTRUCTOR_1_SELL)
    # )
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
    await db_sql_start(message.chat.username, message.chat.first_name, message.chat.last_name)
    await message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


dp.include_routers(sellpath.router)
dp.include_routers(buypath.router)
dp.include_routers(comissionpath.router)

if __name__ == "__main__":
    asyncio.run(main())
