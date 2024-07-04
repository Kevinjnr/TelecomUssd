from TelecomProject.ussd_short import invalid, out, wait, clear, print_slowly, countdown_timer, wait_and_count
from TelecomProject.ussd_process import buyData, buyDataTalk, checkDataBal
import time
from animation.colors import *
import pymysql
import time

db = pymysql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()


# Data plan
def data_plans_subscription():
    wait()
    print()
    print(f'\t\t\t{brt_black_bg}{brt_blue}BUY DATA PLANS{end}   {bold}{magenta}')
    time.sleep(0.6)
    print_slowly(f'{brt_black_bg}{brt_yellow}1. Daily Plan')
    time.sleep(0.6)
    print_slowly('2. Weekly Plan')
    time.sleep(0.6)
    print_slowly('3. Monthly Plan')
    time.sleep(0.6)
    print('4. 2-3Month Plan ')
    time.sleep(0.6)
    print_slowly('5. Always On Plan')
    time.sleep(0.6)
    print_slowly('6. Hot Deals')
    time.sleep(0.6)
    print_slowly('7. Manage Data')
    time.sleep(0.6)
    print_slowly(f'0. Back{end} {bold}{magenta}')


def daily_plan():
    wait()
    while True:
        print()
        print(f'\t\t\t{brt_black_bg}{brt_green}Daily Plan{end}  {bold}{magenta}\n')
        print(f'{brt_black_bg}{brt_yellow}1. 100MB for N100')
        time.sleep(0.6)
        print('2. 200MB for N200')
        time.sleep(0.6)
        print('3. 350MB for N300')
        time.sleep(0.6)
        print('4. 1.5GB for N500')
        time.sleep(0.6)
        print('5. 2GB for N600')
        time.sleep(0.6)
        print(f'0. Back{end}  {bold}{magenta}')
        opt = input('\t>>> ').strip()

        if opt == '1':
            wait_and_count()
            while True:
                print()
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                if user:
                    data_amount = 100
                    cost = 100

                    buyData(phone_number, data_amount, cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()

        elif opt == '2':
            wait_and_count()
            while True:
                print()
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 200
                    cost = 200

                    buyData(phone_number, data_amount, cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif opt == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 350
                    cost = 300

                    buyData(phone_number, data_amount, cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif opt == '4':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1500
                    cost = 500

                    buyData(phone_number, data_amount, cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif opt == '5':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 2000
                    cost = 600

                    buyData(phone_number, data_amount, cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif opt == '0':
            dataPlan()

        else:
            out()


def weekly_plan():
    wait()
    while True:
        print()
        print(f'\t\t{brt_black_bg}{brt_cyan}Weekly Plan{end} {bold}{magenta} \n')
        print(f'{brt_black_bg}{brt_yellow}1. N300 for 350MB')
        time.sleep(0.6)
        print('2. N500 for 700MB/7days')
        time.sleep(0.6)
        print('3. N600 for 1GB')
        time.sleep(0.6)
        print('4. N1000 for 1.5GB')
        time.sleep(0.6)
        print(f'0. Back{end}{bold}{magenta}')
        time.sleep(0.6)
        option = input('\t>>> ').strip()

        if option == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 350
                    cost = 300
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

        elif option == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 700
                    cost = 500
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

        elif option == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1000
                    cost = 600
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

        elif option == '4':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1500
                    cost = 1000
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

        elif option == '0':
            dataPlan()

        else:
            out()


def monthly_plan():
    wait()
    while True:
        print()
        print(f'\t\t{brt_black_bg}{brt_green}Monthly Plan{end}\n')
        print(f'{brt_black_bg}{brt_yellow}1. N1000 for 1.2GB')
        time.sleep(0.6)
        print('2. N1200 for 1.5GB')
        time.sleep(0.6)
        print('3. N2000 for 4GB')
        time.sleep(0.6)
        print('4. N3000 for 8GB')
        time.sleep(0.6)
        print(f'0. Back{end} {bold}{magenta}')
        time.sleep(0.6)
        option = input('\t>>> ').strip()

        if option == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1200
                    cost = 1000
                    days = 30

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1500
                    cost = 1200
                    days = 30

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 4000
                    cost = 2000
                    days = 30

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '4':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 8000
                    cost = 3000
                    days = 30

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '0':
            dataPlan()

        else:
            out()


def _2_3month_plan():
    wait()
    while True:
        print()
        print(f'\t\t{brt_black_bg}{brt_red}2-3 Month Plan{end}\n')
        print(f'{brt_black_bg}{brt_yellow}1. N8000 for 30GB/60days')
        time.sleep(0.6)
        print('2. N20000 for 100GB/60days')
        time.sleep(0.6)
        print('3. N30000 for 160GB/60days')
        time.sleep(0.6)
        print('4. N50000 for 400GB/90days')
        time.sleep(0.6)
        print(f'0. Back{end}{bold}{magenta}')
        time.sleep(0.6)
        option = input('\t>>> ').strip()

        if option == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 30000
                    cost = 8000
                    days = 60

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 100000
                    cost = 20000
                    days = 60

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 160000
                    cost = 30000
                    days = 60

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '4':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 400000
                    cost = 50000
                    days = 90

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '0':
            dataPlan()

        else:
            out()


def always_on_plan():
    wait()
    while True:
        print()
        print(f'\t\t{brt_black_bg}{brt_green}Always on Bundle{end}')
        print(f'{brt_black_bg}{brt_yellow}1. N60 for 200MB/24hrs')
        time.sleep(0.6)
        print('2. N120 for 450MB/7days')
        time.sleep(0.6)
        print('3. N3000 for 15GB/30days')
        time.sleep(0.6)
        print('4. N6000 for 45GB/30days')
        time.sleep(0.6)
        print(f'0. Back{end}{bold}{magenta}')
        option = input('\t>>>').strip()

        if option == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 200
                    cost = 60

                    buyData(phone_number, data_amount, cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 450
                    cost = 120
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

        elif option == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 15000
                    cost = 3000
                    days = 30

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '4':
            wait_and_count()
            while True:
                print()
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 45000
                    cost = 6000
                    days = 30

                    buyData(phone_number, data_amount, cost, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '0':
            dataPlan()

        else:
            out()


def hot_deals_plan():
    wait()
    while True:
        print()
        print(f'\t\t{brt_black_bg}{brt_magenta}Hot Deals Plan{end}')
        print(f'{brt_black_bg}{brt_yellow}1. N500-750MB +500 Talk time/14days')
        time.sleep(0.6)
        print('2. N1000-1.5GB +1000 Talk time/30days')
        time.sleep(0.6)
        print('3. N2000-4.5GB +2000 Talk time/30days')
        time.sleep(0.6)
        print(f'0 back{end}{bold}{magenta}')
        time.sleep(0.6)
        option = input('\t>>> ').strip()

        if option == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 750
                    cost = 500
                    talk_time = 500
                    days = 14

                    buyDataTalk(phone_number, data_amount, cost, talk_time, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '2':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1500
                    cost = 1000
                    talk_time = 1000
                    days = 30

                    buyDataTalk(phone_number, data_amount, cost, talk_time, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '3':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 4500
                    cost = 2000
                    talk_time = 2000
                    days = 30

                    buyDataTalk(phone_number, data_amount, cost, talk_time, days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()

                else:
                    invalid()

        elif option == '0':
            dataPlan()

        else:
            out()


def manage_data_plan():
    wait()
    while True:
        print()
        print(f'\t\t{brt_black_bg}{brt_white}Manage Data Plan{end}')
        print(f'{brt_black_bg}{brt_yellow}1. VIEW ACTIVE DATA BUNDLE')
        time.sleep(0.6)
        print(f'0. back{end}{bold}{magenta}')
        time.sleep(0.6)

        option = input('\t>>> ').strip()

        if option == '1':
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    wait_and_count()
                    clear()
                    checkDataBal(phone_number)

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()

        elif option == '0':
            dataPlan()

        else:
            out()


# Data plan
def dataPlan():
    from TelecomProject.test import main_menu
    wait()
    data_plans_subscription()

    user_result = input('\t>>> ').strip()
    if user_result == '1':
        clear()
        print(end='\r')
        print(end='\r')
        daily_plan()
        time.sleep(1)
        exit()

    elif user_result == '2':
        clear()
        print(end='\r')
        print(end='\r')
        weekly_plan()
        time.sleep(1)
        exit()

    elif user_result == '3':
        clear()
        print(end='\r')
        print(end='\r')
        monthly_plan()
        time.sleep(1)
        exit()

    elif user_result == '4':
        clear()
        print(end='\r')
        print(end='\r')
        _2_3month_plan()
        time.sleep(1)
        exit()

    elif user_result == '5':
        clear()
        print(end='\r')
        print(end='\r')
        always_on_plan()
        time.sleep(1)
        exit()

    elif user_result == '6':
        clear()
        print(end='\r')
        print(end='\r')
        hot_deals_plan()
        time.sleep(1)
        exit()

    elif user_result == '7':
        clear()
        print(end='\r')
        print(end='\r')
        manage_data_plan()
        time.sleep(1)
        exit()

    elif user_result == '0':
        main_menu()

    else:
        out()
        time.sleep(1)
        dataPlan()


# dataPlan()
