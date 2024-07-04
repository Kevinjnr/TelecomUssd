from TelecomProject.ussd_short import invalid, out, wait, clear, print_slowly, countdown_timer, wait_and_count
from TelecomProject.ussd_process import buyData, buyDataTalk
import time
from animation.colors import *
import pymysql

db = pymysql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()


# Roaming int'l
def travel_pass_plan():
    wait()
    while True:
        print()
        print(f" \t\t{brt_black_bg}{brt_blue}Travel Pass Plan{end} \n")
        time.sleep(1)
        print(f"{brt_black_bg}{brt_yellow}1. 7days(voice) 4000talktime and 100MB @ ₦10,000.")
        time.sleep(1)
        print("2. 7days 1GB Data @ ₦10,000.")
        time.sleep(1)
        print(f'0. back{end}    {bold}  {magenta}')
        # time.sleep(1)
        # print("3. Inflight Roaming Data.")
        # time.sleep(1)
        # print("4. Roaming Balance Check.")
        time.sleep(1.5)
        ans = input(">>> ").strip()

        if ans == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 100
                    cost = 10000
                    talk_time = 4000
                    days = 7

                    buyDataTalk(phone_number, data_amount, cost, talk_time, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1000
                    cost = 10000
                    days = 7

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '0':
            roaming_int()

        else:
            out()
            clear()


def data_hybrid():
    wait()
    while True:
        print()
        print(f"\t\t{brt_black_bg}{brt_magenta}Data Hybrid{end} \n")
        time.sleep(1)
        print(f"{brt_black_bg}{brt_yellow}1. ₦2,000 for 4GB.")
        time.sleep(1)
        print("2. ₦3,000 for 8GB.")
        time.sleep(1)
        print("3. ₦3,500 for 10GB.")
        time.sleep(1)
        print("4. ₦4,000 for 12GB.")
        time.sleep(1)
        print(f'0. back{end}{bold}{magenta}')
        time.sleep(1.5)
        ans = input("\t>>> ").strip()

        if ans == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 4000
                    cost = 2000
                    days = 14

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 8000
                    cost = 3000
                    days = 14

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 10000
                    cost = 3500
                    days = 14

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '4':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 12000
                    cost = 4000
                    days = 14

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '0':
            roaming_int()

        else:
            out()
            clear()


def inflight_roaming_data():
    wait()
    while True:
        print()
        print(f"\t{brt_black_bg}{brt_red}Inflight Roaming Data{end} \n")
        time.sleep(1)
        print(f"{brt_black_bg}{brt_yellow}1. 50MB @ ₦200.")
        time.sleep(1.5)
        print(f'0. back{end}{bold}{magenta}')
        ans = input("\t>>> ").strip()

        if ans == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 50
                    cost = 200
                    days = 3

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    clear()

        elif ans == '0':
            roaming_int()

        else:
            out()


def roaming_int():
    from TelecomProject.test import main_menu
    while True:
        wait()
        print()
        print(f"\t\t{brt_black_bg}{brt_white}Roaming{end} \n")
        time.sleep(1)
        print_slowly(f"{brt_black_bg}{brt_yellow}1. Travel Pass Plan.")
        time.sleep(1)
        print_slowly("2. Data Hybrid")
        time.sleep(1)
        print_slowly("3. Inflight Roaming Data")
        time.sleep(1)
        print_slowly(f'0. Back{end}{bold}{magenta}')
        time.sleep(1.5)
        ans = input("\t>>> ").strip()

        if ans == '1':
            clear()
            travel_pass_plan()
            time.sleep(1)
            exit()

        elif ans == '2':
            clear()
            data_hybrid()
            time.sleep(1)
            exit()

        elif ans == '3':
            clear()
            inflight_roaming_data()
            time.sleep(1)
            exit()

        elif ans == '0':
            main_menu()

        else:
            out()
            clear()
            roaming_int()

