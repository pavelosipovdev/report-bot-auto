import psycopg2
import os

dict_colleges = [
    {"id": "1", "name": "Осипов Павел", "tag": "rogerthatdev"},
    {"id": "2", "name": "Чудин Павел", "tag": "p_chudin"}
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
        sql_count_tg_user_info = "select count(*) from bot_planeta_avto.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
        cur.execute(sql_count_tg_user_info.format(value_teg_name_tg=username))
        count_tg_user_info = cur.fetchall()
        print(count_tg_user_info[0][0])
        if count_tg_user_info[0][0] != 0:
            sql_select_tg_user_info = "select user_name_tg from bot_planeta_avto.tg_info_user where teg_name_tg='{value_teg_name_tg}';"
            cur.execute(sql_select_tg_user_info.format(value_teg_name_tg=username))
            select_tg_user_info = cur.fetchall()
            return select_tg_user_info[0][0]
        else:
            print(count_tg_user_info[0][0])
            return "Некорректный USERNAME"
    else:
        print(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()


def db_sql_buy_insert(dict_report):
    conn = psycopg2.connect(user=os.getenv('SQL_USER'),
                            password=os.getenv('SQL_PASSWORD'),
                            host=os.getenv('SQL_HOST'),
                            port=os.getenv('SQL_PORT'),
                            database=os.getenv('SQL_DATABASE')
                            )
    cur = conn.cursor()
    if conn.closes == 0:
        print(f'Успешное подключение к бд, статус {conn.closed}')
        sql_insert_tg_info_user = 'INSERT INTO bot_planeta_avto.purchase_report(type_purchase_report, platform,username_purchase_сolleagues,write_dkp,price,tires,vin,gos_number,brand,model,years,comment_report,username_purchase_report) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql_insert_tg_info_user, (
        type_purchase_report[0], platform[0], username_purchase_сolleagues[0], write_dkp[0], price[0], tires[0], vin[0],
        gos_number[0], brand[0], model[0], years[0], comment_report[0], username_purchase_report[0],))
    else:
        print(f'База недоступна, статус {conn.closed}')

    conn.commit()
    conn.close()
