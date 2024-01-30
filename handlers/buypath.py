from pydoc import html
from typing import Optional

import psycopg2
import os
from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineQueryResultArticle, InputTextMessageContent, InlineQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import convert, api
from texts import texts
import re

router = Router()


class SetReport(StatesGroup):
    choosing_buyer = State()
    choosing_data_car = State()
    choosing_vin = State()
    choosing_pts = State()
    choosing_data_car_marka = State()
    choosing_data_car_model = State()
    choosing_data_car_year = State()
    choosing_data_car_gosnumber = State()
    choosing_data_car_next = State()
    choosing_self_college = State()
    choosing_self_college_dkp = State()
    choosing_who_write_dkp0 = State()
    choosing_who_write_dkp = State()
    choosing_cost = State()
    choosing_cost1 = State()
    choosing_wire = State()
    choosing_wire_cost = State()
    choosing_comment = State()
    choosing_who_write_dkp_inline = State()
    choosing_cost_inline = State()
    choosing_comment = State()
    choosing_comment = State()
    choosing_editor = State()
    choosing_editor_start = State()
    choosing_editor_first = State()
    choosing_editor_first_place = State()
    choosing_editor_first_cost = State()
    choosing_editor_first_vin_gos_number = State()
    choosing_editor_first_vin_marka = State()
    choosing_editor_first_vin_model = State()
    choosing_editor_first_vin_year = State()
    choosing_editor_first_vin_number = State()
    choosing_editor_first_comment = State()
    choosing_editor_finish = State()


def db_sql_buy_with_college(username):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    print(username)
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_count_tg_user_info = "select count(*) from bot_planeta_avto.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
        cur.execute(sql_count_tg_user_info.format(value_teg_name_tg=username))
        count_tg_user_info = cur.fetchall()
        print(count_tg_user_info[0][0])
        if count_tg_user_info[0][0] != 0:
            sql_select_tg_user_info = "select user_name_tg from bot_planeta_avto.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
            cur.execute(sql_select_tg_user_info.format(value_teg_name_tg=username))
            select_tg_user_info = cur.fetchall()
            return select_tg_user_info[0][0]
        else:
            print(count_tg_user_info[0][0])
            return "Некорректный USERNAME"
    else:
        print(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()


dict_colleges = [
    {"id": "1", "name": "Осипов Павел", "tag": "rogerthatdev"},
    {"id": "2", "name": "Чудин Павел", "tag": "p_chudin"}
]


@router.callback_query(F.data == texts.BT_CONSTRUCTOR_1_BUY)
async def main_menu_bt_constructor_1_buy(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_type=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_ATP,
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_ABAKAN,
        callback_data=texts.BT_CONSTRUCTOR_2_ABAKAN)
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_PLANETA,
        callback_data=texts.BT_CONSTRUCTOR_2_PLANETA)
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_ALIEN,
        callback_data=texts.BT_CONSTRUCTOR_2_ALIEN)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_GETOUT,
        callback_data=texts.BT_CONSTRUCTOR_2_GETOUT)
    )

    await callback.message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_1_SELL, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer)
    await callback.message.delete()


@router.callback_query(SetReport.choosing_buyer)
async def constructor_choosing_download(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_place=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD,
        callback_data=texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD)
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD,
        callback_data=texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD)
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL,
        callback_data=texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
    )
    await callback.message.edit_text(text="Скачать или руками", reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_data_car)


@router.callback_query(SetReport.choosing_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON2)
    await state.set_state(SetReport.choosing_vin)


@router.callback_query(SetReport.choosing_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON22)
    await state.set_state(SetReport.choosing_pts)


@router.callback_query(SetReport.choosing_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Укажите VIN")
    await state.set_state(SetReport.choosing_data_car_marka)


@router.message(SetReport.choosing_data_car_marka)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_number=message.text.upper())
    await message.answer(text="Укажите марку")
    await state.set_state(SetReport.choosing_data_car_model)


@router.message(SetReport.choosing_data_car_model)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_marka=message.text.upper())
    await message.answer(text="Укажите модель")
    await state.set_state(SetReport.choosing_data_car_year)


@router.message(SetReport.choosing_data_car_year)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_model=message.text.upper())
    await message.answer(text="Укажите год")
    await state.set_state(SetReport.choosing_data_car_gosnumber)


@router.message(SetReport.choosing_data_car_gosnumber)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_year=message.text.upper())
    await message.answer(text="Укажите гоc номер")
    await state.set_state(SetReport.choosing_data_car_next)


@router.message(SetReport.choosing_data_car_next)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_gos_number=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    data = await state.get_data()
    text = f'''Вы указали:
    Год {data['chosen_vin_year'].upper()}
    Гос номер {data['chosen_vin_gos_number'].upper()}
    VIN {data['chosen_vin_number'].upper()}
    Марка {data['chosen_vin_marka'].upper()}
    Модель {data['chosen_vin_model'].upper()}
    '''
    await message.answer(text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_self_college)


@router.message(SetReport.choosing_vin, F.photo)
async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await bot.download(
        message.photo[-1],
        destination=f"tmp/{message.photo[-1].file_id}.jpg"

    )
    await message.answer(text="Подождите пожалуйста")
    convert.convert_json_vin(f"tmp/{message.photo[-1].file_id}.jpg")
    msg = api.get_strings_vin()
    print(msg)
    doka = []
    for i in msg:
        if i["name"] == "stsfront_car_year":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_number":
            doka.append(i["text"])
        elif i["name"] == "stsfront_vin_number":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_brand":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_model":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_color":
            doka.append(i["text"])

    print(doka)
    # data_new = f"{msg[]}"
    msg2 = f'''В базу внесено:
    Год {str(doka[0]).upper()}
    Гос номер {str(doka[1]).upper()}
    VIN {str(doka[2]).upper()}
    Марка {str(doka[3]).upper()}
    Модель {str(doka[4]).upper()}
    '''
    await state.update_data(chosen_vin_gos_number=str(doka[1]).upper(), chosen_vin_number=str(doka[2]).upper(),
                            chosen_vin_marka=str(doka[3]).upper(), chosen_vin_model=str(doka[4]).upper(),
                            chosen_vin_year=str(doka[
                                                    0]).upper())  # await message.answer(text=texts.MESSAGE_MAIN_MENU_VIN, reply_markup=builder.as_markup())
    await message.answer(text=msg2, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_self_college)


@router.message(SetReport.choosing_pts, F.photo)
async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await bot.download(
        message.photo[-1],
        destination=f"tmp/{message.photo[-1].file_id}.jpg"

    )
    await message.answer(text="Подождите пожалуйста", reply_markup=builder.as_markup())
    convert.convert_json_japan(f"tmp/{message.photo[-1].file_id}.jpg")
    msg = api.get_strings_japan()
    # print(msg)
    doka = []
    electro_vin = 'UNKNOWN'
    for i in msg:
        if i["lines"][0]["words"][0]["text"]:
            doka.append(i["lines"][0]["words"][0]["text"])
    print(doka)
    for k in doka:
        if len(k) == 14 and str(k[13]).isdigit():
            electro_vin = str(k).upper()
            print(electro_vin)
    print(doka[6], doka[8], doka[10], doka[25])
    msg2 = f'''В базу внесено:
    Год {str(doka[25]).upper()}
    VIN {str(doka[6]).upper()}
    Марка {str(doka[8]).upper()}
    Модель {str(doka[10]).upper()}
    '''
    await message.answer(text=msg2, reply_markup=builder.as_markup())
    await state.update_data(chosen_vin_gos_number="NONE", chosen_vin_number=str(doka[6]).upper(),
                            chosen_vin_marka=str(doka[8]).upper(), chosen_vin_model=str(doka[10]).upper(),
                            chosen_vin_year=str(doka[25]).upper())
    await state.set_state(SetReport.choosing_self_college)


@router.callback_query(SetReport.choosing_self_college)
async def constructor_choosing_dkp(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_dkp1=callback.data, chosen_dkp=callback.message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    )
    await callback.message.edit_text(text=texts.MESSAGE_BT_CONSTRUCTOR_4_COLLEGE, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_self_college_dkp)


@router.callback_query(SetReport.choosing_self_college_dkp, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_colleges ')
    )
    await callback.message.edit_text(text="Введите первые символы фамилии коллеги", reply_markup=builder.as_markup())
    await state.update_data(chosen_college=callback.data)
    await state.set_state(SetReport.choosing_who_write_dkp0)


@router.message(SetReport.choosing_who_write_dkp0)
@router.inline_query(lambda query: query.query.startswith("find_colleges "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    #     builder.add(types.InlineKeyboardButton(
    #         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
    #         callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    #     )
    # Здесь ты можешь реализовать логику поиска колледжа и создать список результатов
    results = []

    # Получение дополнительных символов из запроса
    query = inline_query.query
    query = query.replace("find_colleges ", "").strip()

    # Поиск колледжей, название или адрес которых содержит дополнительные символы
    # Здесь ты можешь использовать свою базу данных или API для получения данных о колледжах
    # Для примера я буду использовать список колледжей в Москве
    # colleges = [
    #     {"id": "1", "name": "Осипов Павел", "tag": "rogerthatdev"},
    #     {"id": "2", "name": "Чудин Павел", "tag": "p_chudin"}
    # ]


    # Фильтрация колледжей по дополнительным символам
    for college in dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            # Добавление результата в список
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    # Отправка результатов пользователю
    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_who_write_dkp_inline)
    # await state.set_state(SetReport.choosing_cost1)
    # await state.set_state(SetReport.choosing_wire)


@router.message(SetReport.choosing_who_write_dkp_inline)
async def constructor_choosing_cost(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_fio=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    )
    await message.answer(text="КТО ПИСАЛ ДКП?", reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_cost_inline)


@router.callback_query(SetReport.choosing_cost_inline, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_cost222(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_dkps="САМ")
    await callback.message.edit_text(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.callback_query(SetReport.choosing_cost_inline, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_colleges_dkp ')
    )
    await callback.message.edit_text(text="Введите первые символы фамилии коллеги", reply_markup=builder.as_markup())
    # await state.update_data(chosen_college=callback.data)
    await state.set_state(SetReport.choosing_who_write_dkp_inline)


@router.message(SetReport.choosing_who_write_dkp_inline)
@router.inline_query(lambda query: query.query.startswith("find_colleges_dkp "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    #     builder.add(types.InlineKeyboardButton(
    #         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
    #         callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    #     )
    # Здесь ты можешь реализовать логику поиска колледжа и создать список результатов
    results = []

    # Получение дополнительных символов из запроса
    query = inline_query.query
    query = query.replace("find_colleges_dkp ", "").strip()

    # Поиск колледжей, название или адрес которых содержит дополнительные символы
    # Здесь ты можешь использовать свою базу данных или API для получения данных о колледжах
    # Для примера я буду использовать список колледжей в Москве

    # Фильтрация колледжей по дополнительным символам
    for college in dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            # Добавление результата в список
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    # Отправка результатов пользователю
    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_wire_cost)


# @router.message(SetReport.choosing_who_write_dkp)
# async def constructor_choosing_cost(message: Message, state: FSMContext):
#     await state.update_data(chosen_college_fio=db_sql_buy_with_college(message.text.lower()))
#     if db_sql_buy_with_college(message.text.lower()) == "Некорректный USERNAME":
#         await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
#         callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
#         callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
#     )
#     await message.answer(text="КТО ПИСАЛ ДКП?", reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_cost)


@router.callback_query(SetReport.choosing_self_college_dkp, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_fio="САМ")
    just = callback.message.text.upper()
    await state.update_data(chosen_college=callback.data, chosen_cost=re.sub("[^0-9]", "", just))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
    )
    # builder.add(types.InlineKeyboardButton(
    #     text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
    #     callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    # )
    await callback.message.edit_text(text="КТО ПИСАЛ ДКП?", reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_cost)


# @router.message(SetReport.choosing_cost)
# async def constructor_choosing_wire(message: Message, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Следующий шаг",
#         callback_data="bt_constructor_55_college_self")
#     )
#     await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST, reply_markup=builder.as_markup())
#     await state.update_data(chosen_wire=message.text.upper())
#     await state.set_state(SetReport.choosing_wire)

# @router.callback_query(SetReport.choosing_cost, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
# async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(chosen_college_dkp=callback.data)
#     await callback.message.edit_text(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
#     await state.set_state(SetReport.choosing_wire)
# @router.callback_query(SetReport.choosing_cost, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
# async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(chosen_college_fio=callback.message.text)
#     await state.update_data(chosen_college_dkp=callback.data)
#     await callback.message.edit_text(text="Введите тег коллеги")
#     await state.set_state(SetReport.choosing_cost1)


@router.message(SetReport.choosing_cost1)
async def constructor_choosing_cost222(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_fio=college_name)
    await state.update_data(chosen_college_dkps=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.callback_query(SetReport.choosing_cost, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_fio_dkp="САМ")
    await state.update_data(chosen_college_dkps=callback.data)
    await callback.message.edit_text(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.message(SetReport.choosing_wire)
async def constructor_choosing_wire2(message: Message, state: FSMContext):
    just = message.text.upper()
    await state.update_data(chosen_cost=re.sub("[^0-9]", "", just))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_6_WIRE_YES,
        callback_data=texts.BT_CONSTRUCTOR_6_WIRE_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_6_WIRE_NO,
        callback_data=texts.BT_CONSTRUCTOR_6_WIRE_NO)
    )
    await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_6_WIRE, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_comment)


@router.message(SetReport.choosing_wire_cost)
async def constructor_choosing_wire2(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_dkps=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.callback_query(SetReport.choosing_comment)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_wire=callback.data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_editor)


# @router.message(SetReport.choosing_wire123)
# async def constructor_choosing_wire12(message: Message, state: FSMContext):
#     await state.update_data(chosen_wire23456=message.text)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Да",
#         callback_data="bt_constructor_6_wire_yes")
#     )
#     await message.answer(text="Все?", reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_wire123232323)


@router.message(SetReport.choosing_editor)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="bt_constructor_7_edit111")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="bt_constructor_7_save"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде продал: {data['chosen_place']}\nОдин или с коллегой: {data['chosen_college']}\nФИО Коллеги: {data['chosen_college_fio']}\nКто писал дкп: {data['chosen_college_dkps']}\nЦена: {data['chosen_cost']}\nРезина есть?: {data['chosen_wire']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\n{message.chat.first_name + " " + message.chat.last_name}
        '''
    for i in data:
        print(i, "----", data[i])

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_start, F.data == "bt_constructor_7_save")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_editor_start)
async def constructor_choosing_awa_our_credit424(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Где продал",
        callback_data="edit_menu_where"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Цена",
        callback_data="edit_menu_cost"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Гос номер",
        callback_data="edit_menu_gosnumber"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Марка",
        callback_data="edit_menu_marka"
    ))
    builder.row(types.InlineKeyboardButton(
        text="Модель",
        callback_data="edit_menu_model"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Год",
        callback_data="edit_menu_year"
    ))
    builder.add(types.InlineKeyboardButton(
        text="VIN",
        callback_data="edit_menu_vin"
    ))
    builder.add(types.InlineKeyboardButton(
        text="Комментарий",
        callback_data="edit_menu_comment"
    ))
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="bt_constructor_7_save"
    ))
    data = await state.get_data()
    # text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде продал: {data['chosen_place']}\nОдин или с коллегой: {data['chosen_college']}\nФИО Коллеги: {data['chosen_college_fio']}\nКто писал дкп: {data['chosen_college_dkp']}\nЦена: {data['chosen_cost']}\nРезина есть?: {data['chosen_wire']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
    #     '''
    text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде продал: {data['chosen_place']}\nОдин или с коллегой: {data['chosen_college']}\nФИО Коллеги: {data['chosen_college_fio']}\nКто писал дкп: {data['chosen_college_dkps']}\nЦена: {data['chosen_cost']}\nРезина есть?: {data['chosen_wire']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
        '''
    for i in data:
        print(i)
    await callback.message.answer(
        text=text,
    )
    await callback.message.answer(
        text="Какое поле хотите изменить?",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_editor_first)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_where")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_ATP,
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_ABAKAN,
        callback_data=texts.BT_CONSTRUCTOR_2_ABAKAN)
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_PLANETA,
        callback_data=texts.BT_CONSTRUCTOR_2_PLANETA)
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_ALIEN,
        callback_data=texts.BT_CONSTRUCTOR_2_ALIEN)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_GETOUT,
        callback_data=texts.BT_CONSTRUCTOR_2_GETOUT)
    )
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_place'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_first_place)


@router.callback_query(SetReport.choosing_editor_first_place)
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_place=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    await callback.message.answer(text="Замена на " + callback.data, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_cost")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_cost'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_first_cost)


@router.message(SetReport.choosing_editor_first_cost)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_cost=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_cost'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_gosnumber")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_gos_number'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_first_vin_gos_number)


@router.message(SetReport.choosing_editor_first_vin_gos_number)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_gos_number=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_gos_number'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_marka")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_marka'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_first_vin_marka)


@router.message(SetReport.choosing_editor_first_vin_marka)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_marka=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_marka'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_model")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_model'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_first_vin_model)


@router.message(SetReport.choosing_editor_first_vin_model)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_model=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_model'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_year")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_year'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_first_vin_year)


@router.message(SetReport.choosing_editor_first_vin_year)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_year=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_year'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_vin")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_number'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_first_vin_number)


@router.message(SetReport.choosing_editor_first_vin_number)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_number=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_number'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "edit_menu_comment")
async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_comment'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
    await state.set_state(SetReport.choosing_editor_start)


@router.message(SetReport.choosing_editor_first_comment)
async def constructor_choosing_electro(message: Message, state: FSMContext):
    await state.update_data(chosen_comment=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_comment'], reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_editor_start)


@router.callback_query(SetReport.choosing_editor_first, F.data == "bt_constructor_7_save")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()

#
# @router.message(SetReport.choosing_electro, F.photo)
# async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.MESSAGE_IN_MAIN_MENU,
#         callback_data="main_menu")
#     )
#     await bot.download(
#         message.photo[-1],
#         destination=f"tmp/{message.photo[-1].file_id}.jpg"
#
#     )
#     await message.answer(text="Подождите пожалуйста", reply_markup=builder.as_markup())
#     convert.convert_json_japan(f"tmp/{message.photo[-1].file_id}.jpg")
#     msg = api.get_strings_japan()
#     # print(msg)
#     doka = []
#     electro_vin = 'UNKNOWN'
#     for i in msg:
#         if i["lines"][0]["words"][0]["text"]:
#             doka.append(i["lines"][0]["words"][0]["text"])
#     print(doka)
#     for k in doka:
#         if len(k) == 14 and str(k[13]).isdigit():
#             electro_vin = str(k).upper()
#             print(electro_vin)
#     msg2 = f'''В базу внесено:
#     VIN {electro_vin}
#     '''
#     # await message.answer(text=texts.MESSAGE_MAIN_MENU_VIN, reply_markup=builder.as_markup())
#     await message.answer(text=msg2, reply_markup=builder.as_markup())
#     await state.clear()
#
#
# @router.message(SetReport.choosing_report)
# async def cb_place_ad(message: Message, state: FSMContext):
#     global sender_marka, sender_model, sender_year, sender_our, sender_fio, sender_cost, sender_drom, sender_own, sender_torg, sender_fio2, sender_dkpfio, sender_commi, sender_agent
#     sample_data = message.text
#     print(sample_data)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.MESSAGE_IN_MAIN_MENU,
#         callback_data="main_menu")
#     )
#     try:
#         sender_fio = re.findall(template_fio, sample_data)
#         sender_marka = re.findall(template_marka, sample_data)
#         sender_model = re.findall(template_model, sample_data)
#         sender_year = re.findall(template_year, sample_data)
#         sender_our = re.findall(template_our, sample_data)
#         sender_cost = re.findall(template_cost, sample_data)
#         sender_drom = re.findall(template_drom, sample_data)
#         sender_own = re.findall(template_own, sample_data)
#         sender_torg = re.findall(template_torg, sample_data)
#         sender_fio2 = re.findall(template_fio2, sample_data)
#         sender_dkpfio = re.findall(template_dkpfio, sample_data)
#         sender_commi = re.findall(template_commi, sample_data)
#         sender_agent = re.findall(template_agent, sample_data)
#         print(sender_fio[0])
#         print(sender_marka[0])
#         print(sender_model[0])
#         print(sender_year[0])
#         print(sender_our[0])
#         print(sender_cost[0])
#         print(sender_drom[0])
#         print(sender_own[0])
#         print(sender_torg[0])
#         print(sender_fio2[0])
#         print(sender_dkpfio[0])
#         print(sender_commi[0])
#         print(sender_agent[0])
#         text = f'''ФИО: {sender_fio[0]}\nМарка: {sender_marka[0]}\nМодель: {sender_model[0]}\nГод: {sender_year[0]}\nНаша/комиссия: {sender_our[0]}\nЦена продажи: {sender_cost[0]}\nСколько накинул на цену дрома: {sender_drom[0]}\nСколько собственнику: {sender_own[0]}\nДо скольки сторговали собственника: {sender_torg[0]}\nС кем продал ФИО: {sender_fio2[0]}\nДКП ФИО: {sender_dkpfio[0]}\nКто ставил на комиссию: {sender_commi[0]}\nКто писал агентский договор:{sender_agent[0]}
#         '''
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text=texts.MESSAGE_IN_MAIN_MENU,
#             callback_data="main_menu")
#         )
#         await message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_EXIT)
#         await message.answer(text=text)
#     except IndexError as error:
#         print(error)
#         await message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_CANCEL)
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text=texts.MESSAGE_IN_MAIN_MENU,
#             callback_data="main_menu")
#         )

# try:
# conn = psycopg2.connect(user=os.environ['SQL_USER'],
#                         password=os.environ['SQL_PASSWORD'],
#                         host=os.environ['SQL_HOST'],
#                         port=os.environ['SQL_PORT'],
#                         database=os.environ['SQL_DATABASE']
#                         )
#     cur = conn.cursor()
#     print(f'Статус подключение к бд {conn.closed}')
#     sql_insert_data_otchet = 'INSERT INTO bot_vitek.wb_otchet_data(city, full_name, route_number, date_otchet, start_otchet, finish_otchet, waybill_number, amount_shk, loader, amount_flight) VALUES (%s,%s, %s,%s,%s, %s, %s, %s,%s,%s)'
#     cur.execute(sql_insert_data_otchet, (
#         city[0], full_name[0], route_number[0], date_otchet[0], start_otchet[0], finish_otchet[0],
#         waybill_number[0],
#         amount_shk[0], loader[0], amount_flight[0],))
#     conn.commit()
#     count = cur.rowcount
#     print(count, "Record inserted successfully into mobile table")
#     update.message.reply_text('Отчет отправлен!', reply_markup=main_keyboard())
#     conn.close()
#     await state.set_state(SetReport.choosing_exit)
# except (Exception, psycopg2.Error) as error:
#     print("Failed to insert record into mobile table", error)
#     await state.clear()
# await state.clear()

# def get_report_excel(update, context):
#     update.message.reply_text('Ваш отчет:')
#     try:
# conn = psycopg2.connect(user=os.environ['SQL_USER'],
#                         password=os.environ['SQL_PASSWORD'],
#                         host=os.environ['SQL_HOST'],
#                         port=os.environ['SQL_PORT'],
#                         database=os.environ['SQL_DATABASE']
#                         )
#         cur1 = conn1.cursor()
#         print(f'Статус подключение к бд {conn1.closed}')
#         cur1.execute(
#             'SELECT city, full_name, route_number, date_otchet, waybill_number, amount_shk, loader, amount_flight from bot_vitek.wb_otchet_data_2 where date_otchet >= %s and  date_otchet <=%s ',
#             ('2022-11-12', '2022-11-14',))
#         # sql = '''select * from bot_vitek.wb_otchet_data;'''
#         # cur.execute(sql)
#         results = cur1.fetchall()
#         print(results)
#         conn1.close()
#     except (Exception, psycopg2.Error) as error:
#         print("Failed to insert record into mobile table", error)
