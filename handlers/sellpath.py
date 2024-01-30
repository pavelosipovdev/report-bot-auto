from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

import utils.connectors
from utils import convert, api
from texts import texts

router = Router()

import re


class SetReport(StatesGroup):
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
    choosing_sell_data_car = State()
    choosing_sell_vin = State()
    choosing_sell_pts = State()
    choosing_sell_data_car_marka = State()
    choosing_sell_data_car_model = State()
    choosing_sell_data_car_year = State()
    choosing_sell_data_car_gosnumber = State()
    choosing_sell_data_car_next = State()
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
    choosing_sell_comment = State()
    choosing_sell_editor = State()
    choosing_sell_editor_start = State()
    choosing_sell_editor_first = State()
    choosing_sell_editor_first_place = State()
    choosing_sell_editor_first_cost = State()
    choosing_sell_editor_first_vin_gos_number = State()
    choosing_sell_editor_first_vin_marka = State()
    choosing_sell_editor_first_vin_model = State()
    choosing_sell_editor_first_vin_year = State()
    choosing_sell_editor_first_vin_number = State()
    choosing_sell_editor_first_comment = State()
    choosing_sell_editor_finish = State()
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
    choosing_our_credit5 = State()
    choosing_our_credit6 = State()
    choosing_our_credit7 = State()
    choosing_our_credit8 = State()
    choosing_our_cash = State()
    choosing_our_cash2 = State()
    choosing_our_cash3 = State()
    choosing_our_cash4 = State()
    choosing_our_cash45 = State()
    choosing_our_cash5 = State()
    choosing_our_cash6 = State()
    choosing_our_cash7 = State()
    choosing_our_cash8 = State()
    choosing_our_cash9 = State()


@router.callback_query(F.data == texts.BT_CONSTRUCTOR_1_SELL)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer1=callback.data)
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
    await state.set_state(SetReport.choosing_sell_data_car)
    await callback.message.delete()


@router.callback_query(SetReport.choosing_sell_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_VIN_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON2)
    await state.set_state(SetReport.choosing_sell_vin)


@router.callback_query(SetReport.choosing_sell_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_PTS_DOWNLOAD)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU_BUY_BUTTON22)
    await state.set_state(SetReport.choosing_sell_pts)


@router.callback_query(SetReport.choosing_sell_data_car, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_button2(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Укажите VIN")
    await state.set_state(SetReport.choosing_sell_data_car_marka)


@router.message(SetReport.choosing_sell_data_car_marka)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_number=message.text.upper())
    await message.answer(text="Укажите марку")
    await state.set_state(SetReport.choosing_sell_data_car_model)


@router.message(SetReport.choosing_sell_data_car_model)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_marka=message.text.upper())
    await message.answer(text="Укажите модель")
    await state.set_state(SetReport.choosing_sell_data_car_year)


@router.message(SetReport.choosing_sell_data_car_year)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_model=message.text.upper())
    await message.answer(text="Укажите год")
    await state.set_state(SetReport.choosing_sell_data_car_gosnumber)


@router.message(SetReport.choosing_sell_data_car_gosnumber)
async def main_menu_button2(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_year=message.text.upper())
    await message.answer(text="Укажите гоc номер")
    await state.set_state(SetReport.choosing_sell_data_car_next)


@router.message(SetReport.choosing_sell_data_car_next)
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
    await state.set_state(SetReport.choosing_comissiya_our)


@router.message(SetReport.choosing_sell_vin, F.photo)
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
    await state.set_state(SetReport.choosing_comissiya_our)


@router.message(SetReport.choosing_sell_pts, F.photo)
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
    await state.set_state(SetReport.choosing_comissiya_our)


@router.callback_query(SetReport.choosing_comissiya_our)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer3=callback.data)
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
    await state.set_state(SetReport.choosing_comissiya_our2)
    # 


@router.callback_query(SetReport.choosing_comissiya_our2, F.data == texts.BT_COMISSION)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_credit_our=callback.data)
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
    # 


@router.callback_query(SetReport.choosing_comissiya_our2, F.data == texts.BT_OUR)
async def main_menu_bt_constructor_12_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_credit_our=callback.data)
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
    # 


@router.callback_query(SetReport.choosing_comissiya_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT)
async def sell_choosing_comissiya_credit_comission(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_comissiya_credit2)


@router.message(SetReport.choosing_comissiya_credit2)
async def sell_choosing_comissiya_credit_comission2(message: Message, state: FSMContext):
    await state.update_data(drom_cost=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_DISCOUNT,
    )
    await state.set_state(SetReport.choosing_comissiya_credit3)


@router.message(SetReport.choosing_comissiya_credit3)
async def sell_choosing_comissiya_credit_comission3(message: Message, state: FSMContext):
    await state.update_data(dealer_discount=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_SUM_NM,
    )
    await state.set_state(SetReport.choosing_comissiya_credit4)


@router.message(SetReport.choosing_comissiya_credit4)
async def sell_choosing_comissiya_creditcomission4(message: Message, state: FSMContext):
    await state.update_data(summa_nm=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SUM_SOBS,
    )
    await state.set_state(SetReport.choosing_comissiya_credit5)


@router.message(SetReport.choosing_comissiya_credit5)
async def sell_choosing_comissiya_creditcomission5(message: Message, state: FSMContext):
    await state.update_data(summa_sob=message.text.lower())
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
    await message.answer(
        text="СУММА СОБСТВЕННИКУ " + data['summa_sob'], reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit6)


@router.callback_query(SetReport.choosing_comissiya_credit6, F.data == "callback_edit")
async def sell_choosing_comissiya_creditcomission6(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="На какую сумму хотите изменить?",
    )
    await state.set_state(SetReport.choosing_comissiya_credit78)


@router.message(SetReport.choosing_comissiya_credit78)
async def sell_choosing_comissiya_creditcomission78(message: Message, state: FSMContext):
    await state.update_data(summa_sob=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_TORG,
    )
    await state.set_state(SetReport.choosing_comissiya_credit8)


@router.callback_query(SetReport.choosing_comissiya_credit6, F.data == "callback_ostav")
async def sell_choosing_comissiya_creditcomission6(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text=texts.MESSAGE_SELL_TORG,
    )
    await state.set_state(SetReport.choosing_comissiya_credit8)


@router.message(SetReport.choosing_comissiya_credit8)
async def sell_choosing_comissiya_creditcomission8(message: Message, state: FSMContext):
    await state.update_data(howmuchtorg=message.text.lower())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_comissiya_credit ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit9)


@router.callback_query(SetReport.choosing_comissiya_credit9, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission9(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(howsell=callback.message.chat.first_name + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_comissiya_credit_credit ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit101)


@router.callback_query(SetReport.choosing_comissiya_credit101, F.data == "САМ")
async def sell_choosing_comissiya_creditcomission101(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(howsellcredit=callback.message.chat.first_name + callback.message.chat.last_name)
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
@router.inline_query(lambda query: query.query.startswith("find_colleges_comissiya_credit "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    #     builder.add(types.InlineKeyboardButton(
    #         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
    #         callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    #     )
    # Здесь ты можешь реализовать логику поиска колледжа и создать список результатов
    results = []

    # Получение дополнительных символов из запроса
    query = inline_query.query
    query = query.replace("find_colleges_comissiya_credit ", "").strip()

    # Поиск колледжей, название или адрес которых содержит дополнительные символы
    # Здесь ты можешь использовать свою базу данных или API для получения данных о колледжах
    # Для примера я буду использовать список колледжей в Москве
    # colleges = [
    #     {"id": "1", "name": "Осипов Павел", "tag": "rogerthatdev"},
    #     {"id": "2", "name": "Чудин Павел", "tag": "p_chudin"}
    # ]

    # Фильтрация колледжей по дополнительным символам
    for college in utils.connectors.dict_colleges:
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
    await state.set_state(SetReport.choosing_comissiya_credit10)


@router.message(SetReport.choosing_comissiya_credit10)
async def sell_choosing_our_credit5(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsell=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_colleges_comissiya_credit_credit ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit11)


@router.message(SetReport.choosing_comissiya_credit11)
@router.inline_query(lambda query: query.query.startswith("find_colleges_comissiya_credit_credit "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    results = []

    query = inline_query.query
    query = query.replace("find_colleges_comissiya_credit_credit ", "").strip()

    for college in utils.connectors.dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_comissiya_credit12)


@router.message(SetReport.choosing_comissiya_credit12)
async def sell_choosing_our_credit12(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsellcredit=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
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


@router.callback_query(SetReport.choosing_comissiya_credit13, F.data == texts.BT_NO)
async def sell_choosing_comissiya_creditcomission13(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''
    await callback.message.answer(text=text)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_comissiya_credit13, F.data == texts.BT_YES)
async def sell_choosing_comissiya_creditcomission13(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text=texts.MESSAGE_DATE_RASCHET,
    )
    await state.set_state(SetReport.choosing_comissiya_credit14)


@router.message(SetReport.choosing_comissiya_credit14)
async def sell_choosing_comissiya_creditcomission14(message: Message, state: FSMContext):
    await state.update_data(date_raschet=message.text.lower())
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
        text=texts.MESSAGE_TYPE_RASCHETA_WAS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_credit15)


@router.callback_query(SetReport.choosing_comissiya_credit15)
async def sell_choosing_comissiya_creditcomission15(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_raschet="ZAGLUSHKA (НАЛ/БЕЗНАЛ)")
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
    await state.set_state(SetReport.choosing_comissiya_credit16)


@router.callback_query(SetReport.choosing_comissiya_credit16, F.data == "callback_edit")
async def sell_choosing_comissiya_creditcomission6(callback: types.CallbackQuery, state: FSMContext):
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
        text="На какую вид расчета хотите изменить?",
    )
    await state.set_state(SetReport.choosing_comissiya_credit16)


@router.callback_query(SetReport.choosing_comissiya_credit167)
async def sell_choosing_comissiya_creditcomission167(callback: types.CallbackQuery, state: FSMContext):
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


@router.callback_query(SetReport.choosing_comissiya_credit17)
async def sell_choosing_comissiya_creditcomission17(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''
    await callback.message.answer(text=text)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_comissiya_credit16, F.data == "callback_ostav")
async def sell_choosing_comissiya_creditcomission16(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''
    await callback.message.answer(text=text)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_comissiya_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_COMISSION_CASH)
async def sell_choosing_comissiya_cash_comission(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_comissiya_cash2)


@router.message(SetReport.choosing_comissiya_cash2)
async def sell_choosing_comissiya_cash_comission2(message: Message, state: FSMContext):
    await state.update_data(drom_cost=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_DISCOUNT,
    )
    await state.set_state(SetReport.choosing_comissiya_cash3)


@router.message(SetReport.choosing_comissiya_cash3)
async def sell_choosing_comissiya_cash_comission3(message: Message, state: FSMContext):
    await state.update_data(dealer_discount=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_SUM_NM,
    )
    await state.set_state(SetReport.choosing_comissiya_cash4)


@router.message(SetReport.choosing_comissiya_cash4)
async def sell_choosing_comissiya_cash_comission4(message: Message, state: FSMContext):
    await state.update_data(summa_nm=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SUM_SOBS,
    )
    await state.set_state(SetReport.choosing_comissiya_cash5)


@router.message(SetReport.choosing_comissiya_cash5)
async def sell_choosing_comissiya_cash_comission5(message: Message, state: FSMContext):
    await state.update_data(summa_sob=message.text.lower())
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
    await message.answer(
        text="СУММА СОБСТВЕННИКУ " + data['summa_sob'], reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash6)


@router.callback_query(SetReport.choosing_comissiya_cash6, F.data == "callback_edit")
async def sell_choosing_comissiya_cash_comission6(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="На какую сумму хотите изменить?",
    )
    await state.set_state(SetReport.choosing_comissiya_cash78)


@router.message(SetReport.choosing_comissiya_cash78)
async def sell_choosing_comissiya_cash_comission78(message: Message, state: FSMContext):
    await state.update_data(summa_sob=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_TORG,
    )
    await state.set_state(SetReport.choosing_comissiya_cash8)


@router.callback_query(SetReport.choosing_comissiya_cash6, F.data == "callback_ostav")
async def sell_choosing_comissiya_cash_comission6(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text=texts.MESSAGE_SELL_TORG,
    )
    await state.set_state(SetReport.choosing_comissiya_cash8)


@router.message(SetReport.choosing_comissiya_cash8)
async def sell_choosing_comissiya_cash_comission8(message: Message, state: FSMContext):
    await state.update_data(howmuchtorg=message.text.lower())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_comissiya_credit ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash9)


@router.callback_query(SetReport.choosing_comissiya_cash9, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission9(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(howsell=callback.message.chat.first_name + callback.message.chat.last_name)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_comissiya_credit_credit ')
    )
    await callback.message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash101)


@router.callback_query(SetReport.choosing_comissiya_cash101, F.data == "САМ")
async def sell_choosing_comissiya_cash_comission101(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(howsellcredit=callback.message.chat.first_name + callback.message.chat.last_name)
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
@router.inline_query(lambda query: query.query.startswith("find_colleges_comissiya_credit "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    #     builder.add(types.InlineKeyboardButton(
    #         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
    #         callback_data=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE)
    #     )
    # Здесь ты можешь реализовать логику поиска колледжа и создать список результатов
    results = []

    # Получение дополнительных символов из запроса
    query = inline_query.query
    query = query.replace("find_colleges_comissiya_credit ", "").strip()

    # Поиск колледжей, название или адрес которых содержит дополнительные символы
    # Здесь ты можешь использовать свою базу данных или API для получения данных о колледжах
    # Для примера я буду использовать список колледжей в Москве
    # colleges = [
    #     {"id": "1", "name": "Осипов Павел", "tag": "rogerthatdev"},
    #     {"id": "2", "name": "Чудин Павел", "tag": "p_chudin"}
    # ]

    # Фильтрация колледжей по дополнительным символам
    for college in utils.connectors.dict_colleges:
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
    await state.set_state(SetReport.choosing_comissiya_cash10)


@router.message(SetReport.choosing_comissiya_cash10)
async def sell_choosing_comissiya_cash_comission10(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsell=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="САМ",
        callback_data="САМ")
    )
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_comissiya_credit_credit ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash11)


@router.message(SetReport.choosing_comissiya_cash11)
@router.inline_query(lambda query: query.query.startswith("find_colleges_comissiya_credit_credit "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    results = []

    query = inline_query.query
    query = query.replace("find_colleges_comissiya_credit_credit ", "").strip()

    for college in utils.connectors.dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_comissiya_cash12)


@router.message(SetReport.choosing_comissiya_cash12)
async def sell_choosing_comissiya_cash_comission12(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsellcredit=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
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


@router.callback_query(SetReport.choosing_comissiya_cash13, F.data == texts.BT_NO)
async def sell_choosing_comissiya_cash_comission13(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''
    await callback.message.answer(text=text)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_comissiya_cash13, F.data == texts.BT_YES)
async def sell_choosing_comissiya_cash_comission13(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text=texts.MESSAGE_DATE_RASCHET,
    )
    await state.set_state(SetReport.choosing_comissiya_cash14)


@router.message(SetReport.choosing_comissiya_cash14)
async def sell_choosing_comissiya_cash_comission14(message: Message, state: FSMContext):
    await state.update_data(date_raschet=message.text.lower())
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
        text=texts.MESSAGE_TYPE_RASCHETA_WAS, reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_comissiya_cash15)


@router.callback_query(SetReport.choosing_comissiya_cash15)
async def sell_choosing_comissiya_cash_comission15(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_raschet="ZAGLUSHKA (НАЛ/БЕЗНАЛ)")
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
        text="На какую вид расчета хотите изменить?",
    )
    await state.set_state(SetReport.choosing_comissiya_cash16)


@router.callback_query(SetReport.choosing_comissiya_cash167)
async def sell_choosing_comissiya_cash_comission167(callback: types.CallbackQuery, state: FSMContext):
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


@router.callback_query(SetReport.choosing_comissiya_cash17)
async def sell_choosing_comissiya_cash_comission17(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''
    await callback.message.answer(text=text)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_comissiya_cash16, F.data == "callback_ostav")
async def sell_choosing_comissiya_cash_comission16(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''
    await callback.message.answer(text=text)
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_our_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_OUR_CREDIT)
async def sell_choosing_our_credit0(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_our_credit2)


@router.message(SetReport.choosing_our_credit)
async def sell_choosing_our_credit1(message: Message, state: FSMContext):
    await state.update_data(drom_cost=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_DISCOUNT,
    )
    await state.set_state(SetReport.choosing_our_credit2)


@router.message(SetReport.choosing_our_credit2)
async def sell_choosing_our_credit2(message: Message, state: FSMContext):
    await state.update_data(dealer_discount=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_TORG,
    )
    await state.set_state(SetReport.choosing_our_credit3)


@router.message(SetReport.choosing_our_credit3)
async def sell_choosing_our_credit3(message: Message, state: FSMContext):
    await state.update_data(howmuchtorg=message.text.lower())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH + "\nВведите первые символы фамилии коллеги", reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_credit45)


@router.message(SetReport.choosing_our_credit45)
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
    for college in utils.connectors.dict_colleges:
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
    await state.set_state(SetReport.choosing_our_credit5)


@router.message(SetReport.choosing_our_credit5)
async def sell_choosing_our_credit5(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsell=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_dkp ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_CREDIT + "\nВведите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_credit6)


@router.message(SetReport.choosing_our_credit6)
@router.inline_query(lambda query: query.query.startswith("find_colleges_dkp "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    results = []

    query = inline_query.query
    query = query.replace("find_colleges_dkp ", "").strip()

    for college in utils.connectors.dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_our_credit8)


@router.message(SetReport.choosing_our_credit8)
async def sell_choosing_our_credit8(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsellcredit=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['howsellcredit']}\n\n{message.chat.first_name + " " + message.chat.last_name}
        '''
    await message.answer(text=text)
    await message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_our_credit_cash, F.data == texts.BT_CONSTRUCTOR_3_OUR_CASH)
async def sell_choosing_our_credit(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(type_deal=callback.data)
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_our_cash)


@router.message(SetReport.choosing_our_cash)
async def sell_choosing_our_credit2(message: Message, state: FSMContext):
    await state.update_data(drom_cost=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_DISCOUNT,
    )
    await state.set_state(SetReport.choosing_our_cash2)


@router.message(SetReport.choosing_our_cash2)
async def sell_choosing_our_credit3(message: Message, state: FSMContext):
    await state.update_data(dealer_discount=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_TORG,
    )
    await state.set_state(SetReport.choosing_our_cash3)


@router.message(SetReport.choosing_our_cash3)
async def sell_choosing_our_credit4(message: Message, state: FSMContext):
    await state.update_data(howmuchtorg=message.text.lower())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH + "\nНажмите кнопку и введите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_cash45)


@router.message(SetReport.choosing_our_cash45)
@router.inline_query(lambda query: query.query.startswith("find_colleges "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    results = []

    query = inline_query.query
    query = query.replace("find_colleges ", "").strip()

    for college in utils.connectors.dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_our_cash5)


@router.message(SetReport.choosing_our_cash5)
async def sell_choosing_our_credit5(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsell=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажмите, чтобы ввести фамилию",
        switch_inline_query_current_chat='find_colleges_dkp ')
    )
    await message.answer(
        text=texts.MESSAGE_SELL_WITH_DKP + "\nНажмите кнопку и введите первые символы фамилии коллеги",
        reply_markup=builder.as_markup()
    )
    await state.set_state(SetReport.choosing_our_cash6)


@router.message(SetReport.choosing_our_cash6)
@router.inline_query(lambda query: query.query.startswith("find_colleges_dkp "))
async def find_colleges(inline_query: types.InlineQuery, state: FSMContext):
    results = []

    query = inline_query.query
    query = query.replace("find_colleges_dkp ", "").strip()

    for college in utils.connectors.dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
    await state.set_state(SetReport.choosing_our_cash7)


@router.message(SetReport.choosing_our_cash7)
async def sell_choosing_our_credit7(message: Message, state: FSMContext):
    await message.answer(text="Пожалуйста подождите, идет проверка имени в базе данных")
    college_name = utils.connectors.db_sql_buy_with_college(message.text.lower())
    await state.update_data(howsellcredit=college_name)
    if college_name == "Некорректный USERNAME":
        await message.answer("Некорректный USERNAME, укажите корректный в режиме редактирования")
    data = await state.get_data()
    print(data)
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['howsell']}\nКТО ПИСАЛ ДКП?: {data['howsellcredit']}\n\n{message.chat.first_name + " " + message.chat.last_name}
        '''
    await message.answer(text=text)
    await message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_our_credit4)
async def sell_choosing_comissiya_credit_cash_comission(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(SetReport.choosing_comissiya_credit2)


@router.callback_query(SetReport.choosing_buyer4)
# @router.message(SetReport.choosing_buyer4)
async def any_message(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer5=callback.message.text.lower())
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.set_state(SetReport.choosing_buyer5)


@router.message(SetReport.choosing_buyer5)
# @router.callback_query(SetReport.choosing_buyer5)
async def any_message(message: Message, state: FSMContext):
    await state.update_data(choosing_buyer6=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_DISCOUNT,
    )
    await state.set_state(SetReport.choosing_buyer7)


@router.message(SetReport.choosing_buyer7)
# @router.callback_query(SetReport.choosing_buyer5)
async def any_message(message: Message, state: FSMContext):
    await state.update_data(choosing_buyer7=message.text.lower())
    await message.answer(
        text=texts.MESSAGE_SELL_SUM_NM,
    )
    await state.set_state(SetReport.choosing_buyer13)


@router.callback_query(SetReport.choosing_buyer7)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer8=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_SUM_SOBS_OSTAV,
        callback_data=texts.BT_SUM_SOBS_OSTAV)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_SUM_SOBS_EDIT,
        callback_data="bt_sum_sobs_edit")
    )
    await callback.message.edit_text(text=texts.MESSAGE_SUM_SOBS, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer8)


@router.callback_query(SetReport.choosing_buyer8, F.data == texts.BT_SUM_SOBS_EDIT)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer9=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_EDIT_NEW_SUM, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer7)


@router.callback_query(SetReport.choosing_buyer8, F.data == texts.BT_SUM_SOBS_OSTAV)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer9=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_SELL_TORG, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer9)


@router.callback_query(SetReport.choosing_buyer9)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer10=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_SELL_WITH, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer10)


@router.callback_query(SetReport.choosing_buyer10)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer11=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_SELL_WITH_CREDIT, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer11)


@router.callback_query(SetReport.choosing_buyer11)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer12=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_YES,
        callback_data=texts.BT_YES)
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NO,
        callback_data=texts.BT_NO)
    )
    await callback.message.edit_text(text=texts.MESSAGE_CAll_SOBS, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer12)


@router.callback_query(SetReport.choosing_buyer12)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(choosing_buyer13=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_DATE_RASCHET, reply_markup=builder.as_markup())
    await state.set_state(SetReport.choosing_buyer13)


@router.message(SetReport.choosing_buyer13)
async def constructor_choosing_awa_our_credit22(message: Message, state: FSMContext):
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
    text = f'''Спасибо, данные ниже ушли в базу:\nТИП ОТЧЕТА: {data['choosing_buyer1']}\nКОМИССИЯ ИЛИ НАША: {data['choosing_buyer4']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['choosing_buyer5']}\nЦЕНА ДРОМ: {data['choosing_buyer6']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['choosing_buyer7']}\nСУММА НМ: {texts.MESSAGE_ZAGLUSHKA}\n\nНА СКОЛЬКО СТОРГОВАЛ: {texts.MESSAGE_ZAGLUSHKA}\n\nС КЕМ ПРОДАЛ?: {texts.MESSAGE_ZAGLUSHKA}\n\nКТО ОФОРМИЛ КРЕДИТ/ПИСАЛ ДКП?: {texts.MESSAGE_ZAGLUSHKA}\n\nСУММА СОБСТВЕННИКУ: {texts.MESSAGE_ZAGLUSHKA}\n\nСОЗВОНИЛСЯ С ВЛАДЕЛЬЦЕМ?: {texts.MESSAGE_ZAGLUSHKA}\n\nДАТА РАСЧЕТА?: {texts.MESSAGE_ZAGLUSHKA}\n\n@{message.chat.username}
        '''
    for i in data:
        print(i, "==", data[i])
    await message.answer(
        text=text,
    )
    await message.answer(
        text="Сохранить?",
        reply_markup=builder.as_markup()
    )
    # Устанавливаем пользователю состояние "выбирает марку и модель"
    await state.set_state(SetReport.choosing_buyer14)


@router.callback_query(SetReport.choosing_buyer14, F.data == texts.BT_SAVE)
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()


@router.callback_query(SetReport.choosing_buyer14, F.data == texts.BT_EDIT)
async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Отчет отправлен, спасибо, что воспользовались ботом. Нажмите на /start для составления нового отчета.")
    await callback.message.answer(text="/start")
    await state.clear()
