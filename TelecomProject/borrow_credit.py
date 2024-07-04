from TelecomProject.ussd_short import invalid, out, wait, clear, print_slowly, countdown_timer, wait_and_count
from TelecomProject.ussd_process import borrow_air, borrow_mydata
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


# Borrow airtime
def borrow_airtime():
    try:
        wait()
        while True:
            print()
            print(f'{brt_black_bg}{brt_green}\tBorrow Airtime{end}')
            time.sleep(0.6)
            print(f'{brt_black_bg}{brt_yellow}1. N50 ')
            time.sleep(0.6)
            print('2. N100 ')
            time.sleep(0.6)
            print('3. N500')
            time.sleep(0.6)
            print(f'0. back{end}{bold}{magenta}')
            time.sleep(0.6)
            opt = input('>>> ').strip()

            if opt == '1':
                wait()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))

                    # check if user is in db
                    if user:
                        amount = 50

                        borrow_air(phone_number, amount)
                        db.commit()
                        break

                    else:
                        invalid()
                        time.sleep(4)
                        clear()

            elif opt == '2':
                wait()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))

                    # check if user is in db
                    if user:
                        amount = 100

                        borrow_air(phone_number, amount)
                        db.commit()
                        break

                    else:
                        invalid()
                        time.sleep(4)
                        clear()

            elif opt == '3':
                wait()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))

                    # check if user is in db
                    if user:
                        amount = 500

                        borrow_air(phone_number, amount)
                        db.commit()
                        break

                    else:
                        invalid()
                        time.sleep(4)
                        clear()

            elif opt == '0':
                borrow_credit()

            else:
                out()
                time.sleep(4)
                clear()

    except Exception as e:
        print(f'{brt_red}::An error Occurred: ', e, end, bold, magenta)


# Borrow data
def borrow_data():
    try:
        while True:
            wait()
            print()
            print(f'\t{brt_black_bg}{brt_red}Borrow Data{end}')
            time.sleep(0.6)
            print(f'{brt_black_bg}{brt_yellow}1. 100MB ')
            time.sleep(0.6)
            print('2. 150MB ')
            time.sleep(0.6)
            print('3. 500MB')
            time.sleep(0.6)
            print(f'0. back{end}{bold}{magenta}')
            time.sleep(0.6)
            opt = input('>>> ').strip()

            if opt == '1':
                wait()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))

                    # check if user is in db
                    if user:
                        data_amount = 100

                        borrow_mydata(phone_number, data_amount)
                        db.commit()
                        break

                    else:
                        invalid()
                        time.sleep(4)
                        clear()

            elif opt == '2':
                wait()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))

                    # check if user is in db
                    if user:
                        data_amount = 150

                        borrow_mydata(phone_number, data_amount)
                        db.commit()
                        break

                    else:
                        invalid()

            elif opt == '3':
                wait()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))

                    # check if user is in db
                    if user:
                        data_amount = 500

                        borrow_mydata(phone_number, data_amount)
                        db.commit()
                        break

                    else:
                        invalid()
                        time.sleep(4)
                        clear()

            elif opt == '0':
                borrow_credit()

            else:
                out()
                time.sleep(4)
                clear()

    except Exception as e:
        print(f'{brt_red}::An error Occurred: ', e, end, bold, magenta)


# Borrow airtime & Data
def borrow_credit():
    from TelecomProject.test import main_menu
    wait()
    time.sleep(0.6)
    print()
    print_slowly(f'\t\t{brt_black_bg}{brt_red}Borrow credit{end} ')
    time.sleep(0.6)
    print_slowly(f'{brt_black_bg}{brt_yellow}1.Borrow Airtime')
    time.sleep(0.6)
    print_slowly('2. Borrow Data')
    time.sleep(0.6)
    print_slowly(f'0. Back{end}{bold}{magenta}')
    time.sleep(0.6)
    opt = input('>>> ').strip()

    if opt == '1':
        borrow_airtime()

    elif opt == '2':
        borrow_data()

    elif opt == '0':
        main_menu()

    else:
        out()
        time.sleep(4)
        clear()
        borrow_credit()

