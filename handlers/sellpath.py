import re

from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import editor_sell

import utils
from utils import downloader, connectors, inliner
from texts import texts

router = Router()


class SetReport(StatesGroup):
    choosing_sell_selector_1 = State()
    choosing_sell_selector_2 = State()
    choosing_sell_selector_3 = State()
    choosing_sell_selector_4 = State()
    choosing_sell_selector_5 = State()
    choosing_sell_selector_6 = State()
    choosing_sell_selector_7 = State()
    choosing_sell_selector_8 = State()

    choosing_buyer1 = State()
    choosing_buyer2 = State()
    choosing_buyer3 = State()
    choosing_buyer4 = State()
    choosing_buyer5 = State()
    choosing_buyer6 = State()
    choosing_buyer7 = State()
    choosing_buyer8 = State()
    choosing_buyer9 = State()
    choosing_buyer10 = State()
    choosing_buyer11 = State()
    choosing_buyer12 = State()
    choosing_buyer13 = State()
    choosing_buyer14 = State()
    choosing_buyer15 = State()
    choosing_buyer16 = State()
    choosing_buyer17 = State()
    choosing_buyer18 = State()
    choosing_buyer19 = State()
    choosing_buyer20 = State()
    choosing_sell_data_car_start = State()
    choosing_sell_data_comission_car = State()
    choosing_sell_comission_vin = State()
    choosing_sell_comission_pts = State()
    choosing_sell_comission_data_car_marka = State()
    choosing_sell_comission_data_car_model = State()
    choosing_sell_comission_data_car_year = State()
    choosing_sell_comission_data_car_gosnumber = State()
    choosing_sell_comission_data_car_next = State()
    choosing_sell_data_our_car = State()
    choosing_sell_our_vin = State()
    choosing_sell_our_pts = State()
    choosing_sell_our_data_car_marka = State()
    choosing_sell_our_data_car_model = State()
    choosing_sell_our_data_car_year = State()
    choosing_sell_our_data_car_gosnumber = State()
    choosing_sell_our_data_car_next = State()
    choosing_vin_editor_first_sell_comission = State()
    choosing_vin_editor_vin_sell_comission = State()
    choosing_vin_editor_gos_number_sell_comission = State()
    choosing_vin_editor_year_sell_comission = State()
    choosing_vin_editor_marka_sell_comission = State()
    choosing_vin_editor_model_sell_comission = State()
    choosing_vin_editor_start_sell_comission = State()
    choosing_vin_editor_first_sell_our = State()
    choosing_vin_editor_vin_sell_our = State()
    choosing_vin_editor_gos_number_sell_our = State()
    choosing_vin_editor_year_sell_our = State()
    choosing_vin_editor_marka_sell_our = State()
    choosing_vin_editor_model_sell_our = State()
    choosing_vin_editor_start_sell_our = State()
    choosing_our_our = State()
    choosing_our_our44444 = State()
    choosing_comissiya_our44444 = State()
    choosing_comissiya_our22 = State()
    choosing_comissiya_our33 = State()
    choosing_sell_self_college = State()
    choosing_sell_self_college_dkp = State()
    choosing_sell_who_write_dkp0 = State()
    choosing_sell_who_write_dkp = State()
    choosing_sell_cost = State()
    choosing_sell_cost1 = State()
    choosing_sell_wire = State()
    choosing_sell_wire_cost = State()
    choosing_sell_comment = State()
    choosing_sell_who_write_dkp_inline = State()
    choosing_sell_cost_inline = State()
    choosing_sell_editor_1_6 = State()
    choosing_sell_editor_1 = State()
    choosing_sell_editor_2 = State()
    choosing_sell_editor_3 = State()
    choosing_sell_editor_4 = State()
    choosing_sell_editor_5 = State()
    choosing_sell_editor_6 = State()
    choosing_sell_editor_7 = State()
    choosing_sell_editor_8 = State()
    choosing_sell_editor_start_1 = State()
    choosing_sell_editor_start_2 = State()
    choosing_sell_editor_start_3 = State()
    choosing_sell_editor_start_4 = State()
    choosing_sell_editor_start_5 = State()
    choosing_sell_editor_start_6 = State()
    choosing_sell_editor_start_7 = State()
    choosing_sell_editor_start_8 = State()
    choosing_sell_editor_first_place_1 = State()
    choosing_sell_editor_first_place_2 = State()
    choosing_sell_editor_first_place_3 = State()
    choosing_sell_editor_first_place_4 = State()
    choosing_sell_editor_first_place_5 = State()
    choosing_sell_editor_first_place_6 = State()
    choosing_sell_editor_first_place_7 = State()
    choosing_sell_editor_first_place_8 = State()
    choosing_sell_editor_first_cost_1 = State()
    choosing_sell_editor_first_cost_2 = State()
    choosing_sell_editor_first_cost_3 = State()
    choosing_sell_editor_first_cost_4 = State()
    choosing_sell_editor_first_cost_5 = State()
    choosing_sell_editor_first_cost_6 = State()
    choosing_sell_editor_first_cost_7 = State()
    choosing_sell_editor_first_cost_8 = State()
    choosing_sell_editor_first_vin_gos_number_1 = State()
    choosing_sell_editor_first_vin_gos_number_2 = State()
    choosing_sell_editor_first_vin_gos_number_3 = State()
    choosing_sell_editor_first_vin_gos_number_4 = State()
    choosing_sell_editor_first_vin_gos_number_5 = State()
    choosing_sell_editor_first_vin_gos_number_6 = State()
    choosing_sell_editor_first_vin_gos_number_7 = State()
    choosing_sell_editor_first_vin_gos_number_8 = State()
    choosing_sell_editor_first_vin_marka_1 = State()
    choosing_sell_editor_first_vin_marka_2 = State()
    choosing_sell_editor_first_vin_marka_3 = State()
    choosing_sell_editor_first_vin_marka_4 = State()
    choosing_sell_editor_first_vin_marka_5 = State()
    choosing_sell_editor_first_vin_marka_6 = State()
    choosing_sell_editor_first_vin_marka_7 = State()
    choosing_sell_editor_first_vin_marka_8 = State()
    choosing_sell_editor_first_vin_model_1 = State()
    choosing_sell_editor_first_vin_model_2 = State()
    choosing_sell_editor_first_vin_model_3 = State()
    choosing_sell_editor_first_vin_model_4 = State()
    choosing_sell_editor_first_vin_model_5 = State()
    choosing_sell_editor_first_vin_model_6 = State()
    choosing_sell_editor_first_vin_model_7 = State()
    choosing_sell_editor_first_vin_model_8 = State()
    choosing_sell_editor_first_vin_year_1 = State()
    choosing_sell_editor_first_vin_year_2 = State()
    choosing_sell_editor_first_vin_year_3 = State()
    choosing_sell_editor_first_vin_year_4 = State()
    choosing_sell_editor_first_vin_year_5 = State()
    choosing_sell_editor_first_vin_year_6 = State()
    choosing_sell_editor_first_vin_year_7 = State()
    choosing_sell_editor_first_vin_year_8 = State()
    choosing_sell_editor_first_vin_number_1 = State()
    choosing_sell_editor_first_vin_number_2 = State()
    choosing_sell_editor_first_vin_number_3 = State()
    choosing_sell_editor_first_vin_number_4 = State()
    choosing_sell_editor_first_vin_number_5 = State()
    choosing_sell_editor_first_vin_number_6 = State()
    choosing_sell_editor_first_vin_number_7 = State()
    choosing_sell_editor_first_vin_number_8 = State()
    choosing_sell_editor_first_comment_1 = State()
    choosing_sell_editor_first_comment_2 = State()
    choosing_sell_editor_first_comment_3 = State()
    choosing_sell_editor_first_comment_4 = State()
    choosing_sell_editor_first_comment_5 = State()
    choosing_sell_editor_first_comment_6 = State()
    choosing_sell_editor_first_comment_7 = State()
    choosing_sell_editor_first_comment_8 = State()
    choosing_sell_editor_menu_who_sell_edit_1 = State()
    choosing_sell_editor_menu_who_sell_edit_2 = State()
    choosing_sell_editor_menu_who_sell_edit_3 = State()
    choosing_sell_editor_menu_who_sell_edit_4 = State()
    choosing_sell_editor_menu_who_sell_edit_5 = State()
    choosing_sell_editor_menu_who_sell_edit_6 = State()
    choosing_sell_editor_menu_who_sell_edit_7 = State()
    choosing_sell_editor_menu_who_sell_edit_8 = State()
    choosing_sell_editor_menu_who_credit_edit_1 = State()
    choosing_sell_editor_menu_who_credit_edit_2 = State()
    choosing_sell_editor_menu_who_credit_edit_3 = State()
    choosing_sell_editor_menu_who_credit_edit_4 = State()
    choosing_sell_editor_menu_who_credit_edit_5 = State()
    choosing_sell_editor_menu_who_credit_edit_6 = State()
    choosing_sell_editor_menu_who_credit_edit_7 = State()
    choosing_sell_editor_menu_who_credit_edit_8 = State()
    choosing_sell_editor_menu_drom_cost_edit_1 = State()
    choosing_sell_editor_menu_drom_cost_edit_2 = State()
    choosing_sell_editor_menu_drom_cost_edit_3 = State()
    choosing_sell_editor_menu_drom_cost_edit_4 = State()
    choosing_sell_editor_menu_drom_cost_edit_5 = State()
    choosing_sell_editor_menu_drom_cost_edit_6 = State()
    choosing_sell_editor_menu_drom_cost_edit_7 = State()
    choosing_sell_editor_menu_drom_cost_edit_8 = State()
    choosing_sell_editor_menu_gosnumber_edit_1 = State()
    choosing_sell_editor_menu_gosnumber_edit_2 = State()
    choosing_sell_editor_menu_gosnumber_edit_3 = State()
    choosing_sell_editor_menu_gosnumber_edit_4 = State()
    choosing_sell_editor_menu_gosnumber_edit_5 = State()
    choosing_sell_editor_menu_gosnumber_edit_6 = State()
    choosing_sell_editor_menu_gosnumber_edit_7 = State()
    choosing_sell_editor_menu_gosnumber_edit_8 = State()
    choosing_sell_editor_menu_marka_edit_1 = State()
    choosing_sell_editor_menu_marka_edit_2 = State()
    choosing_sell_editor_menu_marka_edit_3 = State()
    choosing_sell_editor_menu_marka_edit_4 = State()
    choosing_sell_editor_menu_marka_edit_5 = State()
    choosing_sell_editor_menu_marka_edit_6 = State()
    choosing_sell_editor_menu_marka_edit_7 = State()
    choosing_sell_editor_menu_marka_edit_8 = State()
    choosing_sell_editor_menu_model_edit_1 = State()
    choosing_sell_editor_menu_model_edit_2 = State()
    choosing_sell_editor_menu_model_edit_3 = State()
    choosing_sell_editor_menu_model_edit_4 = State()
    choosing_sell_editor_menu_model_edit_5 = State()
    choosing_sell_editor_menu_model_edit_6 = State()
    choosing_sell_editor_menu_model_edit_7 = State()
    choosing_sell_editor_menu_model_edit_8 = State()
    choosing_sell_editor_year_edit_1 = State()
    choosing_sell_editor_year_edit_2 = State()
    choosing_sell_editor_year_edit_3 = State()
    choosing_sell_editor_year_edit_4 = State()
    choosing_sell_editor_year_edit_5 = State()
    choosing_sell_editor_year_edit_6 = State()
    choosing_sell_editor_year_edit_7 = State()
    choosing_sell_editor_year_edit_8 = State()
    choosing_sell_editor_menu_vin_edit_1 = State()
    choosing_sell_editor_menu_vin_edit_2 = State()
    choosing_sell_editor_menu_vin_edit_3 = State()
    choosing_sell_editor_menu_vin_edit_4 = State()
    choosing_sell_editor_menu_vin_edit_5 = State()
    choosing_sell_editor_menu_vin_edit_6 = State()
    choosing_sell_editor_menu_vin_edit_7 = State()
    choosing_sell_editor_menu_vin_edit_8 = State()
    choosing_sell_editor_menu_comment_edit_1 = State()
    choosing_sell_editor_menu_comment_edit_2 = State()
    choosing_sell_editor_menu_comment_edit_3 = State()
    choosing_sell_editor_menu_comment_edit_4 = State()
    choosing_sell_editor_menu_comment_edit_5 = State()
    choosing_sell_editor_menu_comment_edit_6 = State()
    choosing_sell_editor_menu_comment_edit_7 = State()
    choosing_sell_editor_menu_comment_edit_8 = State()
    choosing_sell_editor_finish_1 = State()
    choosing_sell_editor_finish_2 = State()
    choosing_sell_editor_finish_3 = State()
    choosing_sell_editor_finish_4 = State()
    choosing_sell_editor_finish_5 = State()
    choosing_sell_editor_finish_6 = State()
    choosing_sell_editor_finish_7 = State()
    choosing_sell_editor_finish_8 = State()

    choosing_comissiya_our = State()
    choosing_comissiya_our2 = State()
    choosing_comissiya_credit_cash = State()
    choosing_our_credit_cash = State()
    choosing_comissiya_credit2 = State()
    choosing_comissiya_credit3 = State()
    choosing_comissiya_credit4 = State()
    choosing_comissiya_credit5 = State()
    choosing_comissiya_credit6 = State()
    choosing_comissiya_credit7 = State()
    choosing_comissiya_credit78 = State()
    choosing_comissiya_credit8 = State()
    choosing_comissiya_credit9 = State()
    choosing_comissiya_credit10 = State()
    choosing_comissiya_credit101 = State()
    choosing_comissiya_credit11 = State()
    choosing_comissiya_credit12 = State()
    choosing_comissiya_credit13 = State()
    choosing_comissiya_credit14 = State()
    choosing_comissiya_credit14_0 = State()
    choosing_comissiya_credit15 = State()
    choosing_comissiya_credit16 = State()
    choosing_comissiya_credit167 = State()
    choosing_comissiya_credit17 = State()
    choosing_comissiya_cash2 = State()
    choosing_comissiya_cash3 = State()
    choosing_comissiya_cash4 = State()
    choosing_comissiya_cash5 = State()
    choosing_comissiya_cash6 = State()
    choosing_comissiya_cash7 = State()
    choosing_comissiya_cash8 = State()
    choosing_comissiya_cash78 = State()
    choosing_comissiya_cash9 = State()
    choosing_comissiya_cash10 = State()
    choosing_comissiya_cash101 = State()
    choosing_comissiya_cash11 = State()
    choosing_comissiya_cash12 = State()
    choosing_comissiya_cash13 = State()
    choosing_comissiya_cash14 = State()
    choosing_comissiya_cash15 = State()
    choosing_comissiya_cash16 = State()
    choosing_comissiya_cash167 = State()
    choosing_comissiya_cash17 = State()
    choosing_comissiya_cash18 = State()
    choosing_comissiya_cash19 = State()
    choosing_our_credit = State()
    choosing_our_credit2 = State()
    choosing_our_credit3 = State()
    choosing_our_credit4 = State()
    choosing_our_credit45 = State()
    choosing_our_credit451 = State()
    choosing_our_credit452 = State()
    choosing_our_credit453 = State()
    choosing_our_credit5 = State()
    choosing_our_credit6 = State()
    choosing_our_credit7 = State()
    choosing_our_credit8 = State()
    choosing_our_cash = State()
    choosing_our_cash2 = State()
    choosing_our_cash3 = State()
    choosing_our_cash4 = State()
    choosing_our_cash45 = State()
    choosing_our_cash451 = State()
    choosing_our_cash452 = State()
    choosing_our_cash453 = State()
    choosing_our_cash5 = State()
    choosing_our_cash6 = State()
    choosing_our_cash7 = State()
    choosing_our_cash8 = State()
    choosing_our_cash9 = State()
    choosing_critical_finish = State()


# ============================================
@router.callback_query(F.data == texts.BT_CONSTRUCTOR_1_SELL)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    print(f"PRINTER_LOGGER {callback.message.chat.username} на ветке ПРОДАЛ")
    await state.update_data(chosen_type=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_COMISSION,
        callback_data=texts.BT_COMISSION)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_OUR,
        callback_data=texts.BT_OUR)
    )
    await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_data_car_start)


@router.message(SetReport.choosing_critical_finish)
async def main_menu_choosing_critical_finish(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await message.answer(
        text="Произошла ошибка. Нажмите на /start для составления нового отчета.")
    await message.answer(text="/start")


# =============================
@router.callback_query(SetReport.choosing_sell_data_car_start, F.data == texts.BT_COMISSION)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
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
    await callback.message.answer(text=texts.MESSAGE_PHOTO_VIN_DOWNLOAD, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_data_comission_car)
    await callback.message.delete()


@router.callback_query(SetReport.choosing_sell_data_comission_car,
                       F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON2)
    await state.set_state(SetReport.choosing_sell_comission_vin)


@router.callback_query(SetReport.choosing_sell_data_comission_car,
                       F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON22)
    await state.set_state(SetReport.choosing_sell_comission_pts)


@router.callback_query(SetReport.choosing_sell_data_comission_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(text="Укажите VIN")
    await state.set_state(SetReport.choosing_sell_comission_data_car_marka)


@router.message(SetReport.choosing_sell_comission_data_car_marka)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")

    keyboard_to_delete = types.ReplyKeyboardRemove()
    await state.update_data(chosen_vin_number=message.text.upper())
    vin_number = message.text.upper()
    print(vin_number + " choosing_sell_comission_data_car_marka")
    summas =  await utils.connectors.db_sql_vin_comission_owner_select(vin_number, message)
    if summas != "UNKNOWN":
        await message.answer(text="Укажите марку", reply_markup=keyboard_to_delete)
        await state.set_state(SetReport.choosing_sell_comission_data_car_model)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Изменить данные",
            callback_data="Изменить данные")
        )
        await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)
        await message.answer(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте заново")


@router.message(SetReport.choosing_sell_comission_data_car_model)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_vin_marka=message.text.upper())
    await message.answer(text="Укажите модель")
    await state.set_state(SetReport.choosing_sell_comission_data_car_year)


@router.message(SetReport.choosing_sell_comission_data_car_year)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_vin_model=message.text.upper())
    await message.answer(text="Укажите год")
    await state.set_state(SetReport.choosing_sell_comission_data_car_gosnumber)


@router.message(SetReport.choosing_sell_comission_data_car_gosnumber)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        await message.answer(text="Укажите гоc номер")
        await state.set_state(SetReport.choosing_sell_comission_data_car_next)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(text="Укажите год")
        await state.set_state(SetReport.choosing_sell_comission_data_car_gosnumber)


@router.message(SetReport.choosing_sell_comission_data_car_next)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
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
    Год: {str(data['chosen_vin_year']).upper()}
    Гос номер: {str(data['chosen_vin_gos_number']).upper()}
    VIN: {str(data['chosen_vin_number']).upper()}
    Марка: {data['chosen_vin_marka'].upper()}
    Модель: {data['chosen_vin_model'].upper()}
    '''
    await message.answer(text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_comissiya_our)


@router.message(SetReport.choosing_sell_comission_vin, F.photo)
async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.downloader.constructor_choosing_vin(message, state, bot)
    await state.set_state(SetReport.choosing_comissiya_our)


@router.message(SetReport.choosing_sell_comission_pts, F.photo)
async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.downloader.constructor_choosing_electro(message, state, bot)
    await state.set_state(SetReport.choosing_comissiya_our)


# ==============================

@router.callback_query(SetReport.choosing_comissiya_our,
                       F.data == texts.BT_EDIT)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["Год", "Гос номер", "VIN", "Марка", "Модель", "Все ок"],
                        'data': ["edit_menu_year", "edit_menu_gosnumber", "edit_menu_vin", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_vin(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_vin_editor_first_sell_comission)


@router.callback_query(SetReport.choosing_vin_editor_start_sell_comission)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["Год", "Гос номер", "VIN", "Марка", "Модель", "Все ок"],
                        'data': ["edit_menu_year", "edit_menu_gosnumber", "edit_menu_vin", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_vin(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_vin_editor_first_sell_comission)


# ===================
@router.callback_query(SetReport.choosing_vin_editor_first_sell_comission, F.data == "edit_menu_year")
async def editor_first_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_year(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_year_sell_comission)


@router.message(SetReport.choosing_vin_editor_year_sell_comission)
async def editor_first_vin_year(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_year_editor(message, state)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_comission, F.data == "edit_menu_gosnumber")
async def editor_first_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_gos_number_sell_comission)


@router.message(SetReport.choosing_vin_editor_gos_number_sell_comission)
async def editor_first_vin_gos_number(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_gos_number(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_comission, F.data == "edit_menu_vin")
async def editor_first_menu_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_menu_vin(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_vin_sell_comission)


@router.message(SetReport.choosing_vin_editor_vin_sell_comission)
async def editor_first_vin_number(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_number(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_comission, F.data == "edit_menu_marka")
async def editor_first_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_marka(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_marka_sell_comission)


@router.message(SetReport.choosing_vin_editor_marka_sell_comission)
async def editor_first_vin_marka(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_marka(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_comission, F.data == "edit_menu_model")
async def editor_first_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_model(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_model_sell_comission)


@router.message(SetReport.choosing_vin_editor_model_sell_comission)
async def editor_first_vin_model(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_model(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_comission, F.data == "edit_menu_finish")
async def constructor_choosing_dkp(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_credit_our=texts.BT_COMISSION)
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    print(vin_number + " choosing_sell_comission_vin")
    summas = await utils.connectors.db_sql_vin_comission_owner_select(vin_number, callback)
    if summas != "UNKNOWN":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT,
            callback_data=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT)
        )
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_COMISSION_CASH,
            callback_data=texts.BT_CONSTRUCTOR_3_COMISSION_CASH)
        )
        await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR_CREDIT_CASH, reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_comissiya_credit_cash)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Изменить данные",
            callback_data="Изменить данные")
        )
        await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)
        await callback.message.edit_text(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте сначала",
                                         reply_markup=builder.as_markup())


# ===================


# @router.callback_query(SetReport.choosing_comissiya_our, F.data == texts.BT_EDIT)
# async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.answer(text="Укажите VIN")
#     await state.set_state(SetReport.choosing_comissiya_our44444)


# @router.callback_query(SetReport.choosing_comissiya_our44444, F.data == texts.BT_EDIT)
# async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(chosen_vin_number=callback.message.text.upper())
#     vin_number = callback.message.text.upper()
#     print(vin_number + " choosing_comissiya_our")
#     summas = utils.connectors.db_sql_vin_comission_owner_select(vin_number)
#     if summas != "UNKNOWN":
#         await callback.message.answer(text="Укажите марку")
#         await state.set_state(SetReport.choosing_sell_comission_data_car_marka)
#     else:
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text="Вернуться",
#             callback_data=texts.BT_EDIT)
#         )
#         await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)
#
#         await callback.message.answer(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте заного",
#                                       reply_markup=builder.as_markup())


@router.callback_query(SetReport.choosing_comissiya_our, F.data == texts.BT_NEXT)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_credit_our=texts.BT_COMISSION)
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    print(vin_number + " choosing_sell_comission_vin")
    summas = await utils.connectors.db_sql_vin_comission_owner_select(vin_number, callback)
    if summas != "UNKNOWN":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT,
            callback_data=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT)
        )
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_COMISSION_CASH,
            callback_data=texts.BT_CONSTRUCTOR_3_COMISSION_CASH)
        )
        await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR_CREDIT_CASH, reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_comissiya_credit_cash)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Изменить данные",
            callback_data="Изменить данные")
        )
        await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)
        await callback.message.edit_text(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте сначала",
                                         reply_markup=builder.as_markup())

    #


# ==============================================

# =============================
@router.callback_query(SetReport.choosing_sell_data_car_start, F.data == texts.BT_OUR)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
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
    await callback.message.answer(text=texts.MESSAGE_PHOTO_VIN_DOWNLOAD, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_data_our_car)
    await callback.message.delete()


@router.callback_query(SetReport.choosing_sell_data_our_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON2)
    await state.set_state(SetReport.choosing_sell_our_vin)


@router.callback_query(SetReport.choosing_sell_data_our_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON22)
    await state.set_state(SetReport.choosing_sell_our_pts)


@router.callback_query(SetReport.choosing_sell_data_our_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(text="Укажите VIN")
    await state.set_state(SetReport.choosing_sell_our_data_car_marka)


@router.message(SetReport.choosing_sell_our_data_car_marka)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    keyboard_to_delete = types.ReplyKeyboardRemove()
    await state.update_data(chosen_vin_number=message.text.upper())
    vin_number = message.text.upper()
    print(vin_number + " choosing_sell_our_data_car_marka")
    summas = await utils.connectors.db_sql_vin_buy_owner_select(vin_number, message)
    if summas != "UNKNOWN":
        await message.answer(text="Укажите марку", reply_markup=keyboard_to_delete)
        await state.set_state(SetReport.choosing_sell_our_data_car_model)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Изменить данные",
            callback_data="Изменить данные")
        )
        await state.set_state(SetReport.choosing_vin_editor_start_sell_comission)
        await message.answer(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте заново")


@router.message(SetReport.choosing_sell_our_data_car_model)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_vin_marka=message.text.upper())
    await message.answer(text="Укажите модель")
    await state.set_state(SetReport.choosing_sell_our_data_car_year)


@router.message(SetReport.choosing_sell_our_data_car_year)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_vin_model=message.text.upper())
    await message.answer(text="Укажите год")
    await state.set_state(SetReport.choosing_sell_our_data_car_gosnumber)


@router.message(SetReport.choosing_sell_our_data_car_gosnumber)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        await message.answer(text="Укажите гоc номер")
        await state.set_state(SetReport.choosing_sell_our_data_car_next)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(text="Укажите год")
        await state.set_state(SetReport.choosing_sell_our_data_car_gosnumber)


@router.message(SetReport.choosing_sell_our_data_car_next)
async def main_menu_button2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
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
    Год: {str(data['chosen_vin_year']).upper()}
    Гос номер: {str(data['chosen_vin_gos_number']).upper()}
    VIN: {str(data['chosen_vin_number']).upper()}
    Марка: {data['chosen_vin_marka'].upper()}
    Модель: {data['chosen_vin_model'].upper()}
    '''
    await message.answer(text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_our_our)


@router.message(SetReport.choosing_sell_our_vin, F.photo)
async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.downloader.constructor_choosing_vin(message, state, bot)
    await state.set_state(SetReport.choosing_our_our)


@router.message(SetReport.choosing_sell_our_pts, F.photo)
async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.downloader.constructor_choosing_electro(message, state, bot)
    await state.set_state(SetReport.choosing_our_our)


# ==============================

@router.callback_query(SetReport.choosing_our_our,
                       F.data == texts.BT_EDIT)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["Год", "Гос номер", "VIN", "Марка", "Модель", "Все ок"],
                        'data': ["edit_menu_year", "edit_menu_gosnumber", "edit_menu_vin", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_vin(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_vin_editor_first_sell_our)


@router.callback_query(SetReport.choosing_vin_editor_start_sell_our)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["Год", "Гос номер", "VIN", "Марка", "Модель", "Все ок"],
                        'data': ["edit_menu_year", "edit_menu_gosnumber", "edit_menu_vin", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_vin(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_vin_editor_first_sell_our)


# ===================
@router.callback_query(SetReport.choosing_vin_editor_first_sell_our, F.data == "edit_menu_year")
async def editor_first_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_year(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_year_sell_our)


@router.message(SetReport.choosing_vin_editor_year_sell_our)
async def editor_first_vin_year(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_year_editor(message, state)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_our, F.data == "edit_menu_gosnumber")
async def editor_first_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_gos_number_sell_our)


@router.message(SetReport.choosing_vin_editor_gos_number_sell_our)
async def editor_first_vin_gos_number(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_gos_number(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_our)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_our, F.data == "edit_menu_vin")
async def editor_first_menu_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_menu_vin(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_vin_sell_our)


@router.message(SetReport.choosing_vin_editor_vin_sell_our)
async def editor_first_vin_number(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_number(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_our)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_our, F.data == "edit_menu_marka")
async def editor_first_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_marka(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_marka_sell_our)


@router.message(SetReport.choosing_vin_editor_marka_sell_our)
async def editor_first_vin_marka(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_marka(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_our)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_our, F.data == "edit_menu_model")
async def editor_first_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_model(callback, state)
    await state.set_state(SetReport.choosing_vin_editor_model_sell_our)


@router.message(SetReport.choosing_vin_editor_model_sell_our)
async def editor_first_vin_model(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_first_vin_model(message, state)
    await state.set_state(SetReport.choosing_vin_editor_start_sell_our)


@router.callback_query(SetReport.choosing_vin_editor_first_sell_our, F.data == "edit_menu_finish")
async def constructor_choosing_dkp(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_credit_our=texts.BT_OUR)
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    print(vin_number + " choosing_sell_owner_vin")
    summas = await utils.connectors.db_sql_vin_buy_owner_select(vin_number, callback)
    if summas != "UNKNOWN":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_OUR_CREDIT,
            callback_data=texts.BT_CONSTRUCTOR_3_OUR_CREDIT)
        )
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_OUR_CASH,
            callback_data=texts.BT_CONSTRUCTOR_3_OUR_CASH)
        )
        await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR_CREDIT_CASH, reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_our_credit_cash)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Изменить данные",
            callback_data="Изменить данные")
        )
        await state.set_state(SetReport.choosing_vin_editor_start_sell_our)
        await callback.message.edit_text(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте сначала",
                                         reply_markup=builder.as_markup())


# ===================

# @router.callback_query(SetReport.choosing_our_our, F.data == texts.BT_EDIT)
# async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.answer(text="Укажите VIN")
#     await state.set_state(SetReport.choosing_our_our44444)


# @router.message(SetReport.choosing_our_our44444, F.data == texts.BT_EDIT)
# async def main_menu_button2(message: Message, state: FSMContext):
#     await state.update_data(chosen_vin_number=message.text.upper())
#     vin_number = message.text.upper()
#     print(vin_number + " choosing_our_our")
#     summas = utils.connectors.db_sql_vin_buy_owner_select(vin_number)
#     if summas != "UNKNOWN":
#         await message.answer(text="Укажите марку")
#         await state.set_state(SetReport.choosing_sell_our_data_car_marka)
#     else:
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text="Вернуться",
#             callback_data=texts.BT_CONSTRUCTOR_1_SELL)
#         )
#
#         await message.answer(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте заного",
#                              reply_markup=builder.as_markup())


@router.callback_query(SetReport.choosing_our_our, F.data == texts.BT_NEXT)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_credit_our=texts.BT_OUR)
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    print(vin_number + " choosing_sell_owner_vin")
    summas = await utils.connectors.db_sql_vin_buy_owner_select(vin_number, callback)
    if summas != "UNKNOWN":
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_OUR_CREDIT,
            callback_data=texts.BT_CONSTRUCTOR_3_OUR_CREDIT)
        )
        builder.add(types.InlineKeyboardButton(
            text=texts.BT_CONSTRUCTOR_3_OUR_CASH,
            callback_data=texts.BT_CONSTRUCTOR_3_OUR_CASH)
        )
        await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR_CREDIT_CASH, reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_our_credit_cash)
    else:
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Изменить данные",
            callback_data="Изменить данные")
        )
        await state.set_state(SetReport.choosing_vin_editor_start_sell_our)
        await callback.message.edit_text(text="Автомобиль с этим  VIN отсутствует в базе, попробуйте сначала",
                                         reply_markup=builder.as_markup())


# ==============================================

# @router.callback_query(SetReport.choosing_comissiya_our22)
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(type_credit_our=texts.BT_OUR)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT,
#         callback_data=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT)
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_3_COMISSION_CASH,
#         callback_data=texts.BT_CONSTRUCTOR_3_COMISSION_CASH)
#     )
#     await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR_CREDIT_CASH, reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_comissiya_credit_cash)
#


# @router.callback_query(SetReport.choosing_comissiya_our33)
# async def main_menu_bt_constructor_12_sell(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(type_credit_our=texts.BT_COMISSION)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_3_OUR_CREDIT,
#         callback_data=texts.BT_CONSTRUCTOR_3_OUR_CREDIT)
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_3_OUR_CASH,
#         callback_data=texts.BT_CONSTRUCTOR_3_OUR_CASH)
#     )
#     await callback.message.edit_text(text=texts.MESSAGE_COMISSION_OUR_CREDIT_CASH, reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_our_credit_cash)
#


@router.callback_query(SetReport.choosing_comissiya_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT)
async def sell_choosing_comissiya_credit_comission(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_comissiya_credit2)


@router.message(SetReport.choosing_comissiya_credit2)
async def sell_choosing_comissiya_credit_comission2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=just)
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_comissiya_credit3)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_COST_DROM,
        )
        await state.set_state(SetReport.choosing_comissiya_credit2)


@router.message(SetReport.choosing_comissiya_credit3)
async def sell_choosing_comissiya_credit_comission3(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(dealer_discount=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ВСЕ ОК",
            callback_data="callback_ostav")
        )
        builder.add(types.InlineKeyboardButton(
            text="РЕДАКТИРОВАТЬ",
            callback_data="callback_edit")
        )
        data = await state.get_data()
        vin_number = data['chosen_vin_number']
        print(vin_number + " XXXX")
        await message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
        summas = await utils.connectors.db_sql_price_owner_select(vin_number, message)
        await message.answer(
            text="СУММА СОБСТВЕННИКУ " + str(summas), reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_comissiya_credit6)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_comissiya_credit3)


# @router.message(SetReport.choosing_comissiya_credit4)
# async def sell_choosing_comissiya_creditcomission4(message: Message, state: FSMContext):
#     just = message.text.upper()
#     await state.update_data(summa_nm=re.sub("[^0-9]", "", just))
#     await message.answer(
#         text=texts.MESSAGE_SUM_SOBS,
#     )
#     await state.set_state(SetReport.choosing_comissiya_credit5)


@router.message(SetReport.choosing_comissiya_credit4)
async def sell_choosing_comissiya_creditcomission5(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    await state.update_data(summa_nm=int(re.sub("[^0-9]", "", just)))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ВСЕ ОК",
        callback_data="callback_ostav")
    )
    builder.add(types.InlineKeyboardButton(
        text="РЕДАКТИРОВАТЬ",
        callback_data="callback_edit")
    )
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    print(vin_number + " XXXX")
    await message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
    summas = await utils.connectors.db_sql_price_owner_select(vin_number, message)
    await message.answer(
        text="СУММА СОБСТВЕННИКУ " + str(summas), reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit6)


@router.callback_query(SetReport.choosing_comissiya_credit6, F.data == "callback_edit")
async def sell_choosing_comissiya_creditcomission6(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(
        text="На какую сумму хотите изменить?",
    )
    await state.set_state(SetReport.choosing_comissiya_credit78)


@router.message(SetReport.choosing_comissiya_credit78)
async def sell_choosing_comissiya_creditcomission78(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(summa_sob=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="САМ",
            callback_data="САМ")
        )
        builder.add(types.InlineKeyboardButton(
            text="Нажмите, чтобы ввести фамилию",
            switch_inline_query_current_chat='find_b1 ')
        )
        await message.answer(
            text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_comissiya_credit9)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text="На какую сумму хотите изменить?",
        )
        await state.set_state(SetReport.choosing_comissiya_credit78)


@router.callback_query(SetReport.choosing_comissiya_credit6, F.data == "callback_ostav")
async def sell_choosing_comissiya_creditcomission6(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    just = utils.connectors.db_sql_price_owner_select(vin_number, callback)
    await state.update_data(summa_sob=int(re.sub("[^0-9]", "", str(just))))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b1 ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit9)


# @router.message(SetReport.choosing_comissiya_credit8)
# async def sell_choosing_comissiya_creditcomission8(message: Message, state: FSMContext):
#     current_state = await state.get_state()
#     print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
#     just = message.text.upper()
#     if just.isdigit():
#         await state.update_data(howmuchtorg=int(just))
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text="САМ",
#             callback_data="САМ")
#         )
#         builder.add(types.InlineKeyboardButton(
#             text="Нажмите, чтобы ввести фамилию",
#             switch_inline_query_current_chat='find_b1 ')
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
#         )
#         await state.set_state(SetReport.choosing_comissiya_credit9)
#     else:
#         await message.answer(
#             text=texts.MESSAGE_ONLY_DIGITS,
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_TORG,
#         )
#         await state.set_state(SetReport.choosing_comissiya_credit8)


@router.callback_query(SetReport.choosing_comissiya_credit9, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission9(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosell="-")
    builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="САМ",
    #     callback_data="САМ")
    # )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b2 ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit101)


@router.callback_query(SetReport.choosing_comissiya_credit101, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await callback.message.answer(
        text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit13)


@router.message(SetReport.choosing_comissiya_credit9)
@router.inline_query(lambda query: query.query.startswith("find_b1 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b1 ")
    await state.set_state(SetReport.choosing_comissiya_credit10)


@router.message(SetReport.choosing_comissiya_credit10)
async def sell_choosing_our_credit5(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosell=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="САМ",
    #     callback_data="САМ")
    # )
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_b2 ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit11)


@router.callback_query(SetReport.choosing_comissiya_credit11, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await callback.message.answer(
        text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit13)


@router.message(SetReport.choosing_comissiya_credit11)
@router.inline_query(lambda query: query.query.startswith("find_b2 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b2 ")
    await state.set_state(SetReport.choosing_comissiya_credit12)


@router.message(SetReport.choosing_comissiya_credit12)
async def sell_choosing_our_credit12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosellcredit=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await message.answer(
        text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit13)


# ==================================================================================================
@router.callback_query(SetReport.choosing_comissiya_credit13, F.data == texts.BT_NO)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('1, 3')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_1)


@router.message(SetReport.choosing_sell_editor_1)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА СОБСТВЕННИКУ: {data['summa_sob']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ: {data['whosellcredit']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_editor_start_1, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(date_raschet=None)
    await state.update_data(howmuchtorg=None)
    await state.update_data(type_raschet=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_1)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто оформил кредит", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_1_6_credit(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_1)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_1)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    data = await state.get_data()
    print("kzkzkz1" + data['whosellcredit'])
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_1)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_1)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_1)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_1)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_1)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_1)


@router.message(SetReport.choosing_sell_editor_year_edit_1)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_1)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_1)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_1)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_1)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_1)


@router.callback_query(SetReport.choosing_sell_selector_1, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================
# @router.callback_query(SetReport.choosing_comissiya_credit13, F.data == texts.BT_NO)
# async def sell_choosing_comissiya_creditcomission13(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#             '''
#     await callback.message.answer(text=text)
#     await callback.message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await callback.message.answer(text="/start")
#     await state.clear()


@router.callback_query(SetReport.choosing_comissiya_credit13, F.data == texts.BT_YES)
async def sell_choosing_comissiya_creditcomission13(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Отложить",
        callback_data="Отложить")
    )
    await callback.message.answer(
        text=texts.MESSAGE_DATE_RASCHET, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit14)


@router.callback_query(SetReport.choosing_comissiya_credit14, F.data == "Отложить")
async def sell_choosing_comissiya_comissiya_credit14(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(date_raschet=None)
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    await callback.message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
    type_of_calc = utils.connectors.db_sql_type_of_calc_select(vin_number, callback)
    await state.update_data(type_raschet=str(type_of_calc))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ВСЕ ОК",
        callback_data="callback_ostav")
    )
    builder.add(types.InlineKeyboardButton(
        text="РЕДАКТИРОВАТЬ",
        callback_data="callback_edit")
    )
    data = await state.get_data()
    await callback.message.answer(
        text="ВИД РАСЧЕТА " + "\"" + data['type_raschet'] + "\"", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit16)


@router.message(SetReport.choosing_comissiya_credit14)
async def sell_choosing_comissiya_creditcomission14(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    date_raschet = message.text.lower()
    new_date = await utils.connectors.date_normalizer(date_raschet)
    if new_date:
        await state.update_data(date_raschet=new_date)
        data = await state.get_data()
        vin_number = data['chosen_vin_number']
        await message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
        type_of_calc = utils.connectors.db_sql_type_of_calc_select(vin_number, message)
        await state.update_data(type_raschet=str(type_of_calc))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ВСЕ ОК",
            callback_data="callback_ostav")
        )
        builder.add(types.InlineKeyboardButton(
            text="РЕДАКТИРОВАТЬ",
            callback_data="callback_edit")
        )
        data = await state.get_data()
        await message.answer(
            text="ВИД РАСЧЕТА " + "\"" + data['type_raschet'] + "\"", reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_comissiya_credit16)
    else:
        await message.answer(
            text="ДАТА НЕКОРРЕКТНА, ПОПРОБУЙТЕ ЕЩЕ РАЗ")
        await message.answer(
            text=texts.MESSAGE_DATE_RASCHET,
        )
        await state.set_state(SetReport.choosing_comissiya_credit14)


@router.callback_query(SetReport.choosing_comissiya_credit16, F.data == "callback_edit")
async def sell_choosing_comissiya_creditcomission6(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="НАЛ",
        callback_data="НАЛ")
    )
    builder.add(types.InlineKeyboardButton(
        text="БЕЗНАЛ",
        callback_data="БЕЗНАЛ")
    )
    await callback.message.answer(
        text="На какой вид расчета хотите изменить?", reply_markup=builder.as_markup(),
    )
    await state.set_state(SetReport.choosing_comissiya_credit167)


@router.callback_query(SetReport.choosing_comissiya_credit167)
async def sell_choosing_comissiya_creditcomission167(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_raschet=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_SAVE,
        callback_data=texts.BT_SAVE)
    )
    data = await state.get_data()
    await callback.message.answer(
        text="ВИД РАСЧЕТА " + data['type_raschet'], reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit17)


# ==================================================================================================
@router.callback_query(SetReport.choosing_comissiya_credit17)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('2, 2')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_2)


@router.message(SetReport.choosing_sell_editor_2)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА СОБСТВЕННИКУ: {data['summa_sob']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ: {data['whosellcredit']}\nДАТА РАСЧЕТА: {data['date_raschet']}\nВИД РАСЧЕТА: {data['type_raschet']}\n\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_editor_start_2, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_2)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто оформил кредит", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_1_6(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s1 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s1 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s1 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s2 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s2 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s2 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_2)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    data = await state.get_data()
    print("kzkzkz2" + data['whosellcredit'])
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_2)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_2)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_2)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_2)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_2)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_2)


@router.message(SetReport.choosing_sell_editor_year_edit_2)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_2)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_2)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_2)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_2)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_2)


@router.callback_query(SetReport.choosing_sell_selector_2, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================

# @router.callback_query(SetReport.choosing_comissiya_credit17)
# async def sell_choosing_comissiya_creditcomission17(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#             '''
#     await callback.message.answer(text=text)
#     await callback.message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await callback.message.answer(text="/start")
#     await state.clear()

# ==================================================================================================
@router.callback_query(SetReport.choosing_comissiya_credit16, F.data == "callback_ostav")
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('3, 1')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_3)


@router.message(SetReport.choosing_sell_editor_3)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА СОБСТВЕННИКУ: {data['summa_sob']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ: {data['whosellcredit']}\nДАТА РАСЧЕТА: {data['date_raschet']}\nВИД РАСЧЕТА: {data['type_raschet']}\n\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_editor_start_3, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_3)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто оформил кредит", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_1_6(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_3)


# ===========================
@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s3 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s3 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s3 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_3)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s4 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s4 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s4 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_3)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    data = await state.get_data()
    print("kzkzkz444444" + data['whosellcredit'])
    await state.set_state(SetReport.choosing_sell_editor_start_3)


# ===========================
#
# @router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_who_sell")
# async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_sell(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_3)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_3)
# async def editor_who_sell_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_sell_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_3)
#
#
# @router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_who_credit")
# async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_credit(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_3)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_3)
# async def editor_who_credit_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_credit_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_3)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_3)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_3)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_3)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_3)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_3)


@router.message(SetReport.choosing_sell_editor_year_edit_3)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_3)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_3)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_3)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_3)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_3)


@router.callback_query(SetReport.choosing_sell_selector_3, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================

# @router.callback_query(SetReport.choosing_comissiya_credit16, F.data == "callback_ostav")
# async def sell_choosing_comissiya_creditcomission16(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#             '''
#     await callback.message.answer(text=text)
#     await callback.message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await callback.message.answer(text="/start")
#     await state.clear()


@router.callback_query(SetReport.choosing_comissiya_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_COMISSION_CASH)
async def sell_choosing_comissiya_cash_comission(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_comissiya_cash2)


@router.message(SetReport.choosing_comissiya_cash2)
async def sell_choosing_comissiya_cash_comission2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=just)
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_comissiya_cash3)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_COST_DROM,
        )
        await state.set_state(SetReport.choosing_comissiya_cash2)


@router.message(SetReport.choosing_comissiya_cash3)
async def sell_choosing_comissiya_cash_comission3(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(dealer_discount=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ВСЕ ОК",
            callback_data="callback_ostav")
        )
        builder.add(types.InlineKeyboardButton(
            text="РЕДАКТИРОВАТЬ",
            callback_data="callback_edit")
        )

        data = await state.get_data()
        vin_number = data['chosen_vin_number']
        await message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
        summas = await utils.connectors.db_sql_price_owner_select(vin_number, message)
        await message.answer(
            text="СУММА СОБСТВЕННИКУ " + str(summas), reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_comissiya_cash6)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_comissiya_cash3)


# @router.message(SetReport.choosing_comissiya_cash4)
# async def sell_choosing_comissiya_cash_comission4(message: Message, state: FSMContext):
#     just = message.text.upper()
#     await state.update_data(summa_nm=re.sub("[^0-9]", "", just))
#     await message.answer(
#         text=texts.MESSAGE_SUM_SOBS,
#     )
#     await state.set_state(SetReport.choosing_comissiya_cash5)


@router.message(SetReport.choosing_comissiya_cash4)
async def sell_choosing_comissiya_cash_comission5(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    await state.update_data(summa_nm=int(re.sub("[^0-9]", "", just)))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ВСЕ ОК",
        callback_data="callback_ostav")
    )
    builder.add(types.InlineKeyboardButton(
        text="РЕДАКТИРОВАТЬ",
        callback_data="callback_edit")
    )

    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    await message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
    summas = await utils.connectors.db_sql_price_owner_select(vin_number, message)
    await message.answer(
        text="СУММА СОБСТВЕННИКУ " + str(summas), reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash6)


@router.callback_query(SetReport.choosing_comissiya_cash6, F.data == "callback_edit")
async def sell_choosing_comissiya_cash_comission6(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer(
        text="На какую сумму хотите изменить?",
    )
    await state.set_state(SetReport.choosing_comissiya_cash78)


@router.message(SetReport.choosing_comissiya_cash78)
async def sell_choosing_comissiya_cash_comission78(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    # just = "0"
    if just.isdigit():
        await state.update_data(summa_sob=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="САМ",
            callback_data="САМ")
        )
        builder.add(types.InlineKeyboardButton(
            text="Нажмите, чтобы ввести фамилию",
            switch_inline_query_current_chat='find_b3 ')
        )
        await message.answer(
            text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_comissiya_cash9)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text="На какую сумму хотите изменить?",
        )
        await state.set_state(SetReport.choosing_comissiya_cash78)


@router.callback_query(SetReport.choosing_comissiya_cash6, F.data == "callback_ostav")
async def sell_choosing_comissiya_cash_comission6(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    just = utils.connectors.db_sql_price_owner_select(vin_number, callback)
    await state.update_data(summa_sob=int(re.sub("[^0-9]", "", str(just))))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b3 ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash9)


# @router.message(SetReport.choosing_comissiya_cash8)
# async def sell_choosing_comissiya_cash_comission8(message: Message, state: FSMContext):
#     current_state = await state.get_state()
#     print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
#     just = message.text.upper()
#     if just.isdigit():
#         await state.update_data(howmuchtorg=int(just))
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text="САМ",
#             callback_data="САМ")
#         )
#         builder.add(types.InlineKeyboardButton(
#             text="Нажмите, чтобы ввести фамилию",
#             switch_inline_query_current_chat='find_b3 ')
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
#         )
#         await state.set_state(SetReport.choosing_comissiya_cash9)
#     else:
#         await message.answer(
#             text=texts.MESSAGE_ONLY_DIGITS,
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_TORG,
#         )
#         await state.set_state(SetReport.choosing_comissiya_cash8)


@router.callback_query(SetReport.choosing_comissiya_cash9, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission9(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosell="-")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b4 ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH_DKP + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash101)


@router.callback_query(SetReport.choosing_comissiya_cash101, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await callback.message.answer(
        text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash13)


@router.message(SetReport.choosing_comissiya_cash9)
@router.inline_query(lambda query: query.query.startswith("find_b3 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b3 ")
    await state.set_state(SetReport.choosing_comissiya_cash10)


@router.message(SetReport.choosing_comissiya_cash10)
async def sell_choosing_comissiya_cash_comission10(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosell=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b4 ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_DKP + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash11)


@router.callback_query(SetReport.choosing_comissiya_cash11, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await callback.message.answer(
        text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash13)


@router.message(SetReport.choosing_comissiya_cash11)
@router.inline_query(lambda query: query.query.startswith("find_b4 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b4 ")
    await state.set_state(SetReport.choosing_comissiya_cash12)


@router.message(SetReport.choosing_comissiya_cash12)
async def sell_choosing_comissiya_cash_comission12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosellcredit=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await message.answer(
        text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash13)


# ==================================================================================================
@router.callback_query(SetReport.choosing_comissiya_cash13, F.data == texts.BT_NO)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('4, 6')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_4)


@router.message(SetReport.choosing_sell_editor_4)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА СОБСТВЕННИКУ: {data['summa_sob']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ПИСАЛ ДКП: {data['whosellcredit']}\n\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_editor_start_4, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    await state.update_data(date_raschet=None)
    await state.update_data(type_raschet=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_4)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто писал дкп", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_1_6_dkp(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_4)


# ===========================
@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s5 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s5 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s5 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_4)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s6 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s6 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s6 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_4)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    data = await state.get_data()
    print("kzkzkz9" + data['whosellcredit'])
    await state.set_state(SetReport.choosing_sell_editor_start_4)


# ===========================
# @router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_who_sell")
# async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_sell(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_4)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_4)
# async def editor_who_sell_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_sell_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_4)
#
#
# @router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_who_credit")
# async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_credit(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_4)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_4)
# async def editor_who_credit_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_credit_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_4)
#

@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_4)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_4)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_4)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_4)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_4)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_4)


@router.message(SetReport.choosing_sell_editor_year_edit_4)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_4)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_4)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_4)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_4)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_4)


@router.callback_query(SetReport.choosing_sell_selector_4, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================
# @router.callback_query(SetReport.choosing_comissiya_cash13, F.data == texts.BT_NO)
# async def sell_choosing_comissiya_cash_comission13(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#             '''
#     await callback.message.answer(text=text)
#     await callback.message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await callback.message.answer(text="/start")
#     await state.clear()


@router.callback_query(SetReport.choosing_comissiya_cash13)
async def sell_choosing_comissiya_cash_comission13(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Отложить",
        callback_data="Отложить")
    )
    await callback.message.answer(
        text=texts.MESSAGE_DATE_RASCHET, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash14)


@router.callback_query(SetReport.choosing_comissiya_cash14, F.data == "Отложить")
async def sell_choosing_comissiya_comissiya_cash14(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(date_raschet=None)
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    await callback.message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
    type_of_calc = utils.connectors.db_sql_type_of_calc_select(vin_number, callback)
    await state.update_data(type_raschet=str(type_of_calc))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ВСЕ ОК",
        callback_data="callback_ostav")
    )
    builder.add(types.InlineKeyboardButton(
        text="РЕДАКТИРОВАТЬ",
        callback_data="callback_edit")
    )
    data = await state.get_data()
    await callback.message.answer(
        text="ВИД РАСЧЕТА " + "\"" + data['type_raschet'] + "\"", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash16)


@router.message(SetReport.choosing_comissiya_cash14)
async def sell_choosing_comissiya_creditcomission14(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    date_raschet = message.text.lower()
    new_date = await utils.connectors.date_normalizer(date_raschet)
    if new_date:
        await state.update_data(date_raschet=new_date)
        data = await state.get_data()
        vin_number = data['chosen_vin_number']
        await message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
        type_of_calc = utils.connectors.db_sql_type_of_calc_select(vin_number, message)
        await state.update_data(type_raschet=str(type_of_calc))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ВСЕ ОК",
            callback_data="callback_ostav")
        )
        builder.add(types.InlineKeyboardButton(
            text="РЕДАКТИРОВАТЬ",
            callback_data="callback_edit")
        )
        data = await state.get_data()
        await message.answer(
            text="ВИД РАСЧЕТА " + "\"" + data['type_raschet'] + "\"", reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_comissiya_cash16)
    else:
        await message.answer(
            text="ДАТА НЕКОРРЕКТНА, ПОПРОБУЙТЕ ЕЩЕ РАЗ")
        await message.answer(
            text=texts.MESSAGE_DATE_RASCHET,
        )
        await state.set_state(SetReport.choosing_comissiya_cash14)


@router.callback_query(SetReport.choosing_comissiya_cash15)
async def sell_choosing_comissiya_cash_comission15(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    vin_number = data['chosen_vin_number']
    await callback.message.answer(text="Пожалуйста подождите, идет проверка в базе данных")
    type_of_calc = utils.connectors.db_sql_type_of_calc_select(vin_number, callback)
    await state.update_data(type_raschet=str(type_of_calc))
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОСТАВЛЯЕМ",
        callback_data="callback_ostav")
    )
    builder.add(types.InlineKeyboardButton(
        text="РЕДАКТИРОВАТЬ",
        callback_data="callback_edit")
    )
    data = await state.get_data()
    await callback.message.answer(
        text="ВИД РАСЧЕТА " + data['type_raschet'], reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash16)


@router.callback_query(SetReport.choosing_comissiya_cash16, F.data == "callback_edit")
async def sell_choosing_comissiya_cash_comission16(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="НАЛ",
        callback_data="НАЛ")
    )
    builder.add(types.InlineKeyboardButton(
        text="БЕЗНАЛ",
        callback_data="БЕЗНАЛ")
    )
    await callback.message.answer(
        text="На какую вид расчета хотите изменить?", reply_markup=builder.as_markup(),
    )
    await state.set_state(SetReport.choosing_comissiya_cash167)


@router.callback_query(SetReport.choosing_comissiya_cash167)
async def sell_choosing_comissiya_cash_comission167(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_raschet=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_SAVE,
        callback_data=texts.BT_SAVE)
    )
    data = await state.get_data()
    await callback.message.answer(
        text="ВИД РАСЧЕТА " + data['type_raschet'], reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash17)


# ==================================================================================================
@router.callback_query(SetReport.choosing_comissiya_cash17)
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('5, 5')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_5)


@router.message(SetReport.choosing_sell_editor_5)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА СОБСТВЕННИКУ: {data['summa_sob']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ: {data['whosellcredit']}\nДАТА РАСЧЕТА: {data['date_raschet']}\nВИД РАСЧЕТА: {data['type_raschet']}\n\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_editor_start_5, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_5)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто оформил кредит", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_1_6(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_5)


# ===========================
@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s7 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s7 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s7 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_5)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s8 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s8 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s8 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_5)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    data = await state.get_data()
    print("kzkzkz12" + data['whosellcredit'])
    await state.set_state(SetReport.choosing_sell_editor_start_5)


# ===========================
# @router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_who_sell")
# async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_sell(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_5)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_5)
# async def editor_who_sell_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_sell_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_5)
#
#
# @router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_who_credit")
# async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_credit(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_5)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_5)
# async def editor_who_credit_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_credit_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_5)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_5)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_5)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_5)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_5)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_5)


@router.message(SetReport.choosing_sell_editor_year_edit_5)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_5)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_5)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_5)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_5)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_5)


@router.callback_query(SetReport.choosing_sell_selector_5, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================
# @router.callback_query(SetReport.choosing_comissiya_cash17)
# async def sell_choosing_comissiya_cash_comission17(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#             '''
#     await callback.message.answer(text=text)
#     await callback.message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await callback.message.answer(text="/start")
#     await state.clear()


# ==================================================================================================
@router.callback_query(SetReport.choosing_comissiya_cash16, F.data == "callback_ostav")
async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('6, 4')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_6)


@router.message(SetReport.choosing_sell_editor_6)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА СОБСТВЕННИКУ: {data['summa_sob']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ: {data['whosellcredit']}\nДАТА РАСЧЕТА: {data['date_raschet']}\nВИД РАСЧЕТА: {data['type_raschet']}\n\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_editor_start_6, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_6)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто оформил кредит", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_1_6(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_6)


# ===========================
@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s9 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s9 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s9 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_6)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s10 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s10 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s10 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_6)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


# ===========================

# @router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_who_sell")
# async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_sell(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_6)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_6)
# async def editor_who_sell_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_sell_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_6)
#
#
# @router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_who_credit")
# async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_credit(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_6)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_6)
# async def editor_who_credit_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_credit_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_6)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_6)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_6)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_6)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_6)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_6)


@router.message(SetReport.choosing_sell_editor_year_edit_6)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_6)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_6)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_6)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_6)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_6)


@router.callback_query(SetReport.choosing_sell_selector_6, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================
# @router.callback_query(SetReport.choosing_comissiya_cash16, F.data == "callback_ostav")
# async def sell_choosing_comissiya_cash_comission16(callback: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
#             '''
#     await callback.message.answer(text=text)
#     await callback.message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await callback.message.answer(text="/start")
#     await state.clear()


@router.callback_query(SetReport.choosing_our_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_OUR_CREDIT)
async def sell_choosing_our_credit0(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_our_credit)


@router.message(SetReport.choosing_our_credit)
async def sell_choosing_our_credit1(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_our_credit2)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_COST_DROM,
        )
        await state.set_state(SetReport.choosing_our_credit)


@router.message(SetReport.choosing_our_credit2)
async def sell_choosing_our_credit2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(dealer_discount=int(just))
        builder = InlineKeyboardBuilder()
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="САМ",
            callback_data="САМ")
        )
        builder.add(types.InlineKeyboardButton(
            text="Нажмите, чтобы ввести фамилию",
            switch_inline_query_current_chat='find_b5 ')
        )
        await message.answer(
            text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_our_credit45)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_our_credit2)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# @router.message(SetReport.choosing_our_credit3)
# async def sell_choosing_comissiya_cash_comission8(message: Message, state: FSMContext):
#     current_state = await state.get_state()
#     print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
#     just = message.text.upper()
#     if just.isdigit():
#         await state.update_data(howmuchtorg=int(just))
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text="САМ",
#             callback_data="САМ")
#         )
#         builder.add(types.InlineKeyboardButton(
#             text="Нажмите, чтобы ввести фамилию",
#             switch_inline_query_current_chat='find_b5 ')
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
#         )
#         await state.set_state(SetReport.choosing_our_credit45)
#     else:
#         await message.answer(
#             text=texts.MESSAGE_ONLY_DIGITS,
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_TORG,
#         )
#         await state.set_state(SetReport.choosing_our_credit3)


@router.callback_query(SetReport.choosing_our_credit45, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission9(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosell="-")
    builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="САМ",
    #     callback_data="САМ")
    # )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b6 ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_credit6)


@router.callback_query(SetReport.choosing_our_credit6, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_7)


# @router.callback_query(SetReport.choosing_our_cash5, F.data == "САМ")
# async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(whosellcredit=callback.message.chat.first_name + callback.message.chat.last_name)
#     kb = [
#         [types.KeyboardButton(text="Без комментариев")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         one_time_keyboard=True,
#
#     )
#     await callback.message.answer(text="Комментарии", reply_markup=keyboard)
#     await state.set_state(SetReport.choosing_sell_editor_8)


@router.message(SetReport.choosing_our_credit45)
@router.inline_query(lambda query: query.query.startswith("find_b5 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b5 ")
    await state.set_state(SetReport.choosing_our_credit451)


@router.message(SetReport.choosing_our_credit451)
async def sell_choosing_comissiya_cash_comission10(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosell=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="САМ",
    #     callback_data="САМ")
    # )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b6 ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_credit452)


@router.callback_query(SetReport.choosing_our_credit452, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_7)


@router.message(SetReport.choosing_our_credit452)
@router.inline_query(lambda query: query.query.startswith("find_b6 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b6 ")
    await state.set_state(SetReport.choosing_our_credit453)


@router.message(SetReport.choosing_our_credit453)
async def sell_choosing_comissiya_cash_comission12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosellcredit=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_7)


# _________________________________________________________
# @router.message(SetReport.choosing_our_credit3)
# async def sell_choosing_our_credit3(message: Message, state: FSMContext):
#     just = message.text.upper()
#     await state.update_data(howmuchtorg=int(re.sub("[^0-9]", "", just)))
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="САМ",
#         callback_data="САМ")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Нажмите, чтобы ввести фамилию",
#         switch_inline_query_current_chat='find_b7 ')
#     )
#     await message.answer(
#         text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
#     )
#     await state.set_state(SetReport.choosing_our_credit45)
#
#
# @router.callback_query(SetReport.choosing_our_credit45, F.data == "САМ")
# async def sell_choosing_our_credit45(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(whosell=callback.message.chat.first_name + callback.message.chat.last_name)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="САМ",
#         callback_data="САМ")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Нажмите, чтобы ввести фамилию",
#         switch_inline_query_current_chat='find_7 ')
#     )
#     await callback.message.answer(
#         text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
#         reply_markup=builder.as_markup()
#     )
#     await state.set_state(SetReport.choosing_our_credit6)
#
#
# @router.callback_query(SetReport.choosing_our_credit6, F.data == "САМ")
# async def sell_choosing_our_credit45(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(whosellcredit=callback.message.chat.first_name + callback.message.chat.last_name)
#     kb = [
#         [types.KeyboardButton(text="Без комментариев")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         one_time_keyboard=True,
#
#     )
#     await callback.message.answer(text="Комментарии", reply_markup=keyboard)
#     await state.set_state(SetReport.choosing_sell_editor_7)
#
#
# @router.message(SetReport.choosing_our_credit45)
# @router.inline_query(lambda query: query.query.startswith("find_b5 "))
# async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
#     await utils.inliner.find_colleges(inline_query, state, "find_b5 ")
#     await state.set_state(SetReport.choosing_our_credit5)
#
#
# @router.message(SetReport.choosing_our_credit5)
# async def sell_choosing_our_credit5(message: Message, state: FSMContext):
#     # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
#     # college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
#     await state.update_data(whosell=message.text.lower())
#     # if college_name == "Некорректный USERNAME":
#     #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="САМ",
#         callback_data="САМ")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Нажмите, чтобы ввести фамилию",
#         switch_inline_query_current_chat='find_b6 ')
#     )
#     await message.answer(
#         text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
#         reply_markup=builder.as_markup()
#     )
#     await state.set_state(SetReport.choosing_our_credit56)
#
#
# @router.message(SetReport.choosing_our_credit56)
# @router.inline_query(lambda query: query.query.startswith("find_b6 "))
# async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
#     await utils.inliner.find_colleges(inline_query, state, "find_b6 ")
#     await state.set_state(SetReport.choosing_our_credit8)


# ==================================================================================================
@router.message(SetReport.choosing_our_credit8)
async def constructor_choosing_wire(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    print('7')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_7)


@router.message(SetReport.choosing_sell_editor_7)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ: {data['whosellcredit']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_editor_start_7, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(summa_nm=None)
    await state.update_data(summa_sob=None)
    await state.update_data(howmuchtorg=None)
    await state.update_data(date_raschet=None)
    await state.update_data(type_raschet=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_7)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто оформил кредит", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_7_8(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_7)


# ===========================
@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s11 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s11 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s11 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_7)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s12 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s12 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s12 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_7)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


# ===========================


# @router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_who_sell")
# async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_sell(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_7)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_7)
# async def editor_who_sell_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_sell_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_7)
#
#
# @router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_who_credit")
# async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_credit(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_7)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_7)
# async def editor_who_credit_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_credit_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_7)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_7)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_7)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_7)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_7)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_7)


@router.message(SetReport.choosing_sell_editor_year_edit_7)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_7)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_7)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_7)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_7)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_7)


@router.callback_query(SetReport.choosing_sell_selector_7, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


# ==================================================================================================
# @router.message(SetReport.choosing_our_credit8)
# async def sell_choosing_our_credit8(message: Message, state: FSMContext):
#     await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
#     college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
#     await state.update_data(howsellcredit=college_name)
#     if college_name == "Некорректный USERNAME":
#         await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
#     data = await state.get_data()
#     print(data)
#     text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{message.chat.first_name + " " + message.chat.last_name}
#         '''
#     await message.answer(text=text)
#     await message.answer(
#         text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
#     await message.answer(text="/start")
#     await state.clear()


@router.callback_query(SetReport.choosing_our_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_OUR_CASH)
async def sell_choosing_our_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_our_cash)


@router.message(SetReport.choosing_our_cash)
async def sell_choosing_our_credit2(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_our_cash2)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_COST_DROM,
        )
        await state.set_state(SetReport.choosing_our_cash)


@router.message(SetReport.choosing_our_cash2)
async def sell_choosing_our_credit3(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(dealer_discount=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="САМ",
            callback_data="САМ")
        )
        builder.add(types.InlineKeyboardButton(
            text="Нажмите, чтобы ввести фамилию",
            switch_inline_query_current_chat='find_b9 ')
        )
        await message.answer(
            text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
        )
        await state.set_state(SetReport.choosing_our_cash45)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(
            text=texts.MESSAGE_SELL_DISCOUNT,
        )
        await state.set_state(SetReport.choosing_our_cash2)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# @router.message(SetReport.choosing_our_cash3)
# async def sell_choosing_comissiya_cash_comission8(message: Message, state: FSMContext):
#     current_state = await state.get_state()
#     print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
#     just = message.text.upper()
#     if just.isdigit():
#         await state.update_data(howmuchtorg=int(just))
#         builder = InlineKeyboardBuilder()
#         builder.add(types.InlineKeyboardButton(
#             text="САМ",
#             callback_data="САМ")
#         )
#         builder.add(types.InlineKeyboardButton(
#             text="Нажмите, чтобы ввести фамилию",
#             switch_inline_query_current_chat='find_b9 ')
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
#         )
#         await state.set_state(SetReport.choosing_our_cash45)
#     else:
#         await message.answer(
#             text=texts.MESSAGE_ONLY_DIGITS,
#         )
#         await message.answer(
#             text=texts.MESSAGE_SELL_TORG,
#         )
#         await state.set_state(SetReport.choosing_our_cash3)


@router.callback_query(SetReport.choosing_our_cash45, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission9(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosell="-")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b10 ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH_DKP + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_cash6)


@router.callback_query(SetReport.choosing_our_cash6, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_8)


@router.message(SetReport.choosing_our_cash45)
@router.inline_query(lambda query: query.query.startswith("find_b9 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b9 ")
    await state.set_state(SetReport.choosing_our_cash451)


@router.message(SetReport.choosing_our_cash451)
async def sell_choosing_comissiya_cash_comission10(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosell=college_name)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_b10 ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_DKP + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_cash452)


@router.callback_query(SetReport.choosing_our_cash452, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await state.update_data(whosellcredit=callback.message.chat.first_name + " " + callback.message.chat.last_name)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await callback.message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_8)


@router.message(SetReport.choosing_our_cash452)
@router.inline_query(lambda query: query.query.startswith("find_b10 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_b10 ")
    await state.set_state(SetReport.choosing_our_cash453)


@router.message(SetReport.choosing_our_cash453)
async def sell_choosing_comissiya_cash_comission12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = message.text
    await state.update_data(whosellcredit=college_name)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_8)


# _________________________________________________________
# @router.message(SetReport.choosing_our_cash3)
# async def sell_choosing_our_credit4(message: Message, state: FSMContext):
#     await state.update_data(howmuchtorg=message.text.lower())
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="САМ",
#         callback_data="САМ")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Нажмите, чтобы ввести фамилию",
#         switch_inline_query_current_chat='find_b8 ')
#     )
#     await message.answer(
#         text=texts.MESSAGE_SELL_WITH + "\nНажмите кнопку и введите первые символы фамилии коллеги",
#         reply_markup=builder.as_markup()
#     )
#     await state.set_state(SetReport.choosing_our_cash45)
#
#
# # @router.callback_query(SetReport.choosing_our_cash45, F.data == "САМ")
# # async def sell_choosing_comissiya_creditcomission9(callback: types.CallbackQuery, state: FSMContext):
# #     await state.update_data(whosell=callback.message.chat.first_name + callback.message.chat.last_name)
# #     builder = InlineKeyboardBuilder()
# #     builder.add(types.InlineKeyboardButton(
# #         text="САМ",
# #         callback_data="САМ")
# #     )
# #     builder.add(types.InlineKeyboardButton(
# #         text="Нажмите, чтобы ввести фамилию",
# #         switch_inline_query_current_chat='find_b8 ')
# #     )
# #     await callback.message.answer(
# #         text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
# #         reply_markup=builder.as_markup()
# #     )
# #     await state.set_state(SetReport.choosing_our_cash45)
#
#
# @router.callback_query(SetReport.choosing_our_cash45, F.data == "САМ")
# async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(whosell=callback.message.chat.first_name + callback.message.chat.last_name)
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="САМ",
#         callback_data="САМ")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text="Нажмите, чтобы ввести фамилию",
#         switch_inline_query_current_chat='find_b7 ')
#     )
#     await callback.message.answer(
#         text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
#         reply_markup=builder.as_markup()
#     )
#     await state.set_state(SetReport.choosing_our_cash5)
#
#
# @router.message(SetReport.choosing_our_cash5)
# @router.inline_query(lambda query: query.query.startswith("find_b7 "))
# async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
#     await utils.inliner.find_colleges(inline_query, state, "find_b7 ")
#     await state.set_state(SetReport.choosing_our_cash6)
#
#
# # @router.message(SetReport.choosing_our_cash5)
# # async def sell_choosing_our_credit5(message: Message, state: FSMContext):
# #     # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
# #     college_name = message.text.lower()
# #     await state.update_data(whosellcredit=college_name)
# #     # if college_name == "Некорректный USERNAME":
# #     #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
# #     builder = InlineKeyboardBuilder()
# #     builder.add(types.InlineKeyboardButton(
# #         text="САМ",
# #         callback_data="САМ")
# #     )
# #     builder.add(types.InlineKeyboardButton(
# #         text="Нажмите, чтобы ввести фамилию",
# #         switch_inline_query_current_chat='find_b8 ')
# #     )
# #     await message.answer(
# #         text=texts.MESSAGE_SELL_WITH_CREDIT + "\n9Нажмите кнопку и введите первые символы фамилии коллеги",
# #         reply_markup=builder.as_markup()
# #     )
# #     await state.set_state(SetReport.choosing_our_cash6)
#
#
# @router.callback_query(SetReport.choosing_our_cash5, F.data == "САМ")
# async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
#     await state.update_data(whosellcredit=callback.message.chat.first_name + callback.message.chat.last_name)
#     kb = [
#         [types.KeyboardButton(text="Без комментариев")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True,
#         one_time_keyboard=True,
#
#     )
#     await callback.message.answer(text="Комментарии", reply_markup=keyboard)
#     await state.set_state(SetReport.choosing_sell_editor_8)
#
#
# @router.message(SetReport.choosing_our_cash6)
# @router.inline_query(lambda query: query.query.startswith("find_b8 "))
# async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
#     await utils.inliner.find_colleges(inline_query, state, "find_b8 ")
#     await state.set_state(SetReport.choosing_sell_editor_8)


# ==================================================================================================
@router.message(SetReport.choosing_our_cash7)
async def constructor_choosing_wire(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    # await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    # college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(whosellcredit=message.text)
    # if college_name == "Некорректный USERNAME":
    #     await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    data = await state.get_data()
    print('8')
    print(data)
    kb = [
        [types.KeyboardButton(text="Без комментариев")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True,

    )
    await message.answer(text="Комментарии", reply_markup=keyboard)
    await state.set_state(SetReport.choosing_sell_editor_8)


@router.message(SetReport.choosing_sell_editor_8)
async def constructor_choosing_wire12(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await state.update_data(chosen_comment=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Редактировать",
        callback_data="edit_menu_start")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все ок",
        callback_data="edit_menu_finish"
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ПИСАЛ ДКП: {data['whosellcredit']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\nИнициатор: {message.chat.first_name + " " + message.chat.last_name}
            '''

    await message.answer(
        text=text, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_editor_start_8, F.data == "edit_menu_finish")
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(summa_nm=None)
    await state.update_data(summa_sob=None)
    await state.update_data(howmuchtorg=None)
    await state.update_data(date_raschet=None)
    await state.update_data(type_raschet=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_sell_editor_start_8)
async def constructor_editor_start(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    dict_editor = {'editor_start':
                       {'text': ["C кем продал", "Кто писал ДКП", "Цена дром", "Гос номер", "Марка", "Модель",
                                 "Год", "VIN",
                                 "Комментарий", "Все ок"],
                        'data': ["edit_menu_who_sell", "edit_menu_who_credit", "edit_menu_drom_cost",
                                 "edit_menu_gosnumber", "edit_menu_marka",
                                 "edit_menu_model", "edit_menu_year", "edit_menu_vin", "edit_menu_comment",
                                 "edit_menu_finish"]}}

    await utils.editor_sell.editor_start_7_8(callback, state, dict_editor)
    await state.set_state(SetReport.choosing_sell_selector_8)


# ===========================
@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_who_sell")
async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    # await utils.editor_sell.editor_who_sell(callback, state)
    # await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_2)
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s13 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s13 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s13 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_8)
async def editor_who_sell_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_sell_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_who_credit")
async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_s14 ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


@router.inline_query(lambda query: query.query.startswith("find_s14 "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER  на стейте {current_state}")
    await utils.inliner.find_colleges(inline_query, state, "find_s14 ")
    await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_8)
async def editor_who_credit_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_who_credit_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


# ===========================


# @router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_who_sell")
# async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_sell(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_sell_edit_8)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_sell_edit_8)
# async def editor_who_sell_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_sell_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_8)
#
#
# @router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_who_credit")
# async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_sell.editor_who_credit(callback, state)
#     await state.set_state(SetReport.choosing_sell_editor_menu_who_credit_edit_8)
#
#
# @router.message(SetReport.choosing_sell_editor_menu_who_credit_edit_8)
# async def editor_who_credit_edit(message: Message, state: FSMContext):
#     await utils.editor_sell.editor_who_credit_edit(message, state)
#     await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_drom_cost")
async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_drom_cost(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_drom_cost_edit_8)
async def editor_drom_cost_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(drom_cost=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['drom_cost']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_8)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_menu_drom_cost_edit_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_gosnumber")
async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_gosnumber_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_gosnumber_edit_8)
async def editor_gosnumber_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_gosnumber_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_marka")
async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_marka_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_marka_edit_8)
async def editor_marka_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_marka_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_model")
async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_model_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_model_edit_8)
async def editor_model_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_model_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_year")
async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_year(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_year_edit_8)


@router.message(SetReport.choosing_sell_editor_year_edit_8)
async def editor_year_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(chosen_vin_year=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['chosen_vin_year']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_sell_editor_start_8)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await state.set_state(SetReport.choosing_sell_editor_year_edit_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_vin")
async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_vin_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_vin_edit_8)
async def editor_vin_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_vin_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_comment")
async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment(callback, state)
    await state.set_state(SetReport.choosing_sell_editor_menu_comment_edit_8)


@router.message(SetReport.choosing_sell_editor_menu_comment_edit_8)
async def editor_comment_edit(message: Message, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {message.chat.username} на стейте {current_state}")
    await utils.editor_sell.editor_comment_edit(message, state)
    await state.set_state(SetReport.choosing_sell_editor_start_8)


@router.callback_query(SetReport.choosing_sell_selector_8, F.data == "edit_menu_finish")
async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    print(f"PRINTER_LOGGER {callback.message.chat.username} на стейте {current_state}")
    await callback.message.answer("Подождите, идет выгрузка отчета")
    await state.update_data(howmuchtorg=None)
    data = await state.get_data()
    await utils.connectors.db_sql_sell_insert(callback, data)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()
