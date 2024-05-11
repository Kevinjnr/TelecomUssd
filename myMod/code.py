import pymysql as sql
import time
import os
import sys

db = sql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()

phone_number = ''
airtime_balance = ''

def clear():
    if os.name == 'nt':
        os.system('cls')
    sys.stdout.flush()

def wait():
    sys.stdout.flush()
    print("Please wait..", end='')
    time.sleep(2)
    clear()
    print(end='\r')
    print(end='\r')

#SOCIAL BUNDLE CODE
#Whatsapp
def wait_and_count():
    for i in range(3,0,-1):
        sys.stdout.flush()
        print(f"Processing...{i}sec", end='')
        time.sleep(1)
        print(end='\r')
    clear()
    print(end='\r')
    print(end='\r')

def invalid():
    print('Invalid Phone number.')

def out():
    print('Invalid Entry. Service time out')

def checkDataBal(phone_number):
    try:
        #Query to check and select data bal
        sel_bal = 'SELECT Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_bal, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            data_bal = result[0]

            if data_bal == 0:
                print('You have no active data bundle')
            else:
                print(f'Your data balance is {data_bal}MB')

        else:
            print('Error:No query returned')

    except Exception:
        print('Error in code')

#db code for transaction
def buyData(phone_number,data_amount,cost,valid_days=1):
    while True:
        if data_amount >= 1000:
            # Convert to gigabytes (GB) with one decimal place
            bundle_size = f"{data_amount / 1000:.1f}GB"
        else:
            # Keep in megabytes (MB)
            bundle_size = f"{data_amount}MB"

        # query to select airtime bal
        sel_balance = 'SELECT Airtime_balance,Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_balance, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            current_balance = result[0]
            current_data_bal = result[1]
            if current_balance >= cost:

                # Print message
                wait()
                print(f"You have been credited with {bundle_size} @ ₦{cost} valid for {valid_days} day(s).")
                time.sleep(3)
                clear()

                # Deduct from bal
                new_balance = current_balance - cost

                # Add to data bal
                new_data_bal = current_data_bal + data_amount

                # Query to update bal
                update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s WHERE Phone_number = %s'
                my_cur.execute(update_bal, (new_balance, new_data_bal, phone_number))

                # Commit change
                db.commit()
                break

            else:
                wait()
                print('Insufficient Airtime balance.')
                break

        else:
            print('Error: No query returned')
            break

    print(end='\r')
    print(end='\r')
    clear()


def buyDataTalk(phone_number, data_amount, cost, talk_time, valid_days=1):
    while True:
        if data_amount >= 1000:
            # Convert to gigabytes (GB) with one decimal place
            bundle_size = f"{data_amount / 1000:.1f}GB"
        else:
            # Keep in megabytes (MB)
            bundle_size = f"{data_amount}MB"

        # query to select airtime bal
        sel_balance = 'SELECT Airtime_balance,Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_balance, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            current_balance = result[0]
            current_data_bal = result[1]
            current_talk_bal = result[2] if len(result) > 2 else 0
            if current_balance >= cost:

                # Print message
                wait()
                print(f"You have been credited with {bundle_size} and {talk_time}talktime @ ₦{cost} valid for {valid_days} day(s).")
                time.sleep(3)
                clear()

                # Deduct from bal
                new_balance = current_balance - cost

                # Add to data bal
                new_data_bal = current_data_bal + data_amount

                # Add to talk bal
                new_talk_bal = current_talk_bal + talk_time

                # Query to update bal
                update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s,Talk_time = %s WHERE Phone_number = %s'
                my_cur.execute(update_bal, (new_balance, new_data_bal,new_talk_bal, phone_number))

                # Commit change
                db.commit()
                break

            else:
                wait()
                print('Insufficient Airtime balance.')
                break

        else:
            print('Error: No query returned')
            break

    print(end='\r')
    print(end='\r')
    clear()


#Data plan
def data_plans_subcripton():
    wait()
    print(' BUY DATA PLANS')
    time.sleep(0.6)
    print('1. Daily Plan')
    time.sleep(0.6)
    print('2. Weekly Plan')
    time.sleep(0.6)
    print('3. Monthly Plan')
    time.sleep(0.6)
    print('4. 2-3Month Plan ')
    time.sleep(0.6)
    print('5. Always On Plan')
    time.sleep(0.6)
    print('6. Hot Deals')
    time.sleep(0.6)
    print('7. Manage Data')
    time.sleep(0.6)
    print('0. Back')

def daily_plan():
    wait()
    print('\t\tDaily Plan\n')
    print('1. 100MB for N100')
    time.sleep(0.6)
    print('2. 200MB for N200')
    time.sleep(0.6)
    print('3. 350MB for N300')
    time.sleep(0.6)
    print('4. 1.5GB for N500')
    time.sleep(0.6)
    print('5. 2GB for N600')
    time.sleep(0.6)
    opt = input('\t> ')

    if opt == '1':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))
        if user:
            data_amount = 100
            cost = 100

            buyData(phone_number, data_amount, cost)
            db.commit()

            print(end='\r')
            print(end='\r')
            time.sleep(1)
            clear()

        else:
            invalid()

    elif opt == '2':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif opt == '3':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif opt == '4':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif opt == '5':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    else:
        out()

def weekly_plan():
    wait()
    print('\t\tWeekly Plan\n')
    print('1. N300 for 350MB')
    time.sleep(0.6)
    print('2. N500 for 700MB/7days')
    time.sleep(0.6)
    print('3. N600 for 1GB')
    time.sleep(0.6)
    print('4. N1000 for 1.5GB')
    time.sleep(0.6)
    option = input('\t> ')

    if option == '1':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))
        if user:
            data_amount = 350
            cost = 300
            days = 7

            buyData(phone_number, data_amount, cost,days)
            db.commit()

            print(end='\r')
            print(end='\r')
            time.sleep(1)
            clear()

        else:
            invalid()

    elif option == '2':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '3':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '4':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    else:
        out()

def monthly_plan():
    wait()
    print('\t\tMonthly Plan\n')
    print('1. N1000 for 1.2GB')
    time.sleep(0.6)
    print('2. N1200 for 1.5GB')
    time.sleep(0.6)
    print('3. N2000 for 4GB')
    time.sleep(0.6)
    print('4. N3000 for 8GB')
    time.sleep(0.6)
    option = input('\t> ')

    if option == 1:
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

    elif option == 2:
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

    elif option == 3:
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

    elif option == 4:
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

    else:
        out()

def _2_3month_plan():
    wait()
    print('\t\t2-3 Month Plan\n')
    print('1. N8000 for 30GB/60days')
    time.sleep(0.6)
    print('2. N20000 for 100GB/60days')
    time.sleep(0.6)
    print('3. N30000 for 160GB/60days')
    time.sleep(0.6)
    print('4. N50000 for 400GB/90days')
    time.sleep(0.6)
    option = input('\t> ')

    if option == '1':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '2':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '3':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '4':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    else:
        out()

def always_on_plan():
    wait()
    print('\t\tAlways on Bundle\n')
    print('1. N60 for 200MB/24hrs')
    time.sleep(0.6)
    print('2. N120 for 450MB/7days')
    time.sleep(0.6)
    print('3. N3000 for 15GB/30days')
    time.sleep(0.6)
    print('4. N6000 for 45GB/30days')
    time.sleep(0.6)
    option = input('\t> ')

    if option == '1':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '2':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '3':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    elif option == '4':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            invalid()

    else:
        print('Invalid Entry, Please try again')

def hot_deals_plan():
    wait()
    print('\t\tHot Deals Plan\n')
    print('1. N500-750MB +500 Talk time/14days')
    time.sleep(0.6)
    print('2. N1000-1.5GB +1000 Talk time/30days')
    time.sleep(0.6)
    print('3. N2000-4.5GB +2000 Talk time/30days')
    time.sleep(0.6)
    option = input('\t> ')

    if option == '1':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))
        if user:
            data_amount = 750
            cost = 500
            talk_time = 500
            days = 14

            buyDataTalk(phone_number, data_amount, cost,talk_time,days)
            db.commit()

            print(end='\r')
            print(end='\r')
            time.sleep(1)
            clear()

        else:
            invalid()

    elif option == '2':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

    else:
        out()

def manage_data_plan():
    wait()
    print('\t\tManage Data Plan\n')
    print('1. VIEW ACTIVE DATA BUNDLE')
    time.sleep(0.6)
    option = input('\t> ')

    if option == '1':
        wait_and_count()
        phone_number = input('Please enter phone number again to continue\n\t>>> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))
        if user:
            checkDataBal(phone_number)

            print(end='\r')
            print(end='\r')
            time.sleep(1)
            clear()

        else:
            invalid()

    else:
        out()

#Data plan
def dataPlan():

    data_plans_subcripton()

    user_result = input('\t> ')
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
        pass

    else:
        out()


def whatsapp():
    try:
        wait()
        while True:
            print("\t\tWhatsapp\n")
            print("1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 200MB")
            time.sleep(1.5)
            ans = input("\t> ")
            if ans.isnumeric():
                ans = ans
                if ans == '1' :
                    wait_and_count()
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 50
                        cost = 25

                        buyData(phone_number,data_amount,cost)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()
                        break

                elif ans == '2':
                    wait_and_count()
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 100
                        cost = 50
                        valid_days = 7

                        buyData(phone_number,data_amount, cost, valid_days)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()
                        break

                    else:
                        invalid()
                        break

                elif ans == '3':
                    wait_and_count()
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                        break

                else:
                    print("Invalid character. Please try again")
                    whatsapp()

        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        print('Oops something went wrong')
#Facebook
def facebook():
    try:
        wait()
        while True:
            print("\t\tFacebook\n")
            print("1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 250MB")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 50
                    cost = 25

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '2':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 100
                    cost = 50
                    days = 7

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '3':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 250
                    cost = 100
                    days = 30

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")

        clear()
        print(end='\r')
        print(end='\r')
    except ValueError:
        print('Oops something went wrong')
#Instagram
def instagram():
    try:
        wait()
        while True:
            print("\t\tInstagram\n")
            print("1. ₦100 for 250MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦250 for 1.5GB/3-days.")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 250
                    cost = 100

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '2':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 350
                    cost = 150
                    days = 2

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '3':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1000
                    cost = 200

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '4':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
                    data_amount = 1500
                    cost = 200
                    days = 3

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")
        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        return 'Oops Something went wrong'

#Tiktok
def tiktok():
    try:
        wait()
        while True:
            print("\t\tTiktok\n")
            print("1. ₦100 for 200MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦200 for 1.5GB/3-days.")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                #check if user is in db
                if user:
                    data_amount = 200
                    cost = 100

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '2':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 350
                    cost = 150
                    days = 2

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '3':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1000
                    cost = 200

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '4':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1500
                    cost = 250
                    days = 3

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")
        clear()
        print(end='\r')
        print(end='\r')
    except ValueError:
        return 'Oops something went wrong'

#All Social Media Bundles
def all_social_bundles():
    try:
        wait()
        while True:
            print("\t\tAll Social Bundles\n")
            print("1. Daily @ ₦50 for 150MB.")
            time.sleep(1)
            print("2. Weekly @ ₦100 for 350MB.")
            time.sleep(1)
            print("3. Monthly @ ₦250 for 1GB.")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 150
                    cost = 50

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '2':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 350
                    cost = 100
                    days = 7

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '3':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1000
                    cost = 250
                    days = 7

                    buyData(phone_number,data_amount,cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")
        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        print('Oops something went wrong')

#YouTube, Instagram and Tiktok
def yit():
    try:
        wait()
        while True:
            print("\t\tYoutube,Instagram, and TikTok\n")
            print("1. Daily @ ₦100 for 350MB.")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 150
                    cost = 50

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")
        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        print('Oops something went wrong')

#Opera Mini and News
def operamini_and_news():
    try:
        wait()
        while True:
            print("\t\tOpera Mini & News\n")
            print("1. ₦20/50MB/1day.")
            time.sleep(1)
            print("2. ₦50/100MB/7days.")
            time.sleep(1)
            print("3. ₦100/500MB/30days.")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 50
                    cost = 20

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '2':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 100
                    cost = 50
                    days = 7

                    buyData(phone_number, data_amount, cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '3':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 500
                    cost = 250
                    days = 30

                    buyData(phone_number, data_amount, cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")

        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        print('Oops something went wrong.')

#Social Mega Bundles
def social_mega_bundles():
    try:
        wait()
        while True:
            print("\t\tSocial Mega Bundles\n")
            print("1. 750MB for ₦200 (3 days).")
            time.sleep(1)
            print("2. 1GB for N300 (7 days).")
            time.sleep(1.5)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 750
                    cost = 200
                    days = 3

                    buyData(phone_number, data_amount, cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == '2':
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1000
                    cost = 300
                    days = 7
                    wait()

                    buyData(phone_number, data_amount, cost,days)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    time.sleep(1)
                    clear()
                    break

                else:
                    invalid()
                    break

            else:
                print("Invalid character")
        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        print('Oops something went wrong')

# SOCIAL MEDIA BUNDLE
wait()
def socialBundles():
        print('Social Bundles')
        time.sleep(1)
        print("1. Whatsapp")
        time.sleep(1)
        print("2. Facebook")
        time.sleep(1)
        print("3. Instagram")
        time.sleep(1)
        print("4. Tiktok")
        time.sleep(1)
        print("5. All Social Bundles")
        time.sleep(1)
        print("6. Youtube, Instagram, and Tiktok")
        time.sleep(1)
        print("7. Opera Mini & News")
        time.sleep(1)
        print("8. Social Mega Bundles")
        time.sleep(1.5)
        ask = input("\t> ")

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

        else:
            print('Invalid entry. Please try again')
            time.sleep(0.5)
            socialBundles()

## menu function
def main_menu():
    print("Welcome to our USSD Service.")
    time.sleep(1)  # Wait for 1 second
    print('1. Data Plan')
    time.sleep(1)  # Wait for 1 second
    print('2. Social Bundles')
    time.sleep(1)  # Wait for 1 second
    print('3. Borrow Credit')
    time.sleep(1)  # Wait for 1 second
    print("4. Roaming\\int'l")
    time.sleep(1)  # Wait for 1 second
    print('5. Video Pack')
    time.sleep(1)  # Wait for 1 second
    print('6. Gift data')
    time.sleep(1)  # Wait for 1 second
    print('7. Chat with Zigi')

    menu = input('\t>>> ')

    if menu == '1':
        dataPlan()

    elif menu == '2':
        socialBundles()

    elif menu == '3':
        print('f')

    elif menu == '4':
        print('account statement')

    else:
        print('Invalid Entry\nTry again\n')
        main_menu()


## ussd function
def ussd_code():
    ussd = input('Enter ussd\n\t>>> ')
    if ussd == '*312#':
        main_menu()

    else:
        print('Invalid ussd\nTry again\n')

        ussd_code()
ussd_code()





