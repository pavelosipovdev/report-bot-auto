import re

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts import texts


async def editor_start_1_6(callback: types.CallbackQuery, state: FSMContext, dict_editor: dict = None):
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
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nСУММА НМ: {data['summa_nm']}\nСУММА СОБСТВЕННИКУ: ZAGLUSHKA\nСУММА СТОРГОВАЛ: {data['howmuchtorg']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['whosellcredit']}\nДАТА: {data['date_raschet']}\nВИД РАСЧЕТА: {data['type_raschet']}\n\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''

    await callback.message.answer(
        text=text,
    )
    await callback.message.answer(
        text="Какое поле хотите изменить?",
        reply_markup=builder.as_markup()
    )

async def editor_start_7_8(callback: types.CallbackQuery, state: FSMContext, dict_editor: dict = None):
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
    data = await state.get_data()
    text = f'''Предварительный отчет:\nТИП ОТЧЕТА: {data['chosen_type']}\nКОМИССИЯ ИЛИ НАША: {data['type_credit_our']}\nКРЕДИТ ИЛИ НАЛИЧНЫЕ?: {data['type_deal']}\nЦЕНА ДРОМ: {data['drom_cost']}\nМЕНЕДЖЕРСКАЯ СКИДКА: {data['dealer_discount']}\nС КЕМ ПРОДАЛ: {data['whosell']}\nКТО ОФОРМИЛ КРЕДИТ?: {data['whosellcredit']}\nVIN: {data['chosen_vin_number']}\nГос номер: {data['chosen_vin_gos_number']}\nМарка: {data['chosen_vin_marka']}\nМодель: {data['chosen_vin_model']}\nГод: {data['chosen_vin_year']}\nКомментарий: {data['chosen_comment']}\n\n\n{callback.message.chat.first_name + " " + callback.message.chat.last_name}
            '''

    await callback.message.answer(
        text=text,
    )
    await callback.message.answer(
        text="Какое поле хотите изменить?",
        reply_markup=builder.as_markup()
    )


async def editor_first_place(callback: types.CallbackQuery, state: FSMContext):
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


async def editor_first_place_edit(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(chosen_place=callback.data)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    await callback.message.answer(text="Замена на " + callback.data, reply_markup=builder.as_markup())


async def editor_drom_cost(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + str(data['drom_cost']) + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_drom_cost_edit(message: Message, state: FSMContext):
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
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        # await editor_drom_cost_edit(message, state)

    # just = message.text.upper()
    # await state.update_data(drom_cost=int(re.sub("[^0-9]", "", just)))
    # builder = InlineKeyboardBuilder()
    # builder.add(types.InlineKeyboardButton(
    #     text="ОК",
    #     callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    # )
    # data = await state.get_data()
    # await message.answer(text="Замена на " + data['drom_cost'], reply_markup=builder.as_markup())


async def editor_who_sell(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosell'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_who_sell_edit(message: Message, state: FSMContext):
    await state.update_data(whosell=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['whosell'], reply_markup=builder.as_markup())


async def editor_who_credit(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['whosellcredit'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_who_credit_edit(message: Message, state: FSMContext):
    await state.update_data(whosellcredit=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['whosellcredit'], reply_markup=builder.as_markup())


async def editor_gosnumber(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_gos_number'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_gosnumber_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_gos_number=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_gos_number'], reply_markup=builder.as_markup())


async def editor_marka(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_marka'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_marka_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_marka=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_marka'], reply_markup=builder.as_markup())


async def editor_model(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_model'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_model_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_model=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_model'], reply_markup=builder.as_markup())


async def editor_year(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + str(data['chosen_vin_year']) + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_year_edit(message: Message, state: FSMContext):
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
    else:
        await message.answer(
            text=texts.MESSAGE_ONLY_DIGITS,
        )
        # await editor_year_edit(message, state)



async def editor_vin(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_vin_number'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_vin_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_vin_number=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_vin_number'], reply_markup=builder.as_markup())


async def editor_comment(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg2 = "В данный момент используется " + data['chosen_comment'] + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)


async def editor_comment_edit(message: Message, state: FSMContext):
    await state.update_data(chosen_comment=message.text.upper())
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data['chosen_comment'], reply_markup=builder.as_markup())
