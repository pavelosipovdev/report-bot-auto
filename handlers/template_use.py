import datetime

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from texts import texts

router = Router()

#
# class UsingTemplate(StatesGroup):
#     choosing_sell = State()
#     choosing_our = State()
#     choosing_comission = State()
#     choosing_comission_rent = State()
#     choosing_comission_cash = State()
#     choosing_our_rent = State()
#     choosing_our_cash = State()


@router.callback_query(F.data == "main_menu")
async def cmd_start_1(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_1_SELL,
        callback_data="bt_constructor_1_sell")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_1_BUY,
        callback_data="bt_constructor_1_buy")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.CB_BUY_BUTTON31,
        callback_data="main_menu_button5")
    )

    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_1_sell")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_COMISSION,
        callback_data="bt_constructor_2_comission")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_2_OUR,
        callback_data="bt_constructor_2_our")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_1_buy")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.MESSAGE_MAIN_MENU, reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_2_comission")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_3_COMISSION_CREDIT_RENT,
        callback_data="bt_constructor_3_comission_credit_rent")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_3_COMISSION_CASH,
        callback_data="bt_constructor_3_comission_cash")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_2_MESSAGE, reply_markup=builder.as_markup())
    await callback.message.delete()


@router.callback_query(F.data == "bt_constructor_2_our")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_3_OUR_CREDIT_RENT,
        callback_data="bt_constructor_3_our_credit_rent")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_3_OUR_CASH,
        callback_data="bt_constructor_3_our_cash")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_2_MESSAGE, reply_markup=builder.as_markup())
    await callback.message.delete()


@router.callback_query(F.data == "bt_constructor_3_comission_credit_rent")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COMISSION_CREDIT_RENT_NEW,
        callback_data="bt_constructor_4_comission_credit_rent_new")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COMISSION_CREDIT_RENT_OLD,
        callback_data="bt_constructor_4_comission_credit_rent_old")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_3_MESSAGE, reply_markup=builder.as_markup())
    await callback.message.delete()


@router.callback_query(F.data == "bt_constructor_3_comission_cash")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COMISSION_CASH_NEW,
        callback_data="bt_constructor_4_comission_cash_new")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_COMISSION_CASH_OLD,
        callback_data="bt_constructor_4_comission_cash_old")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_3_MESSAGE, reply_markup=builder.as_markup())
    await callback.message.delete()


@router.callback_query(F.data == "bt_constructor_3_our_credit_rent")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_OUR_CREDIT_RENT_NEW,
        callback_data="bt_constructor_4_our_credit_rent_new")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_OUR_CREDIT_RENT_OLD,
        callback_data="bt_constructor_4_our_credit_rent_old")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_3_MESSAGE, reply_markup=builder.as_markup())
    await callback.message.delete()


@router.callback_query(F.data == "bt_constructor_3_our_cash")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_OUR_CASH_NEW,
        callback_data="bt_constructor_4_our_cash_new")
    )
    builder.add(types.InlineKeyboardButton(
        text=texts.BT_CONSTRUCTOR_4_OUR_CASH_OLD,
        callback_data="bt_constructor_4_our_cash_old")
    )
    builder.row(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_3_MESSAGE, reply_markup=builder.as_markup())
    await callback.message.delete()


@router.callback_query(F.data == "bt_constructor_4_comission_credit_rent_new")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_COMISSION_CREDIT_RENT_NEW_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_comission_credit_rent_old")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_COMISSION_CREDIT_RENT_OLD_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_comission_cash_new")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_COMISSION_CASH_NEW_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_comission_cash_old")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_COMISSION_CASH_OLD_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_our_credit_rent_new")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_OUR_CREDIT_RENT_NEW_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_our_credit_rent_old")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_OUR_CREDIT_RENT_OLD_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_our_cash_new")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_OUR_CASH_NEW_TEXT,
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "bt_constructor_4_our_cash_old")
async def cmd_start_main(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text=texts.MESSAGE_IN_MAIN_MENU,
        callback_data="main_menu")
    )

    await callback.message.answer(text=texts.CONSTRUCTOR_4_OUR_CASH_OLD_TEXT,
                                  reply_markup=builder.as_markup())
