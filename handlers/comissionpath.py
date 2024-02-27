from aiogram import Router, F, types, Bot
from aiogram.filters import command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher
# from utils.editor_comission import router
from utils import editor_comission

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

    # choosing_comission_editor = State()
    # choosing_comission_editor_start = State()
    # choosing_comission_editor = State()
    # choosing_comission_editor_start = State()
    # choosing_comission_editor_first = State()
    # choosing_comission_editor_first_place = State()
    # choosing_comission_editor_first_cost = State()
    # choosing_comission_editor_first_vin_gos_number = State()
    # choosing_comission_editor_first_vin_marka = State()
    # choosing_comission_editor_first_vin_model = State()
    # choosing_comission_editor_first_vin_year = State()
    # choosing_comission_editor_first_vin_number = State()
    # choosing_comission_editor_first_comment = State()
    # choosing_comission_editor_finish = State()


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

    await callback.message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_1_COMISSION, reply_markup=builder.as_markup())
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
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        await message.answer(text="Укажите гоc номер")
        await state.set_state(SetReport.choosing_comission_data_car_next)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(text="Укажите год")
        await state.set_state(SetReport.choosing_comission_data_car_gosnumber)


# @router.message(SetReport.choosing_comission_data_car_gosnumber)
# async def main_menu_button2(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_year=message.text.upper())
#     await message.answer(text="Укажите гоc номер")
#     await state.set_state(SetReport.choosing_comission_data_car_next)


@router.message(SetReport.choosing_comission_data_car_next)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_gos_number=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_EDIT,
        callback_data=texts.BT_EDIT)
    )
    data = await state.get_data()
    text = f'''Вы указали:
    Год {str(data['chosen_vin_year']).upper()}
    Гос номер {str(data['chosen_vin_gos_number']).upper()}
    VIN {str(data['chosen_vin_number']).upper()}
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


@router.callback_query(SetReport.choosing_comission_self_college, F.data == texts.BT_EDIT)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Укажите VIN")
    await state.set_state(SetReport.choosing_comission_data_car_marka)


@router.callback_query(SetReport.choosing_comission_self_college, F.data == texts.BT_NEXT)
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
    college_name = message.text.lower()
    await state.update_data(chosen_college_fio=college_name)
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
    await state.update_data(chosen_college_fio=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    await state.update_data(
        chosen_college_dkps=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    await callback.message.edit_text(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


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
    await state.update_data(chosen_college_fio=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
        callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    )

    await callback.message.edit_text(text=texts.MESSAGE_KTO_PISAL_AG, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_comission_cost_inline)


@router.message(SetReport.choosing_dkp004)
async def constructor_choosing_cost222(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text)
    await state.update_data(chosen_college_dkps=college_name)
    if str(college_name).startswith('<'):
        await message.answer("Менеджера нет в базе, укажите корректные данные в режиме редактирования")
        await state.update_data(chosen_college_dkps=message.text)
    await message.answer(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


@router.message(SetReport.choosing_comission_cost1)
async def constructor_choosing_cost222(message: Message, state: FSMContext):
    college_name = message.text
    await state.update_data(chosen_college_fio=college_name)
    if str(college_name).startswith('<'):
        await message.answer("Менеджера нет в базе, укажите корректные данные в режиме редактирования")
        await state.update_data(chosen_college_fio=message.text)
    await message.answer(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


@router.callback_query(SetReport.choosing_comission_cost, F.data == texts.BT_CONSTRUCTOR_4_COLLEGE_SELF)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(
        chosen_college_fio_dkp=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    await state.update_data(chosen_college_dkps=callback.data)
    await callback.message.edit_text(text=texts.MESSAGE_HOW_MUCH_SOBS)
    await state.set_state(SetReport.choosing_dkp04)


@router.message(SetReport.choosing_dkp04)
async def constructor_choosing_dkp4(message: Message, state: FSMContext):
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(howmuchsobs=int(just))
        await message.answer(text=texts.MESSAGE_HOW_MUCH_COMISSION)
        await state.set_state(SetReport.choosing_comment)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_HOW_MUCH_SOBS,
        )
        await state.set_state(SetReport.choosing_dkp04)


@router.message(SetReport.choosing_comment)
async def constructor_choosing_wire(message: Message, state: FSMContext):
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(howmuchcomissiob=int(just))
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
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_HOW_MUCH_COMISSION,
        )
        await state.set_state(SetReport.choosing_comment)


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
    await state.set_state(SetReport.choosing_comission_editor)


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


# =============================================================
@router.callback_query(SetReport.choosing_comission_editor)
async def constructor_choosing_wire12(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(typeraschet=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_SAVE,
        callback_data="edit_menu_finish")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_EDIT,
        callback_data=texts.BT_EDIT)
    )
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде продал: {data['chosen_place']}\nКто купил: {data['chosen_college_fio']}\nКто писал АГ: {data['chosen_college_dkps']}\nСколько собственнику: {data['howmuchsobs']}\nРазмер комиссии?: {data['howmuchcomissiob']}\n\nВид расчета?: {data['typeraschet']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарии: {data['chosen_comment']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
        '''

    await callback.message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_start, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Подождите, идет выгрузка отчета")
    data = await state.get_data()
    await utils.connectors.db_sql_comission_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления но1вого отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_comission_editor_start)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    dict_editor = {'editor_start':
                       {'text': ["Где продал", "Сколько собственнику", "Гос номер", "Марка", "Модель", "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_where", "edit_menu_howmuchsobs", "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_comission.editor_start(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_comission_editor_first)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_where")
async def editor_first_where(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first(callback, state)
    await state.set_state(SetReport.choosing_comission_editor_first_place)


@router.callback_query(SetReport.choosing_comission_editor_first_place)
async def editor_first_place(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_place(callback, state)
    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_howmuchsobs")
async def editor_first(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_howmuchsobs(callback, state)
    await state.set_state(SetReport.choosing_comission_editor_first_cost)


@router.message(SetReport.choosing_comission_editor_first_cost)
async def editor_first_cost(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_cost(message, state)
    # await state.set_state(SetReport.choosing_comission_editor_start)


#
#
@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_gosnumber")
async def editor_first_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_comission_editor_first_vin_gos_number)


@router.message(SetReport.choosing_comission_editor_first_vin_gos_number)
async def editor_first_vin_gos_number(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_vin_gos_number(message, state)

    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_marka")
async def editor_first_marka(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_marka(callback, state)

    await state.set_state(SetReport.choosing_comission_editor_first_vin_marka)


@router.message(SetReport.choosing_comission_editor_first_vin_marka)
async def editor_first_vin_marka(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_vin_marka(message, state)

    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_model")
async def editor_first_model(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_model(callback, state)

    await state.set_state(SetReport.choosing_comission_editor_first_vin_model)


@router.message(SetReport.choosing_comission_editor_first_vin_model)
async def editor_first_vin_model(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_vin_model(message, state)

    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_year")
async def editor_first_year(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_year(callback, state)

    await state.set_state(SetReport.choosing_comission_editor_first_vin_year)


@router.message(SetReport.choosing_comission_editor_first_vin_year)
async def editor_first_vin_year(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_vin_year(message, state)

    # await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_vin")
async def editor_first_menu_vin(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_menu_vin(callback, state)

    await state.set_state(SetReport.choosing_comission_editor_first_vin_number)


@router.message(SetReport.choosing_comission_editor_first_vin_number)
async def editor_first_vin_number(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_vin_number(message, state)

    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_comment")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_comission.editor_first_menu_comment(callback, state)

    await state.set_state(SetReport.choosing_comission_editor_first_comment)


@router.message(SetReport.choosing_comission_editor_first_comment)
async def editor_first_comment(message: Message, state: FSMContext):
    await utils.editor_comission.editor_first_comment(message, state)

    await state.set_state(SetReport.choosing_comission_editor_start)


@router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Подождите, идет выгрузка отчета")
    data = await state.get_data()
    await utils.connectors.db_sql_comission_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()

# ================================================================
# @router.callback_query(SetReport.choosing_comission_editor_start)
# async def constructor_choosing_awa_our_credit424(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Где продал",
#         callback_data="edit_menu_where"
#     ))
#     builder.add(types.InlineKeyboardButton(
#         text="Сколько собственнику",
#         callback_data="howmuchsobs"
#     ))
#     builder.add(types.InlineKeyboardButton(
#         text="Гос номер",
#         callback_data="edit_menu_gosnumber"
#     ))
#     builder.add(types.InlineKeyboardButton(
#         text="Марка",
#         callback_data="edit_menu_marka"
#     ))
#     builder.row(types.InlineKeyboardButton(
#         text="Модель",
#         callback_data="edit_menu_model"
#     ))
#     builder.add(types.InlineKeyboardButton(
#         text="Год",
#         callback_data="edit_menu_year"
#     ))
#     builder.add(types.InlineKeyboardButton(
#         text="VIN",
#         callback_data="edit_menu_vin"
#     ))
#     builder.add(types.InlineKeyboardButton(
#         text="Комментарий",
#         callback_data="edit_menu_comment"
#     ))
#     builder.row(types.InlineKeyboardButton(
#         text="Все ок",
#         callback_data=texts.BT_SAVE
#     ))
#     data = await state.get_data()
#     text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде продал: {data['chosen_place']}\nКто купил: {data['chosen_college_fio']}\nКто писал АГ: {data['chosen_college_dkps']}\nСколько собственнику: {data['howmuchsobs']}\nРазмер комиссии?: {data['howmuchcomissiob']}\n\nВид расчета?: {data['typeraschet']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#         '''
#
#     await callback.message.answer(
#         text=text,
#     )
#     await callback.message.answer(
#         text="Какое поле хотите изменить?",
#         reply_markup=builder.as_markup()
#     )
#     await state.set_state(SetReport.choosing_comission_editor_first)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_where")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_2_ATP,
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_2_ABAKAN,
#         callback_data=texts.BT_CONSTRUCTOR_2_ABAKAN)
#     )
#     builder.row(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_2_PLANETA,
#         callback_data=texts.BT_CONSTRUCTOR_2_PLANETA)
#     )
#     builder.row(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_2_ALIEN,
#         callback_data=texts.BT_CONSTRUCTOR_2_ALIEN)
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_2_GETOUT,
#         callback_data=texts.BT_CONSTRUCTOR_2_GETOUT)
#     )
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_place'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2, reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_first_place)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first_place)
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(chosen_place=callback.data)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     await callback.message.answer(text="Замена на " + callback.data, reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_howmuchsobs")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['howmuchsobs'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_first_cost)
#
#
# @router.message(SetReport.choosing_comission_editor_first_cost)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(howmuchsobs=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['howmuchsobs'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_gosnumber")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_vin_gos_number'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_first_vin_gos_number)
#
#
# @router.message(SetReport.choosing_comission_editor_first_vin_gos_number)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_gos_number=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['chosen_vin_gos_number'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_marka")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_vin_marka'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_first_vin_marka)
#
#
# @router.message(SetReport.choosing_comission_editor_first_vin_marka)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_marka=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['chosen_vin_marka'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_model")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_vin_model'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_first_vin_model)
#
#
# @router.message(SetReport.choosing_comission_editor_first_vin_model)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_model=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['chosen_vin_model'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_year")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_vin_year'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_first_vin_year)
#
#
# @router.message(SetReport.choosing_comission_editor_first_vin_year)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_year=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['chosen_vin_year'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_vin")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_vin_number'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_first_vin_number)
#
#
# @router.message(SetReport.choosing_comission_editor_first_vin_number)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_number=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['chosen_vin_number'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.callback_query(SetReport.choosing_comission_editor_first, F.data == "edit_menu_comment")
# async def constructor_choosing_electro(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     msg2 = "В данный момент используется " + data['chosen_comment'] + ", на какое значение хотите изменить?"
#     await callback.message.answer(text=msg2)
#     await state.set_state(SetReport.choosing_comission_editor_start)
#
#
# @router.message(SetReport.choosing_comission_editor_first_comment)
# async def constructor_choosing_electro(message: Message, state: FSMContext):
#     await state.update_data(chosen_comment=message.text.upper())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="ОК",
#         callback_data=texts.BT_CONSTRUCTOR_2_ATP)
#     )
#     data = await state.get_data()
#     await message.answer(text="Замена на " + data['chosen_comment'], reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comission_editor_start)
