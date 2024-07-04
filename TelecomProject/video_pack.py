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


# YouTube Video Packs
def youtube_video_packs():
    wait()
    while True:
        print()
        print(f" \t\t{brt_black_bg}{brt_green}YouTube Video Packs{end}\n")
        print(f"{brt_black_bg}{brt_yellow}1. 24 hour @ ₦100 for 800MB.")
        time.sleep(1)
        print("2. 24 hours @ ₦150 for 1.2GB.")
        time.sleep(1)
        print("3. 500MB at ₦50 24 hours.")
        time.sleep(1)
        print(f'0. back{end}{bold}{magenta}')
        time.sleep(1.5)
        ans = input("\t>>> ").strip()

        if ans == '1':
            clear()
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 800
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
                    time.sleep(3)
                    clear()

        elif ans == '2':
            clear()
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1200
                    cost = 150

                    buyData(phone_number, data_amount, cost)
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

        elif ans == '3':
            clear()
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
                    time.sleep(3)
                    clear()

        elif ans == '0':
            video_pack()

        else:
            out()


# YouTubeOnlyDataAccess
def youtube_only_data_access():
    wait()
    while True:
        print()
        print(f"\t\t{brt_black_bg}{brt_blue}Youtube Only and Data Access{end}\n")
        time.sleep(1)
        print(f"{brt_black_bg}{brt_yellow}1. ₦500 for Youtube Plus (1.5GB 2-Weeks Plan).")
        print(f'0. back{end}{bold}{magenta}')
        # time.sleep(1)
        # print("2. 2 hours plan for ₦100.")
        time.sleep(1.5)
        ans = input("\t>>> ").strip()

        if ans == '1':
            clear()
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
                    cost = 500
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
                    time.sleep(3)
                    clear()

        elif ans == '0':
            video_pack()

        else:
            out()
            break
    clear()


# Buffet Bundle
def buffet_bundle():
    wait()
    while True:
        print()
        print(f"\t\t{brt_black_bg}{brt_red}Buffet Bundle{end} \n")
        time.sleep(1)
        print(f"{brt_black_bg}{brt_yellow}1. 24 hours(1.3GB) plan for ₦200.")
        time.sleep(1)
        print("2. 24 hours(600MB) plan for ₦100.")
        time.sleep(1)
        print(f'0. back{end}{bold}{magenta}')
        time.sleep(1.5)
        ans = input("\t>>> ").strip()

        if ans == '1':
            clear()
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1300
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
                    time.sleep(3)
                    clear()

        elif ans == '2':
            clear()
            wait_and_count()
            while True:
                print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                phone_number = input('>>> ').strip()
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 600
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
                    time.sleep(3)
                    clear()

        elif ans == '0':
            video_pack()

        else:
            out()


# Video Packs
def video_pack():
    from TelecomProject.test import main_menu
    wait()
    while True:
        print()
        print(f"\t\t{brt_black_bg}{brt_magenta}Video Packs{end}\n")
        time.sleep(1)
        print_slowly(f"{brt_black_bg}{brt_yellow}1. Youtube video packs.")
        time.sleep(1)
        print_slowly("2. Buffet Bundle: This has a 12hrs & 24 hrs plan")
        time.sleep(1)
        print_slowly("3. 1GB(Youtube only) + 500MB (Data access)")
        time.sleep(1)
        print_slowly(f'0. Back{end}{bold}{magenta}')
        time.sleep(1.5)
        ans = input("\t>>> ").strip()

        if ans == '1':
            clear()
            youtube_video_packs()
            time.sleep(1)
            exit()
        elif ans == '2':
            clear()
            buffet_bundle()
            time.sleep(1)
            exit()

        elif ans == '3':
            clear()
            youtube_only_data_access()
            time.sleep(1)
            exit()

        elif ans == '0':
            main_menu()

        else:
            out()
