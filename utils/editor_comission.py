import re

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from texts import texts
import utils.editor_changer


async def editor_start(callback: types.CallbackQuery, state: FSMContext, dict_editor: dict = None):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][0],
        callback_data=dict_editor['editor_start']['data'][0]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][1],
        callback_data=dict_editor['editor_start']['data'][1]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][2],
        callback_data=dict_editor['editor_start']['data'][2]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][3],
        callback_data=dict_editor['editor_start']['data'][3]
    ))
    builder.row(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][4],
        callback_data=dict_editor['editor_start']['data'][4]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][5],
        callback_data=dict_editor['editor_start']['data'][5]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][6],
        callback_data=dict_editor['editor_start']['data'][6]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][7],
        callback_data=dict_editor['editor_start']['data'][7]
    ))
    builder.row(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][8],
        callback_data=dict_editor['editor_start']['data'][8]
    ))
    builder.row(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][9],
        callback_data=dict_editor['editor_start']['data'][9]
    ))
    builder.row(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][10],
        callback_data=dict_editor['editor_start']['data'][10]
    ))
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТип отчета: {data['chosen_type']}\nГде принял на комиссию: {data['chosen_place']}\nФИО Коллеги: {data['chosen_college_fio']}\nКто писал АГ: {data['chosen_college_dkps']}\nСколько собственнику: {data['howmuchsobs']}\nРазмер комиссии: {data['howmuchcomissiob']}\n\nВид расчета: {data['typeraschet']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарии: {data['chosen_comment']}\n\nИнициатор: {callback.message.chat.first_name + " " + callback.message.chat.last_name}
        '''

    await callback.message.answer(
        text=text,
    )
    await callback.message.answer(
        text="Какое поле хотите изменить?",
        reply_markup=builder.as_markup()
    )


async def editor_start_vin(callback: types.CallbackQuery, state: FSMContext, dict_editor: dict = None):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][0],
        callback_data=dict_editor['editor_start']['data'][0]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][1],
        callback_data=dict_editor['editor_start']['data'][1]
    ))
    builder.row(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][2],
        callback_data=dict_editor['editor_start']['data'][2]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][3],
        callback_data=dict_editor['editor_start']['data'][3]
    ))
    builder.row(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][4],
        callback_data=dict_editor['editor_start']['data'][4]
    ))
    builder.add(types.InlineKeyboardButton(
        text=dict_editor['editor_start']['text'][5],
        callback_data=dict_editor['editor_start']['data'][5]
    ))

    data = await state.get_data()
    text = f'''Предварительный отчет:
    Год: {str(data['chosen_vin_year']).upper()}    
    Гос номер: {str(data['chosen_vin_gos_number']).upper()}
    VIN: {str(data['chosen_vin_number']).upper()}
    Марка: {data['chosen_vin_marka'].upper()}
    Модель: {data['chosen_vin_model'].upper()}'''

    await callback.message.answer(
        text=text,
    )
    await callback.message.answer(
        text="Какое поле хотите изменить?",
        reply_markup=builder.as_markup()
    )


async def editor_first(callback: types.CallbackQuery, state: FSMContext):
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

    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_place'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Ввести фамилию",
        switch_inline_query_current_chat='find_aaaa ')
    )
    await callback.message.answer(text=msg2, reply_markup=builder.as_markup())


async def editor_who_sell_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_college_fio=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_college_fio'], reply_markup=builder.as_markup())


async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_college_dkps'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_who_credit_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_college_dkps=message.text)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    print("editor" + data['chosen_college_dkps'])
    await message.answer(text="Замена на " + data['chosen_college_dkps'], reply_markup=builder.as_markup())


async def editor_first_place(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_place=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    await callback.message.answer(text="Замена на " + callback.data, reply_markup=builder.as_markup())


# async def editor_first_howmuchsobs(callback: types.CallbackQuery, state: FSMContext):
#     await utils.editor_changer.getter(callback, state, chosen_data="howmuchsobs")
#
#
# async def editor_first_cost(message: Message, state: FSMContext):
#     await utils.editor_changer.setter(message, state, chosen_data="howmuchsobs")

async def editor_first_howmuchsobs(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + str(data['howmuchsobs']) + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_first_cost(message: Message, state: FSMContext):
    from handlers.comissionpath import SetReport
    just = message.text.upper()
    if just.isdigit():
        await state.update_data(howmuchsobs=int(just))
        builder = InlineKeyboardBuilder()
        builder.add(types.InlineKeyboardButton(
            text="ОК",
            callback_data=texts.BT_CONSTRUCTOR_2_ATP)
        )
        data = await state.get_data()
        await message.answer(text="Замена на " + str(data['howmuchsobs']), reply_markup=builder.as_markup())
        await state.set_state(SetReport.choosing_comission_editor_start)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        # await editor_first_cost(message, state)


async def editor_first_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_changer.getter(callback, state, chosen_data="chosen_vin_gos_number")


async def editor_first_vin_gos_number(message: Message, state: FSMContext):
    await utils.editor_changer.setter(message, state, chosen_data="chosen_vin_gos_number")


async def editor_first_marka(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_changer.getter(callback, state, chosen_data="chosen_vin_marka")


async def editor_first_vin_marka(message: Message, state: FSMContext):
    await utils.editor_changer.setter(message, state, chosen_data="chosen_vin_marka")


async def editor_first_model(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_changer.getter(callback, state, chosen_data="chosen_vin_model")


async def editor_first_vin_model(message: Message, state: FSMContext):
    await utils.editor_changer.setter(message, state, chosen_data="chosen_vin_model")


async def editor_first_year(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + str(data['chosen_vin_year']) + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_first_vin_year(message: Message, state: FSMContext):
    from handlers.comissionpath import SetReport
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
        await state.set_state(SetReport.choosing_comission_editor_start)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(text="Укажите год")


async def editor_first_vin_year_editor(message: Message, state: FSMContext):
    from handlers.comissionpath import SetReport
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
        current_state = await state.get_state()
        print(current_state)
        await state.set_state(SetReport.choosing_vin_editor_start)
        new_state = await state.get_state()
        print(new_state)
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        await message.answer(text="Укажите год")


async def editor_first_menu_vin(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_changer.getter(callback, state, chosen_data="chosen_vin_number")


async def editor_first_vin_number(message: Message, state: FSMContext):
    await utils.editor_changer.setter(message, state, chosen_data="chosen_vin_number")


async def editor_first_menu_comment(callback: types.CallbackQuery, state: FSMContext):
    await utils.editor_changer.getter(callback, state, chosen_data="chosen_comment")


async def editor_first_comment(message: Message, state: FSMContext):
    await utils.editor_changer.setter(message, state, chosen_data="chosen_comment")
