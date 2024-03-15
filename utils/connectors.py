import datetime
import json
import logging
import re

import psycopg2
import os
from aiogram import types
from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hlink

htext = hlink('Техподдержкой', 'https://t.me/paitssupport')
base_master = "bot_planeta_avto"
base_test = "bot_planeta_avto_test"
database_schema = base_master


def get_data_from_template():
    dict_colleges = []
    with open('templates/dict_collegues.txt', 'r', encoding='utf-8') as f:
        try:
            dict_colleges = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Ошибка при разборе JSON get: {e}")

    return dict_colleges


def set_data_from_template(dict_for_update):
    dict_colleges = get_data_from_template()
    if dict_for_update not in dict_colleges:
        dict_colleges.append(dict_for_update)
        with open('templates/dict_collegues.txt', 'w') as f:
            try:
                json.dump(dict_colleges, f)
            except json.JSONDecodeError as e:
                print(f"Ошибка при разборе JSON set: {e}")
    else:
        print("Добавили в словарь: ")
        print(dict_for_update)
        print(dict_colleges)


def set_data_from_template_backup(dict_for_update):
    dict_colleges = get_data_from_template()
    if dict_for_update not in dict_colleges:
        dict_colleges.append(dict_for_update)
        with open('templates/dict_collegues_backup.txt', 'w') as f:
            try:
                json.dump(dict_colleges, f)
            except json.JSONDecodeError as e:
                print(f"Ошибка при разборе JSON set: {e}")
    else:
        print("Добавили в словарь бэкап: ")
        print(dict_for_update)


async def db_sql_start(username, firstname, lastname, bot: Bot, message=None, callback=None):
    conn = None
    try:
        conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                                password=os.getenv('SQL_PASSWORD'),
                                host=os.getenv('SQL_HOST'),
                                port=os.getenv('SQL_PORT'),
                                database=os.getenv('SQL_DATABASE')
                                )

    except Exception as e:
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        await bot.send_message(os.getenv('ERROR_CHAT_ID'),
                               "DATABASE DOWN " + firstname + " " + lastname)
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                parse_mode="HTML",
                reply_markup=builder2.as_markup())
        elif callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                parse_mode="HTML",
                reply_markup=builder2.as_markup())
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_count_tg_user_info = "select count(*) from {database_schema}.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
            print(sql_count_tg_user_info)
            cur.execute(sql_count_tg_user_info.format(value_teg_name_tg=username, database_schema=database_schema))
            count_tg_user_info = cur.fetchall()
            print(count_tg_user_info[0][0])

            if count_tg_user_info[0][0] == 0:
                sql_insert_tg_info_user = 'INSERT INTO {database_schema}.tg_info_user(teg_name_tg, user_name_tg) VALUES (%s,%s)'
                print(sql_insert_tg_info_user)
                cur.execute(sql_insert_tg_info_user.format(database_schema=database_schema), (username, firstname + " " + lastname,))
                set_data_from_template({"name": firstname + " " + lastname, "tag": username})
                set_data_from_template_backup({"name": firstname + " " + lastname, "tag": username})
                logging.info("Success first login for " + firstname + " " + lastname + " " + username)
                await bot.send_message(os.getenv('ERROR_CHAT_ID'),
                                       "Success FIRST login for " + firstname + " " + lastname)

        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_buy_with_college(username, message):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_count_tg_user_info = "select count(*) from {database_schema}.tg_info_user where user_name_tg='{value_user_name_tg}';"
            print(sql_count_tg_user_info)
            cur.execute(sql_count_tg_user_info.format(value_user_name_tg=username, database_schema=database_schema))
            count_tg_user_info = cur.fetchall()
            print(count_tg_user_info[0][0])
            if count_tg_user_info[0][0] != 0:
                sql_select_tg_user_info = "select user_name_tg from {database_schema}.tg_info_user where user_name_tg='{value_user_name_tg}';"
                print(sql_select_tg_user_info)
                cur.execute(sql_select_tg_user_info.format(value_user_name_tg=username, database_schema=database_schema))
                select_tg_user_info = cur.fetchall()

                return select_tg_user_info[0][0]
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                parse_mode="HTML",
                reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        await message.answer(
            text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_buy_insert(callback=types.CallbackQuery, dict_report=None):
    if dict_report is None:
        dict_report = {}
    data = dict_report

    print(data)
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_insert_tg_info_user = 'INSERT INTO {database_schema}.purchase_report(type_purchase_report, platform,username_purchase_сolleagues,write_dkp,price,tires,vin,gos_number,brand,model,years,comment_report,username_purchase_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            print(sql_insert_tg_info_user)
            cur.execute(sql_insert_tg_info_user.format(database_schema=database_schema), (
                data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_fio_dkp'],
                data['chosen_cost'], data['chosen_wire_boolean'], data['chosen_vin_number'],
                data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'],
                data['chosen_vin_year'],
                data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
            logging.info(
                "Success insert buy for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                parse_mode="HTML",
                reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_sell_insert(callback=types.CallbackQuery, dict_report=None):
    if dict_report is None:
        dict_report = {}
    data = dict_report
    print(data)
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_insert_tg_info_user = 'INSERT INTO {database_schema}.sell_report(type_sell_report,type_credit_our,type_deal,drom_cost,dealer_discount,summa_sob,howmuchtorg,whosell,whosellcredit,date_raschet,type_of_calс,vin,gos_number,brand,model,years,comment_report,username_sell_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            print(sql_insert_tg_info_user)
            cur.execute(sql_insert_tg_info_user.format(database_schema=database_schema), (
                data['chosen_type'], data['type_credit_our'], data['type_deal'], data['drom_cost'],
                data['dealer_discount'], data['summa_sob'], data['howmuchtorg'], data['whosell'],
                data['whosellcredit'], data['date_raschet'], data['type_raschet'], data['chosen_vin_number'],
                data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'],
                data['chosen_vin_year'],
                data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
            logging.info(
                "Success insert sell for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                parse_mode="HTML",
                reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_comission_insert(callback=types.CallbackQuery, dict_report=None):
    if dict_report is None:
        dict_report = {}
    data = dict_report
    print(data)
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_insert_comission_report = 'INSERT INTO {database_schema}.commission_report(type_purchase_report, platform, username_commission_сolleagues, write_ag,price_owner, size_commission, vin, gos_number, brand, model, years, comment_report, username_commission_report, type_of_calс) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            print(sql_insert_comission_report)
            cur.execute(sql_insert_comission_report.format(database_schem=database_schema), (
                data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'],
                data['howmuchsobs'], data['howmuchcomissiob'],
                data['chosen_vin_number'],
                data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'],
                data['chosen_vin_year'],
                data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,
                data['typeraschet']))
            logging.info(
                "Success insert comission for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                parse_mode="HTML",
                reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML")
    conn.commit()
    conn.close()


async def db_sql_price_owner_select(vin_dict, message=None, callback=None):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()

    if conn.closed == 0:
        try:
            print(vin_dict)
            sql_select_vin_commission_report = "select price_owner from {database_schema}.commission_report where vin='{value_vin_tg}';"
            print(sql_select_vin_commission_report)
            cur.execute(sql_select_vin_commission_report.format(value_vin_tg=vin_dict, database_schema=database_schema))
            select_price_owner = cur.fetchall()
            try:
                price_owner = select_price_owner[0][0]
                print(price_owner)
                logging.info(
                    "Success select priceowner for ")
                return str(price_owner)
            except Exception as e:
                print("An error has occurred:", e)
                return "UNKNOWN"
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_vin_buy_owner_select(vin_dict, message=None, callback=None):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_select_vin_all = "select vin from {database_schema}.purchase_report pr \
                                        where pr.vin='{value_vin_tg}' \
                                        ;"
            print(sql_select_vin_all)
            cur.execute(sql_select_vin_all.format(value_vin_tg=vin_dict, database_schema=database_schema))
            select_vin_all = cur.fetchall()
            print("select_vin_all=  " + str(select_vin_all))
            try:
                select_vin = select_vin_all[0][0]
                print(select_vin)
                logging.info(
                    "Success select select_vin for ")
                return str(select_vin)
            except Exception as e:
                print("An error has occurred:", e)
                return "UNKNOWN"
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения<pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

    conn.commit()
    conn.close()


async def db_sql_vin_comission_owner_select(vin_dict, message=None, callback=None):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            sql_select_vin_all = "select vin from {database_schema}.commission_report cr where cr.vin='{value_vin_tg}';"
            print(sql_select_vin_all)
            cur.execute(sql_select_vin_all.format(value_vin_tg=vin_dict, database_schema=database_schema))
            select_vin_all = cur.fetchall()
            print("select_vin_all=  " + str(select_vin_all))
            try:
                select_vin = select_vin_all[0][0]
                print(select_vin)
                logging.info(
                    "Success select select_vin for ")
                return str(select_vin)
            except Exception as e:
                print("An error has occurred:", e)
                return "UNKNOWN"
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_type_of_calc_select(vin_dict, message=None, callback=None):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            print(f'Успешное подключение к бд, статус {conn.closed}')
            print(vin_dict)
            sql_select_type_of_calс_commission_report = "select type_of_calс from {database_schema}.commission_report where vin='{value_vin_tg}';"
            print(sql_select_type_of_calс_commission_report)
            cur.execute(sql_select_type_of_calс_commission_report.format(value_vin_tg=vin_dict, database_schema=database_schema))
            select_type_of_calс = cur.fetchall()
            try:
                type_of_calс = select_type_of_calс[0][0]
                print(type_of_calс)
                logging.info(
                    "Success select type_of_calc for ")
                return str(type_of_calс)
            except Exception as e:
                print("An error has occurred:", e)
                return "UNKNOWN"
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_buy_editor_select(vin_dict, message=None, callback=None):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            print(f'Успешное подключение к бд, статус {conn.closed}')
            print(vin_dict)
            sql_select_buy_editor_report = "select * from {database_schema}.purchase_report where vin='{value_vin_tg}';"
            print(sql_select_buy_editor_report)
            cur.execute(sql_select_buy_editor_report.format(value_vin_tg=vin_dict, database_schema=database_schema))
            select_buy_editor = cur.fetchall()
            try:
                buy_editor = select_buy_editor[0]
                print(buy_editor)
                logging.info(
                    "Success select buy_editor_buy for ")
                return buy_editor
            except Exception as e:
                print("An error has occurred:", e)
                # await callback.message.answer(
                #     text="Вин номер не найдет, проверьте его корректность")
                return "UNKNOWN"
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения; <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def db_sql_comission_editor_select(vin_dict, message=None, callback=None):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        try:
            print(f'Успешное подключение к бд, статус {conn.closed}')
            print(vin_dict)
            sql_select_comission_editor_report = "select * from {database_schema}.commission_report where vin='{value_vin_tg}';"
            print(sql_select_comission_editor_report)
            cur.execute(sql_select_comission_editor_report.format(value_vin_tg=vin_dict, database_schema=database_schema))
            select_comission_editor = cur.fetchall()
            try:
                comission_editor = select_comission_editor[0]
                print(comission_editor)
                logging.info(
                    "Success select buy_editor_buy for ")
                return comission_editor
            except Exception as e:
                print("An error has occurred:", e)
                # await callback.message.answer(
                #     text="Вин номер не найдет, проверьте его корректность")
                return "UNKNOWN"
        except Exception as e:
            builder2 = InlineKeyboardBuilder()
            builder2.add(types.InlineKeyboardButton(
                text="Начать заново",
                callback_data="start_from_critical")
            )
            print(f'База недоступна, статус {conn.closed}')
            if message is not None:
                await message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
            if callback is not None:
                await callback.message.answer(
                    text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения: <pre><code>{str(e)[:200]}</code></pre>",
                    parse_mode="HTML",
                    reply_markup=builder2.as_markup())
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        builder2 = InlineKeyboardBuilder()
        builder2.add(types.InlineKeyboardButton(
            text="Начать заново",
            callback_data="start_from_critical")
        )
        print(f'База недоступна, статус {conn.closed}')
        if message is not None:
            await message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())

        if callback is not None:
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML", reply_markup=builder2.as_markup())
    conn.commit()
    conn.close()


async def date_normalizer(date_from_user):
    try:
        date_normal = datetime.datetime.strptime(date_from_user, "%d.%m.%Y").date().isoformat()
        return date_normal
    except Exception as e:
        print(e)
        return False
