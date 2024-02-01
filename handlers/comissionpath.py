from aiogram import Router, F, types, Bot
from aiogram.filters import command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
import psycopg2
import os

import utils
from utils import downloader, connectors, convert, api, inliner
from texts import texts

router = Router()

import re


class SetReport(StatesGroup):
    choosing_comission_buyer = State()
    choosing_comission_data_car = State()
    choosing_comission_vin = State()
    choosing_comission_pts = State()
    choosing_comission_japan = State()
    choosing_comission_data_car_marka = State()
    choosing_comission_data_car_model = State()
    choosing_comission_data_car_year = State()
    choosing_comission_data_car_gosnumber = State()
    choosing_comission_data_car_next = State()
    choosing_comission_self_college = State()
    choosing_comission_self_college_dkp = State()
    choosing_comission_who_write_dkp0 = State()
    choosing_comission_who_write_dkp = State()
    choosing_comission_cost = State()
    choosing_comission_cost1 = State()
    choosing_comission_wire = State()
    choosing_comission_wire_cost = State()
    choosing_comission_comment = State()
    choosing_comission_who_write_dkp_inline = State()
    choosing_comission_cost_inline = State()
    choosing_dkp004 = State()
    choosing_dkp04 = State()
    choosing_dkp06 = State()
    choosing_wire02 = State()
    choosing_wire03 = State()
    choosing_comment = State()

    choosing_comission_editor = State()
    choosing_comission_editor_start = State()
    choosing_comission_editor_first = State()
    choosing_comission_editor_first_place = State()
    choosing_comission_editor_first_cost = State()
    choosing_comission_editor_first_vin_gos_number = State()
    choosing_comission_editor_first_vin_marka = State()
    choosing_comission_editor_first_vin_model = State()
    choosing_comission_editor_first_vin_year = State()
    choosing_comission_editor_first_vin_number = State()
    choosing_comission_editor_first_comment = State()
    choosing_comission_editor_finish = State()


@router.callback_query(F.data == "bt_constructor_2_comission")
async def main_menu_bt_constructor_2_comission(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_type="КОМИССИЯ")
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
    await state.set_state(SetReport.choosing_comission_buyer)
    await callback.message.delete()


@router.callback_query(SetReport.choosing_comission_buyer)
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
    await state.set_state(SetReport.choosing_comission_data_car)


@router.callback_query(SetReport.choosing_comission_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON2)
    await state.set_state(SetReport.choosing_comission_vin)


@router.callback_query(SetReport.choosing_comission_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON22)
    await state.set_state(SetReport.choosing_comission_pts)


@router.callback_query(SetReport.choosing_comission_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Укажите VIN")
    await state.set_state(SetReport.choosing_comission_data_car_marka)


@router.message(SetReport.choosing_comission_data_car_marka)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_number=message.text.upper())
    await message.answer(text="Укажите марку")
    await state.set_state(SetReport.choosing_comission_data_car_model)


@router.message(SetReport.choosing_comission_data_car_model)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_marka=message.text.upper())
    await message.answer(text="Укажите модель")
    await state.set_state(SetReport.choosing_comission_data_car_year)


@router.message(SetReport.choosing_comission_data_car_year)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_model=message.text.upper())
    await message.answer(text="Укажите год")
    await state.set_state(SetReport.choosing_comission_data_car_gosnumber)


@router.message(SetReport.choosing_comission_data_car_gosnumber)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_year=message.text.upper())
    await message.answer(text="Укажите гоc номер")
    await state.set_state(SetReport.choosing_comission_data_car_next)


@router.message(SetReport.choosing_comission_data_car_next)
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
    await state.set_state(SetReport.choosing_comission_self_college)


@router.message(SetReport.choosing_comission_vin, F.photo)
async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
    await utils.downloader.constructor_choosing_vin(message, state, bot)

    await state.set_state(SetReport.choosing_comission_self_college)


@router.message(SetReport.choosing_comission_pts, F.photo)
async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    await utils.downloader.constructor_choosing_electro(message, state, bot)

    await state.set_state(SetReport.choosing_comission_self_college)


@router.callback_query(SetReport.choosing_comission_self_college)
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
    await state.set_state(SetReport.choosing_comission_self_college_dkp)


@router.callback_query(SetReport.choosing_comission_self_college_dkp, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_c ')
    )
    await callback.message.edit_text(text="Введите первые символы фамилии коллеги", reply_markup=builder.as_markup())
    await state.update_data(chosen_college=callback.data)
    await state.set_state(SetReport.choosing_comission_who_write_dkp0)


@router.message(SetReport.choosing_comission_who_write_dkp0)
@router.inline_query(lambda query: query.query.startswith("find_c "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    await utils.inliner.find_colleges(inline_query, state, "find_c ")
    await state.set_state(SetReport.choosing_comission_who_write_dkp_inline)


@router.message(SetReport.choosing_comission_who_write_dkp_inline)
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
    await message.answer(text=texts.MESSAGE_KTO_PISAL_AG, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_comission_cost_inline)


@router.callback_query(SetReport.choosing_comission_cost_inline, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_cost222(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_dkps="САМ")
    await callback.message.edit_text(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST)
    await state.set_state(SetReport.choosing_comission_wire)


@router.callback_query(SetReport.choosing_comission_cost_inline, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_cc ')
    )
    await callback.message.edit_text(text="Введите первые символы фамилии коллеги", reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_comission_who_write_dkp_inline)


@router.message(SetReport.choosing_comission_who_write_dkp_inline)
@router.inline_query(lambda query: query.query.startswith("find_cc "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    await utils.inliner.find_colleges(inline_query, state, "find_cc ")
    await state.set_state(SetReport.choosing_dkp004)


@router.callback_query(SetReport.choosing_comission_self_college_dkp, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_fio="САМ")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
    )

    await callback.message.edit_text(text=texts.MESSAGE_KTO_PISAL_AG, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_dkp04)


@router.message(SetReport.choosing_dkp004)
async def constructor_choosing_cost222(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_dkps=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    await message.answer(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


@router.message(SetReport.choosing_comission_cost1)
async def constructor_choosing_cost222(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(chosen_college_fio=college_name)
    await state.update_data(chosen_college_dkps=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    await message.answer(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


@router.callback_query(SetReport.choosing_comission_cost, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_college_fio_dkp="САМ")
    await state.update_data(chosen_college_dkps=callback.data)
    await callback.message.edit_text(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


@router.message(SetReport.choosing_dkp04)
async def constructor_choosing_dkp4(message: Message, state: FSMContext):
    await state.update_data(howmuchsobs=message.text.upper())
    await message.answer(text=texts.MESSAGE_HOW_MUCH_COMISSION)
    await state.set_state(SetReport.choosing_comment)


@router.message(SetReport.choosing_comment)
async def constructor_choosing_wire(message: Message, state: FSMContext):
    await state.update_data(howmuchcomissiob=message.text.upper())
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_dkp06)


#
@router.message(SetReport.choosing_dkp06)
async def constructor_choosing_dkp5(message: Message, state: FSMContext):
    await state.update_data(chosen_comment=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CASH,
        callback_data=texts.BT_CASH)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NOTCASH,
        callback_data=texts.BT_NOTCASH)
    )
    await message.answer(text=texts.MESSAGE_TYPE_RASHCHET, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_wire02)


@router.callback_query(SetReport.choosing_wire02)
async def constructor_choosing_awa_our_credit22(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(typeraschet=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_SAVE,
        callback_data=texts.BT_SAVE)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_EDIT,
        callback_data=texts.BT_EDIT)
    )
    data = await state.get_data()
    print(data)
    text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде продал: {data['chosen_place']}\nКто купил: {data['chosen_college_fio']}\nКто писал АГ: {data['chosen_college_dkps']}\nСколько собственнику: {data['howmuchsobs']}\nРазмер комиссии?: {data['howmuchcomissiob']}\n\nВид расчета?: {data['typeraschet']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
        '''
    await callback.message.answer(
        text=text
    )
    await callback.message.answer(
        text="Сохранить?",
        reply_markup=builder.as_markup()
    )
    # Устанавливаем пользователю состояние "выбирает марку и модель"
    await state.set_state(SetReport.choosing_wire03)


@router.callback_query(SetReport.choosing_wire03, F.data == texts.BT_SAVE)
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
        sql_insert_comission_report = 'INSERT INTO bot_planeta_avto.commission_report(type_purchase_report, platform, username_commission_сolleagues, write_ag,price_owner, size_commission, vin, gos_number, brand, model, years, comment_report, username_commission_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_comission_report, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'], data['howmuchsobs'], data['howmuchcomissiob'],
            data['chosen_vin_number'],
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


@router.callback_query(SetReport.choosing_wire03, F.data == texts.BT_EDIT)
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
        sql_insert_comission_report = 'INSERT INTO bot_planeta_avto.commission_report(type_purchase_report, platform, username_commission_сolleagues, write_ag,price_owner, size_commission, vin, gos_number, brand, model, years, comment_report, username_commission_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_comission_report, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'], data['howmuchsobs'], data['howmuchcomissiob'],
            data['chosen_vin_number'],
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


@router.message(SetReport.choosing_comission_vin, F.photo)
async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
    await utils.downloader.constructor_choosing_vin(message, state, bot)
    await state.clear()


@router.message(SetReport.choosing_comission_japan, F.photo)
async def constructor_choosing_japan(message: Message, state: FSMContext, bot: Bot):
    await utils.downloader.constructor_choosing_japan(message, state, bot)
    await state.clear()


@router.message(SetReport.choosing_comission_pts, F.photo)
async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    await utils.downloader.constructor_choosing_electro(message, state, bot)
    await state.clear()
