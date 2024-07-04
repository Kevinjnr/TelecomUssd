from TelecomProject.ussd_short import invalid, out, wait, clear, print_slowly, countdown_timer, wait_and_count
from TelecomProject.ussd_process import buyData
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


# SOCIAL BUNDLE CODE
def whatsapp():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_black_bg}{brt_green}Whatsapp{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 200MB")
            time.sleep(1)
            print(f'0. back{end}{bold}{magenta}')
            time.sleep(1.5)
            ans = input("\t>>> ").strip()
            if ans.isnumeric():
                if ans == '1':
                    wait_and_count()
                    while True:
                        print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        phone_number = input('>>> ').strip()
                        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                        user = my_cur.execute(check_num, (phone_number))
                        if user:
                            data_amount = 50
                            cost = 25

                            buyData(phone_number, data_amount, cost)
                            db.commit()

                            print(end='\r')
                            print(end='\r')
                            time.sleep(1)
                            clear()
                            break

                        else:
                            invalid()

                elif ans == '2':
                    wait_and_count()
                    while True:
                        print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        phone_number = input('>>> ').strip()
                        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                        user = my_cur.execute(check_num, (phone_number))
                        if user:
                            data_amount = 100
                            cost = 50
                            valid_days = 7

                            buyData(phone_number, data_amount, cost, valid_days)
                            db.commit()

                            print(end='\r')
                            print(end='\r')
                            time.sleep(1)
                            clear()
                            break

                        else:
                            invalid()

                elif ans == '3':
                    wait_and_count()
                    while True:
                        print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        phone_number = input('>>> ').strip()
                        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                        user = my_cur.execute(check_num, (phone_number))
                        if user:
                            data_amount = 200
                            cost = 150
                            valid_days = 30

                            buyData(phone_number, data_amount, cost, valid_days)
                            db.commit()

                            print(end='\r')
                            print(end='\r')
                            time.sleep(1)
                            clear()
                            break

                        else:
                            invalid()

                elif ans == '0':
                    social_bundles()

                else:
                    out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# Facebook
def facebook():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_black_bg}{brt_red}Facebook{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 250MB")
            time.sleep(1)
            print(f'0. back{end}{bold}{magenta}')
            time.sleep(1.5)
            ask = input("\t>>> ").strip()

            if ask == '1':
                wait_and_count()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 50
                        cost = 25

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

            elif ask == '2':
                wait_and_count()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 100
                        cost = 50
                        days = 7

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

            elif ask == '3':
                wait_and_count()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 250
                        cost = 100
                        days = 30

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

            elif ask == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# Instagram
def instagram():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_black_bg}{brt_cyan}Instagram{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. ₦100 for 250MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦250 for 1.5GB/3-days.")
            time.sleep(1)
            print(f'0. back{end}{bold}{magenta}')
            time.sleep(1.5)
            opt = input("\t>>> ").strip()

            if opt == '1':
                wait_and_count()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 250
                        cost = 100

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

            elif opt == '2':
                wait_and_count()
                while True:
                    print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    phone_number = input('>>> ').strip()
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 350
                        cost = 150
                        days = 2

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
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
                        data_amount = 1000
                        cost = 200

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
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
                        cost = 200
                        days = 3

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

            elif opt == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops Something went wrong: ', e)


# Tiktok
def tiktok():
    try:
        wait()
        while True:

            print()
            print(f"\t\t{brt_black_bg}{brt_blue}Tiktok{end}")
            print(f"{brt_black_bg}{brt_yellow}1. ₦100 for 200MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦200 for 1.5GB/3-days.")
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
                        data_amount = 200
                        cost = 100

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

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
                        data_amount = 350
                        cost = 150
                        days = 2

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

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
                        data_amount = 1000
                        cost = 200

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

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
                        data_amount = 1500
                        cost = 250
                        days = 3

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

            elif ans == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# All Social Media Bundles
def all_social_bundles():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_white_bg}{brt_white}All Social Bundles{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. Daily @ ₦50 for 150MB.")
            time.sleep(1)
            print("2. Weekly @ ₦100 for 350MB.")
            time.sleep(1)
            print("3. Monthly @ ₦250 for 1GB.")
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
                        data_amount = 150
                        cost = 50

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

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
                        data_amount = 350
                        cost = 100
                        days = 7

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

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
                        data_amount = 1000
                        cost = 250
                        days = 7

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        clear()
                        break

                    else:
                        invalid()

            elif ans == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# YouTube, Instagram and Tiktok
def yit():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_black_bg}{brt_red}Youtube,Instagram, and TikTok{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. Daily @ ₦100 for 350MB.")
            time.sleep(0.6)
            print(f'0.back{end}{bold}{magenta}')
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
                        data_amount = 150
                        cost = 50

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

            elif ans == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# Opera Mini and News
def operamini_and_news():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_black_bg}{brt_magenta}Opera Mini & News{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. ₦20/50MB/1day.")
            time.sleep(1)
            print("2. ₦50/100MB/7days.")
            time.sleep(1)
            print("3. ₦100/500MB/30days.")
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
                        data_amount = 50
                        cost = 20

                        buyData(phone_number, data_amount, cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

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
                        data_amount = 100
                        cost = 50
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
                        data_amount = 500
                        cost = 250
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

            elif ans == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# Social Mega Bundles
def social_mega_bundles():
    try:
        wait()
        while True:
            print()
            print(f"\t\t{brt_black_bg}{brt_blue}Social Mega Bundles{end}\n")
            print(f"{brt_black_bg}{brt_yellow}1. 750MB for ₦200 (3 days).")
            time.sleep(1)
            print("2. 1GB for N300 (7 days).")
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
                        data_amount = 750
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
                        cost = 300
                        days = 7
                        wait()

                        buyData(phone_number, data_amount, cost, days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()

            elif ans == '0':
                social_bundles()

            else:
                out()

    except Exception as e:
        print('Oops something went wrong: ', e)


# SOCIAL MEDIA BUNDLE


def social_bundles():
    from TelecomProject.test import main_menu
    wait()
    print()
    print(f'\t{brt_black_bg}{brt_blue}Social Bundles{end}')
    time.sleep(1)
    print_slowly(f"{brt_black_bg}{brt_yellow}1. Whatsapp")
    time.sleep(1)
    print_slowly("2. Facebook")
    time.sleep(1)
    print_slowly("3. Instagram")
    time.sleep(1)
    print_slowly("4. Tiktok")
    time.sleep(1)
    print_slowly("5. All Social Bundles")
    time.sleep(1)
    print_slowly("6. Youtube, Instagram, and Tiktok")
    time.sleep(1)
    print_slowly("7. Opera Mini & News")
    time.sleep(1)
    print_slowly("8. Social Mega Bundles")
    time.sleep(1.5)
    print_slowly(f'0. Back{end}{bold}{magenta}')
    time.sleep(1)
    ask = input("\t>>>").strip()

    if ask == '1':
        clear()
        print(end='\r')
        print(end='\r')
        whatsapp()
        time.sleep(1)
        exit()

    elif ask == '2':
        clear()
        print(end='\r')
        print(end='\r')
        facebook()
        time.sleep(1)
        exit()

    elif ask == '3':
        clear()
        print(end='\r')
        print(end='\r')
        instagram()
        time.sleep(1)
        exit()

    elif ask == '4':
        clear()
        print(end='\r')
        print(end='\r')
        tiktok()
        time.sleep(1)
        exit()

    elif ask == '5':
        clear()
        print(end='\r')
        print(end='\r')
        all_social_bundles()
        time.sleep(1)
        exit()

    elif ask == '6':
        clear()
        print(end='\r')
        print(end='\r')
        yit()
        time.sleep(1)
        exit()

    elif ask == '7':
        clear()
        print(end='\r')
        print(end='\r')
        operamini_and_news()
        time.sleep(1)
        exit()

    elif ask == '8':
        clear()
        print(end='\r')
        print(end='\r')
        social_mega_bundles()
        time.sleep(1)
        exit()

    elif ask == '0':
        main_menu()

    else:
        out()
        time.sleep(0.5)
        social_bundles()