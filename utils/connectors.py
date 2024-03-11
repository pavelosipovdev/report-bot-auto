import datetime
import json
import logging
import re

import psycopg2
import os
from aiogram import types
from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.markdown import hlink


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


async def db_sql_start(username, firstname, lastname, bot: Bot):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_count_tg_user_info = "select count(*) from bot_planeta_avto.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
        cur.execute(sql_count_tg_user_info.format(value_teg_name_tg=username))
        count_tg_user_info = cur.fetchall()
        print(count_tg_user_info[0][0])

        if count_tg_user_info[0][0] == 0:
            sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.tg_info_user(teg_name_tg, user_name_tg) VALUES (%s,%s)'
            cur.execute(sql_insert_tg_info_user, (username, firstname + " " + lastname,))
            set_data_from_template({"name": firstname + " " + lastname, "tag": username})
            set_data_from_template_backup({"name": firstname + " " + lastname, "tag": username})
            logging.info("Success first login for " + firstname + " " + lastname + " " + username)
            await bot.send_message(os.getenv('ERROR_CHAT_ID'),
                                   "Success FIRST login for " + firstname + " " + lastname)

    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
    conn.commit()
    conn.close()


def db_sql_buy_with_college(username):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    print(username)
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_count_tg_user_info = "select count(*) from bot_planeta_avto.tg_info_user where user_name_tg='{value_user_name_tg}';"
        cur.execute(sql_count_tg_user_info.format(value_user_name_tg=username))
        count_tg_user_info = cur.fetchall()
        print(count_tg_user_info[0][0])
        if count_tg_user_info[0][0] != 0:
            sql_select_tg_user_info = "select user_name_tg from bot_planeta_avto.tg_info_user where user_name_tg='{value_user_name_tg}';"
            cur.execute(sql_select_tg_user_info.format(value_user_name_tg=username))
            select_tg_user_info = cur.fetchall()

            return select_tg_user_info[0][0]
        else:
            print(count_tg_user_info[0][0])
            logging.error("Некорректный USERNAME " + username)
            return "Некорректный USERNAME"
    else:
        print(f'База недоступна, статус {conn.closed}')

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
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.purchase_report(type_purchase_report, platform,username_purchase_сolleagues,write_dkp,price,tires,vin,gos_number,brand,model,years,comment_report,username_purchase_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_tg_info_user, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_fio_dkp'],
            data['chosen_cost'], data['chosen_wire_boolean'], data['chosen_vin_number'],
            data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
            data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
        logging.info(
            "Success insert buy for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()


# async def db_sql_sell_insert(callback=types.CallbackQuery, dict_report=None):
#     if dict_report is None:
#         dict_report = {}
#     data = dict_report
#     print(data)
#     conn = psycopg2.connect(user=os.getenv('SQL_USER'),
#                             password=os.getenv('SQL_PASSWORD'),
#                             host=os.getenv('SQL_HOST'),
#                             port=os.getenv('SQL_PORT'),
#                             database=os.getenv('SQL_DATABASE')
#                             )
#     cur = conn.cursor()
#     if conn.closed == 0:
#         print(f'Успешное подключение к бд, статус {conn.closed}')
#         sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto_test.sell_report(type_sell_report,type_credit_our,type_deal,drom_cost,dealer_discount,summa_nm,summa_sob,howmuchtorg,whosell,whosellcredit,date_raschet,type_of_calс,vin,gos_number,brand,model,years,comment_report,username_sell_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#         cur.execute(sql_insert_tg_info_user, (
#             data['chosen_type'], data['type_credit_our'], data['type_deal'], data['drom_cost'],
#             data['dealer_discount'], data['summa_nm'], data['summa_sob'], data['howmuchtorg'], data['whosell'],
#             data['whosellcredit'], data['date_raschet'], data['type_raschet'], data['chosen_vin_number'],
#             data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
#             data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
#         logging.info(
#             "Success insert sell for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
#     else:
#         print(f'База недоступна, статус {conn.closed}')
#         logging.error(f'База недоступна, статус {conn.closed}')
#         await callback.message.answer(
#             text="База недоступна, свяжитесь с администратором>")
#     conn.commit()
#     conn.close()

async def db_sql_sell_insert(callback=types.CallbackQuery, dict_report=None):
    if dict_report is None:
        dict_report = {}
    htext = hlink('Техподдержкой', 'https://web.telegram.org/k/#@planeta_auto_support_bot')
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
        print(f'Успешное подключение к бд, статус {conn.closed}')
        try:
            sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.sell_report(type_sell_report,type_credit_our,type_deal,drom_cost,dealer_discount,summa_sob,howmuchtorg,whosell,whosellcredit,date_raschet,type_of_calс,vin,gos_number,brand,model,years,comment_report,username_sell_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql_insert_tg_info_user, (
                data['chosen_type'], data['type_credit_our'], data['type_deal'], data['drom_cost'],
                data['dealer_discount'], data['summa_sob'], data['howmuchtorg'], data['whosell'],
                data['whosellcredit'], data['date_raschet'], data['type_raschet'], data['chosen_vin_number'],
                data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
                data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
            logging.info(
                "Success insert sell for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
        except Exception as e:
            print(f'База недоступна, статус {conn.closed}')
            await callback.message.answer(
                text=f"База недоступна, свяжитесь с {htext}" + f"\nПередайте эти сведения {e}", parse_mode="HTML")
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text=f"База недоступна, свяжитесь с {htext}", parse_mode="HTML")
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
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_insert_comission_report = 'INSERT INTO bot_planeta_avto.commission_report(type_purchase_report, platform, username_commission_сolleagues, write_ag,price_owner, size_commission, vin, gos_number, brand, model, years, comment_report, username_commission_report, type_of_calс) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_comission_report, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'],
            data['howmuchsobs'], data['howmuchcomissiob'],
            data['chosen_vin_number'],
            data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
            data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,
            data['typeraschet']))
        logging.info(
            "Success insert comission for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()


def db_sql_price_owner_select(vin_dict):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        print(vin_dict)
        sql_select_vin_commission_report = "select price_owner from bot_planeta_avto.commission_report where vin='{value_vin_tg}';"
        cur.execute(sql_select_vin_commission_report.format(value_vin_tg=vin_dict))
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
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        # await callback.message.answer(
        #     text="База недоступна, свяжитесь с администратором>")

    conn.commit()
    conn.close()


def db_sql_vin_buy_owner_select(vin_dict):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        print("select vin from bot_planeta_avto.purchase_report pr \
                            where pr.vin='{value_vin_tg}' \
                            ;")
        sql_select_vin_all = "select vin from bot_planeta_avto.purchase_report pr \
                            where pr.vin='{value_vin_tg}' \
                            ;"
        cur.execute(sql_select_vin_all.format(value_vin_tg=vin_dict))
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
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()


def db_sql_vin_comission_owner_select(vin_dict):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_select_vin_all = "select vin from bot_planeta_avto.commission_report cr where cr.vin='{value_vin_tg}';"
        cur.execute(sql_select_vin_all.format(value_vin_tg=vin_dict))
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
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()


def db_sql_type_of_calc_select(vin_dict):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        print(vin_dict)
        sql_select_type_of_calс_commission_report = "select type_of_calс from bot_planeta_avto.commission_report where vin='{value_vin_tg}';"
        cur.execute(sql_select_type_of_calс_commission_report.format(value_vin_tg=vin_dict))
        select_type_of_calс = cur.fetchall()
        try:
            type_of_calс = select_type_of_calс[0][0]
            print(type_of_calс)
            logging.info(
                "Success select type_of_calc for ")
            return str(type_of_calс)
        except Exception as e:
            print("An error has occurred:", e)
            # await callback.message.answer(
            #     text="Вин номер не найдет, проверьте его корректность")
            return "UNKNOWN"
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        # await callback.message.answer(
        #     text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()


def db_sql_buy_editor_select(vin_dict):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        print(vin_dict)
        sql_select_buy_editor_report = "select * from bot_planeta_avto.purchase_report where vin='{value_vin_tg}';"
        cur.execute(sql_select_buy_editor_report.format(value_vin_tg=vin_dict))
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
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        # await callback.message.answer(
        #     text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()


def db_sql_comission_editor_select(vin_dict):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closed == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        print(vin_dict)
        sql_select_comission_editor_report = "select * from bot_planeta_avto.commission_report where vin='{value_vin_tg}';"
        cur.execute(sql_select_comission_editor_report.format(value_vin_tg=vin_dict))
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
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        # await callback.message.answer(
        #     text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()


async def date_normalizer(date_from_user):
    try:
        date_normal = datetime.datetime.strptime(date_from_user, "%d.%m.%Y").date().isoformat()
        return date_normal
    except Exception as e:
        print(e)
        return False

    # Функция для замены слов


def process_message(text):
    # Словарь для замены слов, обозначающих тысячи
    replacements = {
        'ТЫСЯЧА': '000',
        'ТЫСЯЧИ': '000',
        'ТЫС': '000',
        'К': '000',
        'Т': '000',
        'ТЫЩА': '000',
        'ТЫЩИ': '000',
        'МИЛЛИОН': '000000',
        'МИЛИОН': '000000',
        'МИЛЛИОНА': '000000',
        'МИЛЛИОНОВ': '000000',
        'ЛЯМ': '000000',
        'КК': '000000',
    }

    # Подготовка текста: преобразование в верхний регистр
    just = text.upper()

    # Функция для замены слов
    def replace(match):
        # Извлекаем найденное значение
        value = match.group(1)
        # Извлекаем ключевое слово для замены
        key_word = match.group(2)
        # Возвращаем число с добавленными нулями, если ключевое слово найдено
        return value + replacements.get(key_word, '')

    # Паттерн для поиска чисел, за которыми следуют ключевые слова, обозначающие тысячи
    pattern = r'(\d+)\s*(' + '|'.join(replacements.keys()) + ')'

    # Заменяем найденные сочетания на числа с тремя нулями
    just_transformed = re.sub(pattern, replace, just)

    # Убираем все нечисловые символы и преобразуем в целое число
    number = int(re.sub("[^0-9]", "", just_transformed))

    return number
