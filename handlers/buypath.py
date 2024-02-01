from pydoc import html
from typing import Optional

import psycopg2
import os
from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineQueryResultArticle, InputTextMessageContent, InlineQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import utils
from utils import downloader, connectors, convert, api, inliner
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
    await callback.message.edit_text(text=texts.MESSAGE_PHOTO_VIN_DOWNLOAD, reply_markup=builder.as_markup())
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
    await utils.downloader.constructor_choosing_vin(message, state, bot)
    await state.set_state(SetReport.choosing_self_college)


@router.message(SetReport.choosing_pts, F.photo)
async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    await utils.downloader.constructor_choosing_electro(message, state, bot)
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
        switch_inline_query_current_chat='find_a ')
    )
    await callback.message.edit_text(text="Введите первые символы фамилии коллеги", reply_markup=builder.as_markup())
    await state.update_data(chosen_college=callback.data)
    await state.set_state(SetReport.choosing_who_write_dkp0)


@router.message(SetReport.choosing_who_write_dkp0)
@router.inline_query(lambda query: query.query.startswith("find_a "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    await utils.inliner.find_colleges(inline_query, state, "find_a ")
    await state.set_state(SetReport.choosing_who_write_dkp_inline)


@router.message(SetReport.choosing_who_write_dkp_inline)
async def constructor_choosing_cost(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
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
    await state.update_data(chosen_college_dkps=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    await callback.message.edit_text(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.callback_query(SetReport.choosing_cost_inline, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_aa ')
    )
    await callback.message.edit_text(text="Введите первые символы фамилии коллеги", reply_markup=builder.as_markup())
    # await state.update_data(chosen_college=callback.data)
    await state.set_state(SetReport.choosing_who_write_dkp_inline)


@router.message(SetReport.choosing_who_write_dkp_inline)
@router.inline_query(lambda query: query.query.startswith("find_aa "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    await utils.inliner.find_colleges(inline_query, state, "find_aa ")
    await state.set_state(SetReport.choosing_wire_cost)


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


@router.message(SetReport.choosing_cost1)
async def constructor_choosing_cost222(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_fio=college_name)
    await state.update_data(chosen_college_dkps=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.callback_query(SetReport.choosing_cost, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_fio_dkp=callback.message.chat.last_name + " " + callback.message.chat.first_name)
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
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_dkps=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_wire)


@router.callback_query(SetReport.choosing_comment, F.data == texts.BT_CONSTRUCTOR_6_WIRE_YES)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_wire=callback.data, chosen_wire_boolean=True)
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


@router.callback_query(SetReport.choosing_comment, F.data == texts.BT_CONSTRUCTOR_6_WIRE_NO)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_wire=callback.data, chosen_wire_boolean=False)
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
    data = await state.get_data()

    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )

    cur = conn.cursor()

    if conn.closed == 0:

        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.purchase_report(type_purchase_report, platform,username_purchase_сolleagues,write_dkp,price,tires,vin,gos_number,brand,model,years,comment_report,username_purchase_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_tg_info_user, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'],
            data['chosen_cost'], data['chosen_wire_boolean'], data['chosen_vin_number'],
            data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
            data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
    else:
        print(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()
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
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext, dict_report):
    data = await state.get_data()
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.purchase_report(type_purchase_report, platform,username_purchase_сolleagues,write_dkp,price,tires,vin,gos_number,brand,model,years,comment_report,username_purchase_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_tg_info_user, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'],
            data['chosen_cost'], data['chosen_wire_boolean'], data['chosen_vin_number'],
            data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
            data['chosen_comment'], callback.message.chat.last_name + " " + callback.message.chat.first_name,))
    else:
        print(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()
