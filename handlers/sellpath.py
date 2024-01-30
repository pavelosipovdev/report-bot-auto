from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import convert, api
from texts import texts

router = Router()

import re

template_fio = 'ФИО: (.*)'
template_marka = 'Марка: (.*)'
template_model = 'Модель: (.*)'
template_year = 'Год: (.*)'
template_our = 'Наша/комиссия: (.*)'
template_cost = 'Цена продажи: (.*)'
template_drom = 'Сколько накинул на цену дрома: (.*)'
template_own = 'Сколько собственнику: (.*)'
# template_torg = 'До скольки сторговали собственника: (.*)'
template_torg = 'До скольки сторговали собственника: (.*)'
template_fio2 = 'С кем продал ФИО: (.*)'
template_dkpfio = 'ДКП ФИО: (.*)'
template_commi = 'Кто ставил на комиссию: (.*)'
template_agent = 'Кто писал агентский договор: (.*)'


# sender_fio = ["UNKNOWN"]
# sender_marka = ["UNKNOWN"]
# sender_model = ["UNKNOWN"]
# sender_year = ["UNKNOWN"]
# sender_our = ["UNKNOWN"]
# sender_cost = ["UNKNOWN"]
# sender_drom = ["UNKNOWN"]
# sender_own = ["UNKNOWN"]
# sender_torg = ["UNKNOWN"]
# sender_fio2 = ["UNKNOWN"]
# sender_dkpfio = ["UNKNOWN"]
# sender_commi = ["UNKNOWN"]
# sender_agent = ["UNKNOWN"]

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
    # choosing_download1 = State()
    # choosing_download11 = State()
    # choosing_vin1 = State()
    # choosing_electro1 = State()
    # choosing_college1 = State()
    # choosing_dkp1 = State()
    # choosing_cost1 = State()
    # choosing_wire1 = State()
    # choosing_wire121 = State()
    # choosing_wire441 = State()
    # choosing_wire21 = State()
    # choosing_japan1 = State()
    # choosing_report1 = State()


@router.callback_query(F.data == texts.BT_CONSTRUCTOR_1_SELL)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
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
    await state.update_data(choosing_buyer1=callback.data)
    await state.set_state(SetReport.choosing_buyer1)
    await callback.message.delete()


@router.callback_query(SetReport.choosing_buyer1, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_PHOTO_VIN_DOWNLOAD_PLZ, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer2=callback.data)
    await state.set_state(SetReport.choosing_buyer2)
    # 


@router.callback_query(SetReport.choosing_buyer1, F.data == texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_PHOTO_VIN_DOWNLOAD_PLZ, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer2=callback.data)
    await state.set_state(SetReport.choosing_buyer2)
    # 


@router.callback_query(SetReport.choosing_buyer2)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
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
    await state.update_data(choosing_buyer3=callback.data)
    await state.set_state(SetReport.choosing_buyer3)
    # 


@router.callback_query(SetReport.choosing_buyer3, F.data == texts.BT_COMISSION)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
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
    await state.update_data(choosing_buyer4=callback.data)
    await state.set_state(SetReport.choosing_buyer4)
    # 


@router.callback_query(SetReport.choosing_buyer3, F.data == texts.BT_OUR)
async def main_menu_bt_constructor_12_sell(callback: types.CallbackQuery, state: FSMContext):
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
    await state.update_data(choosing_buyer4=callback.data)
    await state.set_state(SetReport.choosing_buyer4)
    # 


@router.callback_query(SetReport.choosing_buyer4)
# @router.message(SetReport.choosing_buyer4)
async def any_message(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text=texts.MESSAGE_SELL_COST_DROM,
    )
    await state.update_data(choosing_buyer5=callback.message.text.lower())
    await state.set_state(SetReport.choosing_buyer5)


@router.message(SetReport.choosing_buyer5)
# @router.callback_query(SetReport.choosing_buyer5)
async def any_message(message: Message, state: FSMContext):
    await message.answer(
        text=texts.MESSAGE_SELL_DISCOUNT,
    )
    await state.update_data(choosing_buyer6=message.text.lower())
    await state.set_state(SetReport.choosing_buyer7)


@router.message(SetReport.choosing_buyer7)
# @router.callback_query(SetReport.choosing_buyer5)
async def any_message(message: Message, state: FSMContext):
    await message.answer(
        text=texts.MESSAGE_SELL_SUM_NM,
    )
    await state.update_data(choosing_buyer7=message.text.lower())
    await state.set_state(SetReport.choosing_buyer13)


# @router.callback_query(SetReport.choosing_buyer4, F.data == texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT)
# # @router.callback_query(lambda call: call.data == texts.MESSAGE_SELL_DISCOUNT)
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_NEXT,
#         callback_data=texts.BT_NEXT)
#     )
#     await callback.message.edit_text(text=texts.MESSAGE_SELL_COST_DROM, reply_markup=builder.as_markup())
#     await state.update_data(choosing_buyer5=callback.data)
#     await state.set_state(SetReport.choosing_buyer5)

#
# @router.callback_query(SetReport.choosing_buyer5)
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_NEXT,
#         callback_data=texts.BT_NEXT)
#     )
#     await callback.message.edit_text(text=texts.MESSAGE_SELL_DISCOUNT, reply_markup=builder.as_markup())
#     await state.update_data(choosing_buyer6=callback.data)
#     await state.set_state(SetReport.choosing_buyer13)

#
# @router.callback_query(SetReport.choosing_buyer6)
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_NEXT,
#         callback_data=texts.BT_NEXT)
#     )
#     await callback.message.edit_text(text=texts.MESSAGE_SELL_SUM_NM, reply_markup=builder.as_markup())
#     await state.update_data(choosing_buyer7=callback.data)
#     await state.set_state(SetReport.choosing_buyer7)
#

@router.callback_query(SetReport.choosing_buyer7)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
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
    await state.update_data(choosing_buyer8=callback.data)
    await state.set_state(SetReport.choosing_buyer8)


@router.callback_query(SetReport.choosing_buyer8, F.data == texts.BT_SUM_SOBS_EDIT)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_EDIT_NEW_SUM, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer9=callback.data)
    await state.set_state(SetReport.choosing_buyer7)


@router.callback_query(SetReport.choosing_buyer8, F.data == texts.BT_SUM_SOBS_OSTAV)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_SELL_TORG, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer9=callback.data)
    await state.set_state(SetReport.choosing_buyer9)


@router.callback_query(SetReport.choosing_buyer9)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_SELL_WITH, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer10=callback.data)
    await state.set_state(SetReport.choosing_buyer10)


@router.callback_query(SetReport.choosing_buyer10)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_SELL_WITH_CREDIT, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer11=callback.data)
    await state.set_state(SetReport.choosing_buyer11)


@router.callback_query(SetReport.choosing_buyer11)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
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
    await state.update_data(choosing_buyer12=callback.data)
    await state.set_state(SetReport.choosing_buyer12)


@router.callback_query(SetReport.choosing_buyer12)
async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_NEXT,
        callback_data=texts.BT_NEXT)
    )
    await callback.message.edit_text(text=texts.MESSAGE_DATE_RASCHET, reply_markup=builder.as_markup())
    await state.update_data(choosing_buyer13=callback.data)
    await state.set_state(SetReport.choosing_buyer13)


# @router.callback_query(SetReport.choosing_buyer13)
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_SAVE,
#         callback_data="bt_save")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_EDIT,
#         callback_data="bt_edit")
#     )
#     await callback.message.answer(text=texts.MESSAGE_TYPE_RASCHETA_WAS, reply_markup=builder.as_markup())
#     await state.update_data(choosing_buyer14=callback.data)
#     await state.set_state(SetReport.choosing_buyer14)
#     
#
#
# @router.callback_query(SetReport.choosing_buyer14, F.data == "bt_edit")
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_NEXT,
#         callback_data="bt_constructor_3_download")
#     )
#     await callback.message.answer(text=texts.MESSAGE_TYPE_RASCHETA_EDIT, reply_markup=builder.as_markup())
#     await state.update_data(choosing_buyer14=callback.data)
#     await state.set_state(SetReport.choosing_buyer13)
#     

#
# def transformer(value):
#     if value == "bt_constructor_2_atp":
#         return "АТП",
#     elif value == "bt_constructor_2_abakan":
#         return "АБАКАН",
#     elif value == "bt_constructor_2_planeta":
#         return "ПЛАНЕТА АВТО",
#     elif value == "bt_constructor_2_alien":
#         return "ИНОГОРОДНИЕ",
#     elif value == "bt_constructor_2_getout":
#         return "ВЫЕЗД",
#     elif value == "bt_constructor_1_buy":
#         return "КУПИЛ",
#     elif value == "bt_constructor_1_sell":
#         return "ПРОДАЛ",
#     elif value == "bt_constructor_33_download":
#         return "САМ",
#     elif value == "bt_constructor_33_manual":
#         return "КОЛЛЕГА",
#     elif value == "bt_constructor_4_college_self":
#         return "САМ",
#     elif value == "bt_constructor_4_college_college":
#         return "КОЛЛЕГА",
#     elif value == "bt_constructor_6_wire_yes":
#         return "ЕСТЬ",
#     elif value == "bt_constructor_6_wire_no":
#         return "НЕТ",
#     else:
#         return "-"


# @router.callback_query(SetReport.choosing_buyer14, F.data == "bt_save")
# async def main_menu_bt_constructor_1_sell(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_NEXT,
#         callback_data="bt_constructor_3_download")
#     )
#     await callback.message.answer(text=texts.MESSAGE_TYPE_RASCHETA_EDIT, reply_markup=builder.as_markup())
#     await state.update_data(choosing_buyer14=callback.data)
#     await state.set_state(SetReport.choosing_buyer13)
#     

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
    # print(data['chosen_buyer'])
    # tip_otcheta = str(transformer(data['chosen_buyer']))[2:-3]
    # gde_prodal = str(transformer(data['chosen_download']))[2:-3]
    # odin_ili_s_college = str(transformer(data['chosen_dkp1']))[2:-3]
    # kto_pisal_dkp = str(transformer(data['chosen_cost1']))[2:-3]
    # rezina_est = str(transformer(data['chosen_wire23']))[2:-3]
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
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Начать сначала",
        callback_data="main_menu23232"
    ))
    await callback.message.answer(text="ЗАГЛУШКА, введите /start", reply_markup=builder.as_markup())
    await state.clear()


@router.callback_query(SetReport.choosing_buyer14, F.data == texts.BT_EDIT)
async def constructor_choosing_awa_our_credit424(callback: types.CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Начать сначала",
        callback_data="main_menu23232"
    ))
    await callback.message.answer(text="ЗАГЛУШКА, введите /start", reply_markup=builder.as_markup())
    await state.clear()

# @router.callback_query(SetReport.choosing_buyer1)
# async def constructor_choosing_download(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.MESSAGE_BT_CONSTRUCTOR_3_DOWNLOAD,
#         callback_data="bt_constructor_3_download")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.MESSAGE_BT_CONSTRUCTOR_3_MANUAL,
#         callback_data="bt_constructor_3_manual")
#     )
#     await callback.message.answer(text="Скачать или руками", reply_markup=builder.as_markup())
#     await state.update_data(chosen_download=callback.data)
#     await state.set_state(SetReport.choosing_college1)
#     
#
#
# @router.message(SetReport.choosing_japan1, F.photo)
# async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
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
#     convert.convert_json_vin(f"tmp/{message.photo[-1].file_id}.jpg")
#     msg = api.get_strings_vin()
#     print(msg)
#     doka = []
#     for i in msg:
#         if i["name"] == "stsfront_car_year":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_number":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_vin_number":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_brand":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_model":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_color":
#             doka.append(i["text"])
#
#     print(doka)
#     msg2 = f'''В базу внесено:
#     Год {doka[0]}
#     Гос номер {doka[1]}
#     VIN {str(doka[2]).upper()}
#     Марка {doka[3]}
#     Модель {doka[4]}
#     Цвет {doka[5]}
#     '''
#     await message.answer(text=msg2, reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_college1)
#
#
# @router.callback_query(SetReport.choosing_college1)
# async def constructor_choosing_dkp(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
#         callback_data="bt_constructor_4_college_self")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
#         callback_data="bt_constructor_4_college_self")
#     )
#     await callback.message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_4_COLLEGE, reply_markup=builder.as_markup())
#     await state.update_data(chosen_dkp1=callback.data, chosen_dkp=callback.message.text.upper())
#     await state.set_state(SetReport.choosing_dkp1)
#     
#
#
# @router.callback_query(SetReport.choosing_dkp1)
# async def constructor_choosing_cost(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_4_COLLEGE_SELF,
#         callback_data="bt_constructor_4_college_self")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_4_COLLEGE_COLLEGE,
#         callback_data="bt_constructor_4_college_college")
#     )
#     await callback.message.answer(text="КТО ПИСАЛ ДКП?", reply_markup=builder.as_markup())
#     await state.update_data(chosen_cost1=callback.data, chosen_cost=callback.message.text.upper())
#     await state.set_state(SetReport.choosing_cost1)
#     
#
#
# # @router.message(SetReport.choosing_cost)
# # async def constructor_choosing_wire(message: Message, state: FSMContext):
# #     builder = InlineKeyboardBuilder()
# #     builder.add(types.InlineKeyboardButton(
# #         text="Следующий шаг",
# #         callback_data="bt_constructor_55_college_self")
# #     )
# #     await message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST, reply_markup=builder.as_markup())
# #     await state.update_data(chosen_wire=message.text.upper())
# #     await state.set_state(SetReport.choosing_wire)
#
# @router.callback_query(SetReport.choosing_cost1)
# async def constructor_choosing_wire(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Следующий шаг",
#         callback_data="bt_constructor_55_college_self")
#     )
#     await callback.message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_5_COST, reply_markup=builder.as_markup())
#     await state.update_data(chosen_wire=callback.message.text.upper())
#     await state.set_state(SetReport.choosing_wire1)
#     
#
#
# @router.callback_query(SetReport.choosing_wire1)
# async def constructor_choosing_wire2(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_6_WIRE_YES,
#         callback_data="bt_constructor_6_wire_yes")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_6_WIRE_NO,
#         callback_data="bt_constructor_6_wire_no")
#     )
#     await callback.message.answer(text=texts.MESSAGE_BT_CONSTRUCTOR_6_WIRE, reply_markup=builder.as_markup())
#     await state.set_state(SetReport.choosing_wire121)
#     
#
#
# @router.callback_query(SetReport.choosing_wire121)
# async def constructor_choosing_wire12(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Следующий шаг",
#         callback_data="bt_constructor_56_college_self")
#     )
#     await callback.message.answer(text="Все?", reply_markup=builder.as_markup())
#     await state.update_data(chosen_wire23=callback.data)
#     await state.set_state(SetReport.choosing_wire21)
#     
#
#
# def transformer(value):
#     if value == "bt_constructor_2_atp":
#         return "АТП",
#     elif value == "bt_constructor_2_abakan":
#         return "АБАКАН",
#     elif value == "bt_constructor_2_planeta":
#         return "ПЛАНЕТА АВТО",
#     elif value == "bt_constructor_2_alien":
#         return "ИНОГОРОДНИЕ",
#     elif value == "bt_constructor_2_getout":
#         return "ВЫЕЗД",
#     elif value == "bt_constructor_1_buy":
#         return "КУПИЛ",
#     elif value == "bt_constructor_1_sell":
#         return "ПРОДАЛ",
#     elif value == "bt_constructor_33_download":
#         return "САМ",
#     elif value == "bt_constructor_33_manual":
#         return "КОЛЛЕГА",
#     elif value == "bt_constructor_4_college_self":
#         return "САМ",
#     elif value == "bt_constructor_4_college_college":
#         return "КОЛЛЕГА",
#     elif value == "bt_constructor_6_wire_yes":
#         return "ЕСТЬ",
#     elif value == "bt_constructor_6_wire_no":
#         return "НЕТ",
#     else:
#         return "-"
#
#
# @router.callback_query(SetReport.choosing_wire21)
# async def constructor_choosing_awa_our_credit22(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_7_SAVE,
#         callback_data="bt_constructor_7_save")
#     )
#     builder.add(types.InlineKeyboardButton(
#         text=texts.BT_CONSTRUCTOR_7_EDIT,
#         callback_data="bt_constructor_7_edit")
#     )
#     data = await state.get_data()
#     print(data['chosen_buyer'])
#     tip_otcheta = str(transformer(data['chosen_buyer']))[2:-3]
#     gde_prodal = str(transformer(data['chosen_download']))[2:-3]
#     odin_ili_s_college = str(transformer(data['chosen_dkp1']))[2:-3]
#     kto_pisal_dkp = str(transformer(data['chosen_cost1']))[2:-3]
#     rezina_est = str(transformer(data['chosen_wire23']))[2:-3]
#     text = f'''Спасибо, данные ниже ушли в базу:\nТип отчета: {tip_otcheta}\nГде продал: {gde_prodal}\nОдин или с коллегой: {odin_ili_s_college}\nКто писал дкп: {kto_pisal_dkp}\nЦена: {data['chosen_wire']}\nРезина есть?: {rezina_est}\n\n@{callback.message.chat.username}
#         '''
#     for i in data:
#         print(i)
#     await callback.message.answer(
#         text=text,
#     )
#     await callback.message.answer(
#         text="Сохранить?",
#         reply_markup=builder.as_markup()
#     )
#     # Устанавливаем пользователю состояние "выбирает марку и модель"
#     await state.set_state(SetReport.choosing_wire441)
#
#
# @router.callback_query(SetReport.choosing_wire441, F.data == "bt_constructor_7_save")
# async def constructor_choosing_awa_our_credit44(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Начать сначала",
#         callback_data="main_menu23232"
#     ))
#     await callback.message.answer(text="ЗАГЛУШКА, введите /start", reply_markup=builder.as_markup())
#     await state.clear()
#
#
# @router.callback_query(SetReport.choosing_wire441, F.data == "bt_constructor_7_edit")
# async def constructor_choosing_awa_our_credit424(callback: types.CallbackQuery, state: FSMContext):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Начать сначала",
#         callback_data="main_menu23232"
#     ))
#     await callback.message.answer(text="ЗАГЛУШКА, введите /start", reply_markup=builder.as_markup())
#     await state.clear()
#
#
# @router.message(SetReport.choosing_vin1, F.photo)
# async def constructor_choosing_vin(message: Message, state: FSMContext, bot: Bot):
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
#     convert.convert_json_vin(f"tmp/{message.photo[-1].file_id}.jpg")
#     msg = api.get_strings_vin()
#     print(msg)
#     doka = []
#     for i in msg:
#         if i["name"] == "stsfront_car_year":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_number":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_vin_number":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_brand":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_model":
#             doka.append(i["text"])
#         elif i["name"] == "stsfront_car_color":
#             doka.append(i["text"])
#
#     print(doka)
#     # data_new = f"{msg[]}"
#     msg2 = f'''В базу внесено:
#     Год {doka[0]}
#     Гос номер {doka[1]}
#     VIN {str(doka[2]).upper()}
#     Марка {doka[3]}
#     Модель {doka[4]}
#     Цвет {doka[5]}
#     '''
#     # await message.answer(text=texts.MESSAGE_MAIN_MENU_VIN, reply_markup=builder.as_markup())
#     await message.answer(text=msg2, reply_markup=builder.as_markup())
#     await state.clear()
#
#
# @router.message(SetReport.choosing_japan1, F.photo)
# async def constructor_choosing_japan(message: Message, state: FSMContext, bot: Bot):
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
#     japan_vin = 'UNKNOWN'
#     for i in msg:
#         if i["lines"][0]["words"][0]["text"]:
#             doka.append(i["lines"][0]["words"][0]["text"])
#     # print(doka)
#     for k in doka:
#         if len(k) == 13:
#             japan_vin = str(k).upper()
#
#     msg2 = f'''В базу внесено:
#     VIN {japan_vin}
#     '''
#     # await message.answer(text=texts.MESSAGE_MAIN_MENU_VIN, reply_markup=builder.as_markup())
#     await message.answer(text=msg2, reply_markup=builder.as_markup())
#     await state.clear()
#
#
# @router.message(SetReport.choosing_electro1, F.photo)
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
# @router.message(SetReport.choosing_report1)
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
#
#     # try:
# conn = psycopg2.connect(user=os.environ['SQL_USER'],
#                         password=os.environ['SQL_PASSWORD'],
#                         host=os.environ['SQL_HOST'],
#                         port=os.environ['SQL_PORT'],
#                         database=os.environ['SQL_DATABASE']
#                         )
#     #     cur = conn.cursor()
#     #     print(f'Статус подключение к бд {conn.closed}')
#     #     sql_insert_data_otchet = 'INSERT INTO bot_vitek.wb_otchet_data(city, full_name, route_number, date_otchet, start_otchet, finish_otchet, waybill_number, amount_shk, loader, amount_flight) VALUES (%s,%s, %s,%s,%s, %s, %s, %s,%s,%s)'
#     #     cur.execute(sql_insert_data_otchet, (
#     #         city[0], full_name[0], route_number[0], date_otchet[0], start_otchet[0], finish_otchet[0],
#     #         waybill_number[0],
#     #         amount_shk[0], loader[0], amount_flight[0],))
#     #     conn.commit()
#     #     count = cur.rowcount
#     #     print(count, "Record inserted successfully into mobile table")
#     #     update.message.reply_text('Отчет отправлен!', reply_markup=main_keyboard())
#     #     conn.close()
#     #     await state.set_state(SetReport.choosing_exit)
#     # except (Exception, psycopg2.Error) as error:
#     #     print("Failed to insert record into mobile table", error)
#     #     await state.clear()
#     await state.clear()
#
# # def get_report_excel(update, context):
# #     update.message.reply_text('Ваш отчет:')
# #     try:
# #         conn1 = psycopg2.connect(user='habrpguser',
# #                                  password='pgpwd4habr',
# #                                  host='91.238.99.236',
# #                                  port='5432',
# #                                  database='NEWBASE'
# #                                  )
# #         cur1 = conn1.cursor()
# #         print(f'Статус подключение к бд {conn1.closed}')
# #         cur1.execute(
# #             'SELECT city, full_name, route_number, date_otchet, waybill_number, amount_shk, loader, amount_flight from bot_vitek.wb_otchet_data_2 where date_otchet >= %s and  date_otchet <=%s ',
# #             ('2022-11-12', '2022-11-14',))
# #         # sql = '''select * from bot_vitek.wb_otchet_data;'''
# #         # cur.execute(sql)
# #         results = cur1.fetchall()
# #         print(results)
# #         conn1.close()
# #     except (Exception, psycopg2.Error) as error:
# #         print("Failed to insert record into mobile table", error)
