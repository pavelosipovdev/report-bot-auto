import psycopg2
import os
from aiogram import Router, F, types, Bot

dict_colleges = [
    {"name": "Papa Roach", "tag": "rogerthatdev"},
    {"name": "Pavel Chudin", "tag": "p_chudin"},
    {"name": "Семен Дьяченко", "tag": "Semen008"},
]


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
        cur.execute(sql_count_tg_user_info.format(value_teg_name_tg="@" + username))
        count_tg_user_info = cur.fetchall()
        print(count_tg_user_info[0][0])

        if count_tg_user_info[0][0] == 0:
            sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.tg_info_user(teg_name_tg, user_name_tg) VALUES (%s,%s)'
            cur.execute(sql_insert_tg_info_user, ("@" + username, firstname + " " + lastname,))
    else:
        print(f'База недоступна, статус {conn.closed}')
    conn.commit()
    conn.close()
    # with open("dict_report.txt", "a") as myfile:
    #     myfile.write("@" + username + firstname + " " + lastname)


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
            data['chosen_comment'], callback.message.chat.last_name + " " + callback.message.chat.first_name,))
    else:
        print(f'База недоступна, статус {conn.closed}')
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
            data['chosen_comment'], callback.message.chat.last_name + " " + callback.message.chat.first_name,))
    else:
        print(f'База недоступна, статус {conn.closed}')
        await callback.message.answer(
            text="База недоступна, свяжитесь с администратором>")
    conn.commit()
    conn.close()
