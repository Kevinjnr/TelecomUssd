from TelecomProject.ussd_short import invalid, out, wait, clear, print_slowly, countdown_timer, wait_and_count
from TelecomProject.ussd_process import buy_friend_data, data_trans
import time
from animation.colors import *
import pymysql
import time
import re

db = pymysql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()


# Transfer data
def data_transfer():
    try:
        wait()
        while True:
            print(f'\n{brt_yellow}Please enter phone number to continue:{end} {bold}{magenta} ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            sender_number = input('>>> ').strip()
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (sender_number))

            if user:
                wait()
                while True:
                    print(f"{brt_yellow}\nEnter recipient's number:{end} {bold}{magenta} ")
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                    receiver_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (receiver_number))

                    if user:
                        wait()
                        while True:
                            print(f'{brt_yellow}Please enter data amount:{end} {bold}{magenta} ')
                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                            data_amount = input('>>> ').strip()

                            if data_amount.isnumeric():
                                data_amount = int(data_amount)

                                limit = 2000
                                if data_amount <= int(limit):

                                    wait_and_count()
                                    data_trans(sender_number, receiver_number, data_amount)
                                    db.commit()

                                    print(end='\r')
                                    print(end='\r')
                                    time.sleep(1)
                                    clear()
                                    break

                                else:
                                    print()
                                    print(f"{brt_red}::Can't make transfer more than 2000MB{end}{bold}{magenta} ")
                                    time.sleep(0.7)
                                    print(f'{brt_red}::Re-enter amount{end}{bold}{magenta}')
                                    time.sleep(4)
                                    clear()

                            else:
                                out()
                                time.sleep(3)
                                clear()

                    else:
                        invalid()
                        time.sleep(3)
                        clear()

            else:
                invalid()
                time.sleep(3)
                clear()

    except Exception as e:
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)


# Buy for a friend
def buy_friend():
    try:
        wait()
        while True:
            print()
            print(f'{brt_yellow}Please enter phone number to continue:{end} {bold}{magenta} ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            sender_number = input('>>> ').strip()
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (sender_number))

            if user:
                wait()
                while True:
                    print()
                    print(f'\t\t{brt_black_bg}{brt_blue}Welcome to our gifting service.Select data plan to gift.{end}')
                    time.sleep(0.6)
                    print_slowly(f'{brt_black_bg}{brt_yellow}1. Data Plans')
                    time.sleep(0.6)
                    print_slowly('2. Social Bundles')
                    time.sleep(0.6)
                    print_slowly('3. Video Pack')
                    time.sleep(0.6)
                    print_slowly(f'0. Back{end} {bold}{magenta}')
                    opt = input('\t>>> ').strip()

                    if opt == '1':
                        wait()
                        while True:
                            print()
                            print(f'\t\t{brt_black_bg}{brt_cyan}BUY DATA PLANS{end}')
                            time.sleep(0.6)
                            print_slowly(f'{brt_black_bg}{brt_yellow}1. Daily Plan')
                            time.sleep(0.6)
                            print_slowly('2. Weekly Plan')
                            time.sleep(0.6)
                            print_slowly('3. Monthly Plan')
                            time.sleep(0.6)
                            print_slowly(f'4. 2-3Month Plan {end} {bold}{magenta}')
                            ans = input('\t>>> ').strip()

                            if ans == '1':
                                wait()
                                while True:
                                    print()
                                    print(f'\t\t{brt_black_bg}{brt_red}Daily Plan{end}\n')
                                    print(f'{brt_black_bg}{brt_yellow}1. 100MB for N100')
                                    time.sleep(0.6)
                                    print('2. 200MB for N200')
                                    time.sleep(0.6)
                                    print('3. 350MB for N300')
                                    time.sleep(0.6)
                                    print(f'4. 1.5GB for N500{end} {bold}{magenta}')
                                    res = input('\t>>> ').strip()
                                    clear()

                                    if res == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 100
                                                cost = 100

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                time.sleep(3)
                                                clear()

                                    elif re.search('^.*(back|return).*$', res, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif res == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 200
                                                cost = 200

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                time.sleep(3)
                                                clear()

                                    elif res == '3':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 350
                                                cost = 300

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                time.sleep(3)
                                                clear()

                                    elif res == '4':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1500
                                                cost = 500

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                time.sleep(3)
                                                clear()

                                    else:
                                        out()
                                        time.sleep(3)
                                        clear()
                            elif re.search('^.*(back|return).*$', ans, re.IGNORECASE):
                                # If the user types 'back' or 'return', exit the function.
                                gift_data()

                            elif ans == '2':
                                wait()
                                while True:
                                    print()
                                    print(f'\t\t{brt_black_bg}{brt_blue}Weekly Plan{end}')
                                    print(f'{brt_black_bg}{brt_yellow}1. N300 for 350MB')
                                    time.sleep(0.6)
                                    print('2. N500 for 700MB/7days')
                                    time.sleep(0.6)
                                    print('3. N600 for 1GB')
                                    time.sleep(0.6)
                                    print(f'4. N1000 for 1.5GB{end}{bold}{magenta}')
                                    time.sleep(0.6)
                                    res = input('\t>>> ').strip()

                                    if res == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 350
                                                cost = 300
                                                days = 7

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                time.sleep(3)
                                                clear()

                                    elif re.search('^.*(back|return).*$', res, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif res == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 700
                                                cost = 500
                                                days = 7

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                time.sleep(3)
                                                clear()

                                    elif res == '3':
                                        print()
                                        print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                        print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                        receiver_number = input('>>> ').strip()
                                        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                        user = my_cur.execute(check_num, (receiver_number))

                                        if user:
                                            data_amount = 1000
                                            cost = 600
                                            days = 7

                                            buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                            db.commit()

                                            print(end='\r')
                                            print(end='\r')
                                            time.sleep(1)
                                            clear()
                                            break

                                        else:
                                            invalid()
                                            clear()

                                    elif res == '4':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1500
                                                cost = 1000
                                                days = 7

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
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
                                    print(f'4. N3000 for 8GB{end} {bold}{magenta}')
                                    time.sleep(0.6)
                                    res = input('\t>>> ').strip()

                                    if res == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1200
                                                cost = 1000
                                                days = 30

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif re.search('^.*(back|return).*$', res, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif res == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1500
                                                cost = 1200
                                                days = 30

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif res == '3':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 4000
                                                cost = 2000
                                                days = 30

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif res == '4':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 8000
                                                cost = 3000
                                                days = 30

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
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
                                wait()
                                while True:
                                    print()
                                    print(f'\t\t{brt_black_bg}{brt_white}2-3 Month Plan{end}n')
                                    print(f'{brt_black_bg}{brt_yellow}1. N8000 for 30GB/60days')
                                    time.sleep(0.6)
                                    print('2. N20000 for 100GB/60days')
                                    time.sleep(0.6)
                                    print('3. N30000 for 160GB/60days')
                                    time.sleep(0.6)
                                    print(f'4. N50000 for 400GB/90days{end}{bold}{magenta}')
                                    time.sleep(0.6)
                                    res = input('\t>>> ').strip()

                                    if res == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 30000
                                                cost = 8000
                                                days = 60

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif re.search('^.*(back|return).*$', res, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif res == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 100000
                                                cost = 20000
                                                days = 60

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif res == '3':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 160000
                                                cost = 30000
                                                days = 60

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif res == '4':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 400000
                                                cost = 50000
                                                days = 90

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    else:
                                        out()
                                        clear()
                            else:
                                out()
                                time.sleep(0.5)
                                clear()

                    elif re.search('^.*(back|return).*$', opt, re.IGNORECASE):
                        # If the user types 'back' or 'return', exit the function.
                        gift_data()

                    elif opt == '2':
                        wait()
                        while True:
                            print()
                            print(f'\t\t{brt_black_bg}{brt_blue}Social Bundles{end}')
                            time.sleep(1)
                            print_slowly(f"{brt_black_bg}{brt_yellow}1. Whatsapp")
                            time.sleep(1)
                            print_slowly("2. Facebook")
                            time.sleep(1)
                            print_slowly("3. Instagram")
                            time.sleep(1)
                            print_slowly("4. Tiktok")
                            time.sleep(1)
                            print_slowly(f'0.Back{end}{bold}{magenta}')
                            time.sleep(1)
                            ask = input('\t>>> ').strip()

                            if ask == '1':
                                while True:
                                    wait()
                                    print()
                                    print(f"\t\t{brt_black_bg}{brt_magenta}Whatsapp{end}\n")
                                    print(f"{brt_black_bg}{brt_yellow}1. Daily @ ₦25 for 50MB")
                                    time.sleep(1)
                                    print("2. Weekly @ ₦50 for 100MB")
                                    time.sleep(1)
                                    print(f"3. Monthly @ ₦150 for 200MB{end}{bold}{magenta}")
                                    time.sleep(1.5)
                                    ans = input("\t>>> ").strip()

                                    if ans == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 50
                                                cost = 25

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif re.search('^.*(back|return).*$', ans, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif ans == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 100
                                                cost = 50
                                                days = 7

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
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
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 200
                                                cost = 150
                                                days = 30

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()
                                    else:
                                        out()
                                        clear()

                            elif re.search('^.*(back|return).*$', ask, re.IGNORECASE):
                                # If the user types 'back' or 'return', exit the function.
                                gift_data()

                            elif ask == '2':
                                while True:
                                    wait()
                                    print()
                                    print(f"\t\t{brt_black_bg}{brt_green}Facebook{end}\n")
                                    print(f"{brt_black_bg}{brt_yellow}1. Daily @ ₦25 for 50MB")
                                    time.sleep(1)
                                    print("2. Weekly @ ₦50 for 100MB")
                                    time.sleep(1)
                                    print(f"3. Monthly @ ₦150 for 250MB{end} {bold}{magenta}")
                                    time.sleep(1.5)
                                    ans = input("\t>>> ").strip()

                                    if ans == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 50
                                                cost = 25

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif re.search('^.*(back|return).*$', ans, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif ans == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 100
                                                cost = 50
                                                days = 7

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
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
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 250
                                                cost = 150
                                                days = 30

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    else:
                                        out()
                                        clear()

                            elif ask == '3':
                                wait()
                                while True:
                                    print()
                                    print(f"\t\t{brt_black_bg}{brt_blue}Instagram{end}\n")
                                    print(f"{brt_black_bg}{brt_yellow}1. ₦100 for 250MB/1 day.")
                                    time.sleep(1)
                                    print("2. ₦150 for 350MB/2 days.")
                                    time.sleep(1)
                                    print("3. ₦200 for 1GB/1 day.")
                                    time.sleep(1)
                                    print(f"4. ₦250 for 1.5GB/3-days.{end}{bold}{magenta}")
                                    time.sleep(1.5)
                                    ans = input("\t>>> ").strip()

                                    if ans == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 250
                                                cost = 100

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif re.search('^.*(back|return).*$', ans, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif ans == '2':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 350
                                                cost = 150
                                                days = 2

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
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
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1000
                                                cost = 200

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
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
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1500
                                                cost = 250
                                                days = 3

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    else:
                                        out()
                                        clear()

                            elif ask == '4':
                                while True:
                                    wait()
                                    print()
                                    print(f"\t\t{brt_black_bg}{brt_magenta}Tiktok{end}")
                                    print(f"{brt_black_bg}{brt_yellow}1. ₦100 for 200MB/1 day.")
                                    time.sleep(1)
                                    print("2. ₦150 for 350MB/2 days.")
                                    time.sleep(1)
                                    print("3. ₦200 for 1GB/1 day.")
                                    time.sleep(1)
                                    print(f"4. ₦200 for 1.5GB/3-days.{end}{bold}{magenta}")
                                    time.sleep(1.5)
                                    ans = input("\t>>> ").strip()

                                    if ans == '1':
                                        while True:
                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 200
                                                cost = 100

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif re.search('^.*(back|return).*$', ans, re.IGNORECASE):
                                        # If the user types 'back' or 'return', exit the function.
                                        gift_data()

                                    elif ans == '2':
                                        while True:

                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 350
                                                cost = 150
                                                days = 2

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
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
                                        while True:

                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1000
                                                cost = 200

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
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
                                        while True:

                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1500
                                                cost = 200
                                                days = 3

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost, days)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    else:
                                        out()
                                        clear()

                            elif ask == '0':
                                buy_friend()

                            else:
                                out()
                                clear()

                    elif opt == '3':
                        while True:
                            print()
                            print(f"\t\t{brt_black_bg}{brt_green} Video Packs{end} \n")
                            time.sleep(0.6)
                            print(f"{brt_black_bg}{brt_yellow}1. Youtube video packs.{end}{bold}{magenta}")
                            time.sleep(0.6)
                            ans = input('\t>>> ').strip()

                            if ans == '1':
                                wait()
                                while True:

                                    print()
                                    print(f" \t\t{brt_black_bg}{brt_magenta}YouTube Video Packs{end}\n")
                                    print(f"{brt_black_bg}{brt_yellow}1. 24 hour @ ₦100 for 800MB.")
                                    time.sleep(1)
                                    print("2. 24 hours @ ₦150 for 1.2GB.")
                                    time.sleep(1)
                                    print(f"3. 500MB at ₦50 24 hours.{end}{bold}{magenta}")
                                    time.sleep(1.5)

                                    ask = input("\t>>> ").strip()

                                    if ask == '1':
                                        while True:

                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 800
                                                cost = 100

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif ask == '2':
                                        while True:

                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 1200
                                                cost = 150

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    elif ask == '3':
                                        while True:

                                            print()
                                            print(f"{brt_yellow}Enter recipient's number:{end} {bold}{magenta} ")
                                            print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                            receiver_number = input('>>> ').strip()
                                            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                                            user = my_cur.execute(check_num, (receiver_number))

                                            if user:
                                                data_amount = 500
                                                cost = 50

                                                buy_friend_data(sender_number, receiver_number, data_amount, cost)
                                                db.commit()

                                                print(end='\r')
                                                print(end='\r')
                                                time.sleep(1)
                                                clear()
                                                break

                                            else:
                                                invalid()
                                                clear()

                                    else:
                                        out()
                                        clear()

                            else:
                                out()
                                clear()

                    elif opt == '0':
                        buy_friend()

                    else:
                        out()
                        clear()

            else:
                invalid()
                clear()

            clear()

    except Exception as e:
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)


# GIFT DATA
def gift_data():
    from TelecomProject.test import main_menu
    wait()
    print()
    print(f'\t\t{brt_black_bg}{brt_red}Gift Data{end}')
    print()
    time.sleep(0.6)
    print_slowly(f'{brt_black_bg}{brt_yellow}1.Transfer from data balance')
    time.sleep(0.6)
    print_slowly('2.Buy for a friend')
    time.sleep(0.6)
    print_slowly(f'0. Back{end}{bold}{magenta}')
    time.sleep(0.6)
    opt = input('\t>>> ').strip()

    if opt == '1':
        clear()
        data_transfer()
        clear()


    elif opt == '2':
        clear()
        buy_friend()
        clear()

    elif opt == '0':
        main_menu()

    else:
        out()
        clear()
        gift_data()


clear()
