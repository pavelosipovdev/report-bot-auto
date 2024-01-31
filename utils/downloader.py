from aiogram import Router, F, types, Bot
from aiogram.filters import command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import convert, api
from texts import texts


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
    await message.answer(text="Подождите пожалуйста")
    convert.convert_json_japan(f"tmp/{message.photo[-1].file_id}.jpg")
    msg = api.get_strings_japan()
    doka = []
    for i in msg:
        if i["lines"][0]["words"][0]["text"]:
            doka.append(i["lines"][0]["words"][0]["text"])
    print(doka)
    for k in doka:
        if len(k) == 14 and str(k[13]).isdigit():
            electro_vin = str(k).upper()
            print(electro_vin)
    print(doka[6], doka[8], doka[10], doka[26])
    msg2 = f'''В базу внесено:
    Год {str(doka[26]).upper()}
    VIN {str(doka[6]).upper()}
    Марка {str(doka[8]).upper()}
    Модель {str(doka[10]).upper()}
    '''
    await message.answer(text=msg2, reply_markup=builder.as_markup())
    await state.update_data(chosen_vin_gos_number="NONE", chosen_vin_number=str(doka[6]).upper(),
                            chosen_vin_marka=str(doka[8]).upper(), chosen_vin_model=str(doka[10]).upper(),
                            chosen_vin_year=str(doka[25]).upper())


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
                                                    0]).upper())
    await message.answer(text=msg2, reply_markup=builder.as_markup())

async def constructor_choosing_japan(message: Message, state: FSMContext, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
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
    japan_vin = 'UNKNOWN'
    for i in msg:
        if i["lines"][0]["words"][0]["text"]:
            doka.append(i["lines"][0]["words"][0]["text"])
    # print(doka)
    for k in doka:
        if len(k) == 13:
            japan_vin = str(k).upper()

    msg2 = f'''В базу внесено:
    VIN {japan_vin}
    '''

    await message.answer(text=msg2, reply_markup=builder.as_markup())
