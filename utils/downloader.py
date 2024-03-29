import os
import time

from aiogram import Router, F, types, Bot
from aiogram.filters import command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hlink

from utils import convert, api
from texts import texts
from pathlib import Path

htext = hlink('Техподдержкой', 'https://t.me/paitssupport')


async def handle_photo(message: Message, bot: Bot):
    # Путь к папке для сохранения
    save_path = Path("tmp")
    save_path.mkdir(exist_ok=True)  # Создаем папку, если она еще не существует
    await message.answer(text="Подождите пожалуйста")
    # Сохраняем фото
    photo_file_id = message.photo[-1].file_id
    destination = save_path / f"{photo_file_id}.jpg"
    await bot.download(message.photo[-1], destination=destination)
    convert.convert_json_japan(f"tmp/{message.photo[-1].file_id}.jpg")



    # Оставляем только последние 10 файлов
    keep_last_n_files(save_path, 10)


async def handle_photo_vin(message: Message, bot: Bot):
    # Путь к папке для сохранения
    save_path = Path("tmp")
    save_path.mkdir(exist_ok=True)  # Создаем папку, если она еще не существует

    # Сохраняем фото
    photo_file_id = message.photo[-1].file_id
    destination = save_path / f"{photo_file_id}.jpg"
    await bot.download(message.photo[-1], destination=destination)
    await message.answer(text="Подождите пожалуйста")
    convert.convert_json_vin(destination)

    # Оставляем только последние 10 файлов
    keep_last_n_files(save_path, 10)


def keep_last_n_files(directory, n):
    # Получаем список всех файлов в папке
    files = list(directory.iterdir())
    if len(files) <= n:
        return  # Ничего делать не нужно, если файлов меньше или равно n

    # Сортируем файлы по времени модификации (от самых старых к новым)
    files.sort(key=lambda x: x.stat().st_mtime)

    # Удаляем самые старые, чтобы осталось только n последних
    for file in files[:-n]:
        file.unlink()


async def constructor_choosing_electro(message: Message, state: FSMContext, bot: Bot):
    global this_year
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_EDIT,
        callback_data=texts.BT_EDIT)
    )

    await handle_photo(message, bot)
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

    # 46 - year [25],  47 - year [26]
    print(len(doka))
    try:
        print(doka[6], doka[8], doka[10], doka[26])
    except Exception as e:
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        await message.answer(
            text=f"Фото не поддерживается, свяжитесь с {htext}", parse_mode="HTML",reply_markup=builder2.as_markup())

        await bot.send_message(os.getenv('ERROR_CHAT_ID'),
                               f"Error \n{e} \nfor " + message.chat.first_name + " " + message.chat.last_name)
    if len(doka) == 47:
        msg2 = f'''В базу внесено:
        Год: {str(doka[26]).upper()}
        VIN: {str(doka[21]).upper()}
        Марка: {str(doka[8]).upper()}
        Модель: {str(doka[10]).upper()}
        '''
        await message.answer(text=msg2, reply_markup=builder.as_markup())
        await state.update_data(chosen_vin_gos_number="NONE", chosen_vin_number=str(doka[21]).upper(),
                                chosen_vin_marka=str(doka[8]).upper(), chosen_vin_model=str(doka[10]).upper(),
                                chosen_vin_year=str(doka[26]).upper())
    elif len(doka) == 46:
        msg2 = f'''В базу внесено:
        Год: {str(doka[25]).upper()}
        VIN: {str(doka[19]).upper()}
        Марка: {str(doka[8]).upper()}
        Модель: {str(doka[10]).upper()}
        '''
        await message.answer(text=msg2, reply_markup=builder.as_markup())
        await state.update_data(chosen_vin_gos_number="NONE", chosen_vin_number=str(doka[19]).upper(),
                                chosen_vin_marka=str(doka[8]).upper(), chosen_vin_model=str(doka[10]).upper(),
                                chosen_vin_year=str(doka[25]).upper())
    elif len(doka) == 44:
        msg2 = f'''В базу внесено:
        Год: {str(doka[24]).upper()}
        VIN: {str(doka[20]).upper()}
        Марка: {str(doka[7]).upper()}
        Модель: {str(doka[9]).upper()}
        '''
        await message.answer(text=msg2, reply_markup=builder.as_markup())
        await state.update_data(chosen_vin_gos_number="NONE", chosen_vin_number=str(doka[20]).upper(),
                                chosen_vin_marka=str(doka[7]).upper(), chosen_vin_model=str(doka[9]).upper(),
                                chosen_vin_year=str(doka[24]).upper())
    else:
        for i in doka:
            if i.isdigit() and len(
                    i) == 4:  # Проверка, что i является числом и имеет длину 4 символа (предполагая, что год состоит из 4 цифр)
                this_year = int(i)  # Преобразование года в целое число
                # Далее можно добавить необходимую логику для обработки года
                print(f"Найден год: {this_year}")
                break
        vin_number_sts = doka[6]
        marka_sts = doka[8]
        model_sts = doka[10]
        if str(doka[4]).upper() == "ИДЕНТИФИКАЦИОННЫЙ":
            vin_number_sts = doka[5]
        if str(doka[7]).upper() == "МАРКА":
            marka_sts = doka[8]
        if str(doka[9]).upper() == "КОММЕРЧЕСКОЕ":
            model_sts = doka[10]

        msg2 = f'''В базу внесено:
        Год: {str(this_year)}
        VIN: {str(vin_number_sts).upper()}
        Марка: {str(marka_sts).upper()}
        Модель: {str(model_sts).upper()}
        '''
        await message.answer(text=msg2, reply_markup=builder.as_markup())
        await state.update_data(chosen_vin_gos_number="NONE", chosen_vin_number=str(vin_number_sts).upper(),
                                chosen_vin_marka=str(marka_sts).upper(), chosen_vin_model=str(model_sts).upper(),
                                chosen_vin_year=str(this_year))


async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_EDIT,
        callback_data=texts.BT_EDIT)
    )
    await handle_photo_vin(message, bot)
    msg = api.get_strings_vin()
    print(msg)
    doka = []
    for i in msg:
        if i["name"] == "stsfront_car_year":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_number":
            doka.append(i["text"])
        # elif i["name"] == "stsfront_vin_number":
        elif i["name"] == "stsfront_car_trailer_number":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_brand":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_model":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_color":
            doka.append(i["text"])

    print(doka)
    msg2 = f'''В базу внесено:
    Год: {str(doka[0]).upper()}
    Гос номер: {str(doka[1]).upper()}
    VIN: {str(doka[4]).upper()}
    Марка: {str(doka[2]).upper()}
    Модель: {str(doka[3]).upper()}
    '''
    await state.update_data(chosen_vin_gos_number=str(doka[1]).upper(), chosen_vin_number=str(doka[4]).upper(),
                            chosen_vin_marka=str(doka[2]).upper(), chosen_vin_model=str(doka[3]).upper(),
                            chosen_vin_year=str(doka[0]).upper())
    await message.answer(text=msg2, reply_markup=builder.as_markup())


async def constructor_choosing_vin_checker(message: Message, state: FSMContext, bot: Bot):
    await handle_photo_vin(message, bot)
    msg = api.get_strings_vin()
    print(msg)
    doka = []
    for i in msg:
        if i["name"] == "stsfront_car_year":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_number":
            doka.append(i["text"])
        # elif i["name"] == "stsfront_vin_number":
        elif i["name"] == "stsfront_car_trailer_number":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_brand":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_model":
            doka.append(i["text"])
        elif i["name"] == "stsfront_car_color":
            doka.append(i["text"])

    print(doka)
    await state.update_data(chosen_vin_gos_number=str(doka[1]).upper(), chosen_vin_number=str(doka[4]).upper(),
                            chosen_vin_marka=str(doka[2]).upper(), chosen_vin_model=str(doka[3]).upper(),
                            chosen_vin_year=str(doka[0]).upper())


async def constructor_choosing_japan(message: Message, state: FSMContext, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )
    # await bot.download(
    #     message.photo[-1],
    #     destination=f"tmp/{message.photo[-1].file_id}.jpg"
    #
    # )
    # await message.answer(text="Подождите пожалуйста", reply_markup=builder.as_markup())
    # convert.convert_json_japan(f"tmp/{message.photo[-1].file_id}.jpg")
    await handle_photo(message, bot)
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
