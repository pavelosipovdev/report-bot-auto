from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts import texts


async def setter(message: Message, state: FSMContext, chosen_data: str):
    await state.update_data(data={chosen_data: message.text.upper()})
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="ОК",
        callback_data=texts.BT_CONSTRUCTOR_2_ATP)
    )
    data = await state.get_data()
    await message.answer(text="Замена на " + data[chosen_data], reply_markup=builder.as_markup())


async def getter(callback: types.CallbackQuery, state: FSMContext, chosen_data: str):
    data = await state.get_data()
    msg2 = "В данный момент используется " + str(data[chosen_data]) + ", на какое значение хотите изменить?"
    await callback.message.answer(text=msg2)
