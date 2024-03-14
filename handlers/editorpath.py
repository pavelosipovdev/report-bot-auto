from aiogram import Router, F, types, Bot
from aiogram.filters import command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher
# from utils.editor_comission import router
from utils import editor_comission
from keyboards import editor

import psycopg2
import os

import utils
from utils import downloader, connectors, convert, api, inliner
from texts import texts

router = Router()


class SetReport(StatesGroup):
    choosing_editor_1 = State()
    choosing_editor_2 = State()
    choosing_editor_3 = State()
    choosing_editor_4 = State()
    choosing_editor_5 = State()
    choosing_editor_6 = State()
    choosing_editor_7 = State()
    choosing_editor_8 = State()
    choosing_editor_9 = State()
    choosing_editor_10 = State()


@router.callback_query(F.data == "start_editor")
async def main_menu_bt_constructor_editor(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_1_SELL,
        callback_data="editor_buy_start")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_1_BUY,
        callback_data="editor_buy_start")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_COMISSION,
        callback_data="editor_comission_start")
    )
    await callback.message.answer(text="Выберите тип сделки", reply_markup=builder.as_markup())

    await state.set_state(SetReport.choosing_editor_1)


@router.callback_query(SetReport.choosing_editor_1, F.data == "editor_buy_start")
async def main_menu_bt_constructor_editor(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите VIN авто")
    await state.set_state(SetReport.choosing_editor_2)


@router.callback_query(SetReport.choosing_editor_1, F.data == "editor_comission_start")
async def main_menu_bt_constructor_editor(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите VIN авто")
    await state.set_state(SetReport.choosing_editor_6)


@router.callback_query(SetReport.choosing_editor_1, F.data == "editor_sell_start")
async def main_menu_bt_constructor_editor(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите VIN авто")
    await state.set_state(SetReport.choosing_editor_9)


@router.message(SetReport.choosing_editor_2)
async def main_menu_bt_constructor_editor(message: types.Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите")
    buy_data = utils.connectors.db_sql_buy_editor_select(message.text.upper(), message)
    await state.update_data(dict_buy_data=buy_data)
    rezina = 'Есть' if buy_data[5] else 'Нет'
    try:
        text = f'''
    Тип отчета - {buy_data[0]}\nГде купил - {buy_data[1]}\nКто купил - {buy_data[2]}\nКто писал ДКП - {buy_data[3]}\nЦена - {buy_data[4]}\n
Резина - {rezina}\nVIN номер - {buy_data[6]}\nГос номер - {buy_data[7]}\nМарка - {buy_data[8]}\nМодель - {buy_data[9]}\n
Год - {buy_data[10]}\nКомментарий - {buy_data[11]}\n
    '''
    except IndexError as e:
        print(e)
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="start_editor")
        )
        await message.answer(text=f"Ошибка {e}, попробуйте сначала", reply_markup=builder.as_markup())
    await message.answer(text=text)
    await message.answer(text="Какое значение хотите изменить?", reply_markup=editor.get_buy_keyboard_page1())
    await state.set_state(SetReport.choosing_editor_3)


@router.message(SetReport.choosing_editor_6)
async def main_menu_bt_constructor_editor(message: types.Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите")
    comission_data = utils.connectors.db_sql_comission_editor_select(message.text.upper(), message)
    await state.update_data(dict_comission_data=comission_data)
    try:
        text = f'''
    Тип отчета - {comission_data[0]}\nГде купил - {comission_data[1]}\nВид расчета - {comission_data[12]}\nКто купил - {comission_data[2]}\nКто писал ДКП - {comission_data[3]}\nСколько собственнику - {comission_data[4]}\n
Комиссия - {comission_data[5]}\nVIN номер - {comission_data[6]}\nГос номер - {comission_data[7]}\nМарка - {comission_data[8]}\nМодель - {comission_data[9]}\n
Год - {comission_data[10]}\nКомментарий - {comission_data[11]}\n
    '''
    except IndexError as e:
        print(e)
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="Назад",
            callback_data="start_editor")
        )
        await message.answer(text=f"Ошибка {e}, попробуйте сначала", reply_markup=builder.as_markup())
    await message.answer(text=text)
    await message.answer(text="Какое значение хотите изменить?", reply_markup=editor.get_comission_keyboard_page1())
    await state.set_state(SetReport.choosing_editor_7)
