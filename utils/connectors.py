import json
import logging

import psycopg2
import os
from aiogram import Router, F, types, Bot


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


async def db_sql_start(username, firstname, lastname):
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
            logging.info("Succes first login for " + firstname + " " + lastname + " " + username)

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
            logging.info("Succes insert buy_with_college for " + username)
            return select_tg_user_info[0][0]
        else:
            print(count_tg_user_info[0][0])
            logging.error("Некорректный USERNAME "+ username)
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
        logging.info("Succes insert buy for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text="База недоступна, свяжитесь с администратором>")
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
        sql_insert_comission_report = 'INSERT INTO bot_planeta_avto.commission_report(type_purchase_report, platform, username_commission_сolleagues, write_ag,price_owner, size_commission, vin, gos_number, brand, model, years, comment_report, username_commission_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_comission_report, (
            data['chosen_type'], data['chosen_place'], data['chosen_college_fio'], data['chosen_college_dkps'],
            data['howmuchsobs'], data['howmuchcomissiob'],
            data['chosen_vin_number'],
            data['chosen_vin_gos_number'], data['chosen_vin_marka'], data['chosen_vin_model'], data['chosen_vin_year'],
            data['chosen_comment'], callback.message.chat.first_name + " " + callback.message.chat.last_name,))
        logging.info(
            "Succes insert comission for " + callback.message.chat.first_name + " " + callback.message.chat.last_name)
    else:
        print(f'База недоступна, статус {conn.closed}')
        logging.error(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()
