import datetime
import pymysql
import time
import sys
import os

# Initialize the db and my_cur variables
db = pymysql.connect(
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
    print('~' * 50)
    print('Invalid Phone number.')
    time.sleep(0.6)
    print('Service time out')


def out():
    time.sleep(0.8)
    print('~' * 50)
    print('Invalid Entry. Service time out')


def recharge():
    print('~' * 50)
    # Check user number
    phone_number = input('Enter phone number\n\t>>> ')
    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
    user = my_cur.execute(check_num, (phone_number))

    if user:
        print('~' * 50)
        amount = input('Enter amount to recharge\n\t>>> ')

        # Check if amount input is a numeric value
        if amount.isnumeric():
            amount = int(amount)
            sel_bal = 'SELECT Airtime_balance FROM Telecom_tbl WHERE Phone_number = %s'
            my_cur.execute(sel_bal, (phone_number,))
            result = my_cur.fetchone()

            if result is not None:
                current_airtime_bal = result[0]

                # Credit user
                new_airtime_bal = current_airtime_bal + amount

                # Query to db
                update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s WHERE Phone_number = %s'
                my_cur.execute(update_bal, (new_airtime_bal, phone_number))

                # Commit changes
                db.commit()

                print('~' * 50)
                print(f'The recharge of N{amount} was successful\nAcct.bal N{amount}')
            else:
                invalid()

        else:
            out()

    else:
        invalid()


def checkDataBal(phone_number):
    try:
        #Query to check and select data bal
        sel_bal = 'SELECT Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_bal, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            data_bal = result[0]

            if data_bal == 0:
                print('~' * 50)
                print('You have no active data bundle')
            else:
                print('~' * 50)
                print(f'Your data balance is {data_bal}MB')

        else:
            print('~' * 50)
            print('Error:No query returned')

    except Exception as e:
        print('~' * 50)
        print('An error occurred: ',e)


#db code for transaction
def buyData(phone_number, data_amount, cost, valid_days=1):
    # Calculate expiry date outside the loop
    expiry_date = datetime.date.today() + datetime.timedelta(days=valid_days)

    with db.cursor() as my_cur:
        try:
            while True:
                if data_amount >= 1000:
                    # Convert to gigabytes (GB) with one decimal place
                    bundle_size = f"{data_amount / 1000:.1f}GB"
                else:
                    # Keep in megabytes (MB)
                    bundle_size = f"{data_amount}MB"

                # query to select airtime bal
                sel_balance = 'SELECT Airtime_balance, Data_balance, Data_expires FROM Telecom_tbl WHERE Phone_number = %s'
                my_cur.execute(sel_balance, (phone_number,))
                result = my_cur.fetchone()

                if result is not None:
                    current_balance = result[0]
                    current_data_bal = result[1]
                    data_expire = result[2]

                    # Check if data has expired
                    if data_expire and data_expire < datetime.date.today():
                        print('~' * 50)
                        print('Your data has expired')
                        # Update data bal
                        update_bal = 'UPDATE Telecom_tbl SET Data_balance = 0 WHERE Phone_number = %s'
                        my_cur.execute(update_bal, (phone_number,))
                        db.commit()
                        break

                    if current_balance >= cost:
                        # Print message
                        wait()
                        print('~' * 50)
                        print(f"You have been credited with {bundle_size} @ ₦{cost} valid for {valid_days} day(s).")
                        time.sleep(3)
                        clear()

                        # Deduct from bal
                        new_balance = current_balance - cost

                        # Add to data bal
                        new_data_bal = current_data_bal + data_amount

                        try:
                            # Query to update bal and expiry date
                            update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s WHERE Phone_number = %s'
                            my_cur.execute(update_bal, (new_balance, new_data_bal, phone_number))

                            # Query to update Data_expires
                            update_expiry = 'UPDATE Telecom_tbl SET Data_expires = %s WHERE Phone_number = %s'
                            my_cur.execute(update_expiry, (expiry_date, phone_number))

                            # Commit changes
                            db.commit()
                            break

                        except Exception as e:
                            print('~' * 50)
                            print("An error occurred while updating data:", e)
                            db.rollback()  # Rollback changes if an error occurs

                    else:
                        wait()
                        print('~' * 50)
                        print('Insufficient Airtime balance.')
                        break

                else:
                    print('~' * 50)
                    print('Error: No query returned')
                    break

        except Exception as e:
            print('~' * 50)
            print("An error occurred:", e)


def buyDataTalk(phone_number, data_amount, cost, talk_time, valid_days=1):
    # Calculate expiry date outside the loop
    expiry_date = datetime.date.today() + datetime.timedelta(days=valid_days)

    with db.cursor() as my_cur:
        while True:
            if data_amount >= 1000:
                # Convert to gigabytes (GB) with one decimal place
                bundle_size = f"{data_amount / 1000:.1f}GB"
            else:
                # Keep in megabytes (MB)
                bundle_size = f"{data_amount}MB"

            # query to select airtime bal
            sel_balance = 'SELECT Airtime_balance,Data_balance,Talk_time,Data_expires from Telecom_tbl WHERE Phone_number =%s'
            my_cur.execute(sel_balance, (phone_number,))
            result = my_cur.fetchone()

            if result is not None:
                current_balance = result[0]
                current_data_bal = result[1]
                current_talk_bal = result[2] if len(result) > 2 else 0
                data_expire = result[3] if len(result) > 3 else 0

                # Check if data has expired
                if data_expire and data_expire < datetime.date.today():
                    print('~' * 50)
                    print('Your data has expired')

                    # Update data bal
                    update_bal = 'UPDATE Telecom_tbl SET Data_balance = 0,Talk_time = 0 WHERE Phone_number = %s'
                    my_cur.execute(update_bal, (phone_number,))
                    db.commit()
                    break

                if current_balance >= cost:

                    # Print message
                    wait()
                    print('~' * 50)
                    print(f"You have been credited with {bundle_size} and {talk_time}talktime @ ₦{cost} valid for {valid_days} day(s).")
                    time.sleep(3)
                    clear()

                    # Deduct from bal
                    new_balance = current_balance - cost

                    # Add to data bal
                    new_data_bal = current_data_bal + data_amount

                    # Add to talk bal
                    new_talk_bal = current_talk_bal + talk_time
                    try:
                        # Query to update bal
                        update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s,Talk_time = %s WHERE Phone_number = %s'
                        my_cur.execute(update_bal, (new_balance, new_data_bal,new_talk_bal, phone_number))

                        # Query to update Data_expires
                        update_expiry = 'UPDATE Telecom_tbl SET Data_expires = %s WHERE Phone_number = %s'
                        my_cur.execute(update_expiry, (expiry_date, phone_number))

                        # Commit change
                        db.commit()
                        break

                    except Exception as e:
                        print('~' * 50)
                        print("An error occurred while updating data:", e)
                        # db.rollback()  # Rollback changes if an error occurs

                else:
                    wait()
                    print('~' * 50)
                    print('Insufficient Airtime balance.')
                    break

            else:
                print('~' * 50)
                print('Error: No query returned')
                break

        print(end='\r')
        print(end='\r')
        clear()


def data_trans(sender_number,receiver_number,data_amount):
    try:
        with db.cursor() as my_cur:
            if data_amount >= 1000:
                # Convert to gigabytes (GB) with one decimal place
                bundle_size = f"{data_amount / 1000:.1f}GB"
            else:
                # Keep in megabytes (MB)
                bundle_size = f"{data_amount}MB"

            # Check if sender has sufficient data amount
            sel_sender_bal = 'SELECT Data_balance FROM Telecom_tbl WHERE Phone_number = %s'
            my_cur.execute(sel_sender_bal, (sender_number))
            result = my_cur.fetchone()

            if result is not None:
                sender_bal = result[0]

                if sender_bal >= 100:

                    if sender_bal >= data_amount:

                        # Deduct from sender bal
                        new_sender_bal = sender_bal - data_amount

                        # Query to update sender bal
                        update_bal = 'UPDATE Telecom_tbl SET Data_balance = %s WHERE Phone_number = %s '
                        my_cur.execute(update_bal,(new_sender_bal,sender_number))

                        # Add data to receiver's balance
                        sel_receiver_balance = 'SELECT Data_balance FROM Telecom_tbl WHERE Phone_number = %s'
                        my_cur.execute(sel_receiver_balance, (receiver_number,))
                        result = my_cur.fetchone()

                        if result is not None:
                            receiver_bal = result[0]

                            # Add to receiver bal
                            new_receiver_bal = receiver_bal + data_amount

                            # Update receiver's balance
                            update_receiver_bal = 'UPDATE Telecom_tbl SET Data_balance = %s WHERE Phone_number = %s'
                            my_cur.execute(update_receiver_bal, (new_receiver_bal, receiver_number))

                            # Commit changes
                            db.commit()

                            print('~' * 50)
                            print(f"Data transfer successful! {bundle_size} transferred from {sender_number} to {receiver_number}.")

                        else:
                            print('~' * 50)
                            print('No query returned')

                    else:
                        print('~' * 50)
                        print('Insufficient data balance for data transfer.')

                else:
                    print('~' * 50)
                    print('Airtime balance must be more than 100MB to continue this process.')

            else:
                print('~' * 50)
                print('No query returned')

    except Exception as e:
        print('~' * 50)
        print('An error occurred: ', e)


# Data plan
def data_plans_subscription():
    wait()
    print('~' * 50)
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
    print('~' * 50)
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
    print('~' * 50)
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
    print('~' * 50)
    print('\t\tWeekly Plan\n')
    print('1. N300 for 350MB')
    time.sleep(0.6)
    print('2. N500 for 700MB/7days')
    time.sleep(0.6)
    print('3. N600 for 1GB')
    time.sleep(0.6)
    print('4. N1000 for 1.5GB')
    time.sleep(0.6)
    print('~' * 50)
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
    print('~' * 50)
    print('\t\tMonthly Plan\n')
    print('1. N1000 for 1.2GB')
    time.sleep(0.6)
    print('2. N1200 for 1.5GB')
    time.sleep(0.6)
    print('3. N2000 for 4GB')
    time.sleep(0.6)
    print('4. N3000 for 8GB')
    time.sleep(0.6)
    print('~' * 50)
    option = input('\t> ')

    if option == '1':
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

    elif option == '2':
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

    elif option == '3':
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

    elif option == '4':
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
    print('~' * 50)
    print('\t\t2-3 Month Plan\n')
    print('1. N8000 for 30GB/60days')
    time.sleep(0.6)
    print('2. N20000 for 100GB/60days')
    time.sleep(0.6)
    print('3. N30000 for 160GB/60days')
    time.sleep(0.6)
    print('4. N50000 for 400GB/90days')
    time.sleep(0.6)
    print('~' * 50)
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
    print('~' * 50)
    print('\t\tAlways on Bundle\n')
    print('1. N60 for 200MB/24hrs')
    time.sleep(0.6)
    print('2. N120 for 450MB/7days')
    time.sleep(0.6)
    print('3. N3000 for 15GB/30days')
    time.sleep(0.6)
    print('4. N6000 for 45GB/30days')
    time.sleep(0.6)
    print('~' * 50)
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
    print('~' * 50)
    print('\t\tHot Deals Plan\n')
    print('1. N500-750MB +500 Talk time/14days')
    time.sleep(0.6)
    print('2. N1000-1.5GB +1000 Talk time/30days')
    time.sleep(0.6)
    print('3. N2000-4.5GB +2000 Talk time/30days')
    time.sleep(0.6)
    print('~' * 50)
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
    print('~' * 50)
    print('\t\tManage Data Plan\n')
    print('1. VIEW ACTIVE DATA BUNDLE')
    time.sleep(0.6)
    print('~' * 50)
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


# Data plan
def dataPlan():

    data_plans_subscription()

    print('~' * 50)
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
        # cod.main_menu()
        print()

    else:
        out()


# SOCIAL BUNDLE CODE
def whatsapp():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tWhatsapp\n")
            print("1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 200MB")
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")
            if ans.isnumeric():
                ans = ans
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


# Facebook
def facebook():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tFacebook\n")
            print("1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 250MB")
            time.sleep(1.5)
            print('~' * 50)
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


# Instagram
def instagram():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tInstagram\n")
            print("1. ₦100 for 250MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦250 for 1.5GB/3-days.")
            time.sleep(1.5)
            print('~' * 50)
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


# Tiktok
def tiktok():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tTiktok\n")
            print("1. ₦100 for 200MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦200 for 1.5GB/3-days.")
            time.sleep(1.5)
            print('~' * 50)
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


# All Social Media Bundles
def all_social_bundles():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tAll Social Bundles\n")
            print("1. Daily @ ₦50 for 150MB.")
            time.sleep(1)
            print("2. Weekly @ ₦100 for 350MB.")
            time.sleep(1)
            print("3. Monthly @ ₦250 for 1GB.")
            time.sleep(1.5)
            print('~' * 50)
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


# YouTube, Instagram and Tiktok
def yit():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tYoutube,Instagram, and TikTok\n")
            print("1. Daily @ ₦100 for 350MB.")
            time.sleep(1.5)
            print('~' * 50)
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


# Opera Mini and News
def operamini_and_news():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tOpera Mini & News\n")
            print("1. ₦20/50MB/1day.")
            time.sleep(1)
            print("2. ₦50/100MB/7days.")
            time.sleep(1)
            print("3. ₦100/500MB/30days.")
            time.sleep(1.5)
            print('~' * 50)
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
                out()
                break

        clear()
        print(end='\r')
        print(end='\r')

    except ValueError:
        print('Oops something went wrong.')


# Social Mega Bundles
def social_mega_bundles():
    try:
        wait()
        while True:
            print('~' * 50)
            print("\t\tSocial Mega Bundles\n")
            print("1. 750MB for ₦200 (3 days).")
            time.sleep(1)
            print("2. 1GB for N300 (7 days).")
            time.sleep(1.5)
            print('~' * 50)
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
                out()
                break
        clear()
        print(end='\r')
        print(end='\r')

    except Exception as e:
        print('Oops something went wrong: ',e)


# SOCIAL MEDIA BUNDLE
wait()


def social_bundles():
    print('~' * 50)
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
    print('~' * 50)
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
        out()
        time.sleep(0.5)


# Transfer data
def data_transfer():
    try:
        wait()
        print('~' * 50)
        sender_number = input('Please enter your phone number to continue\n\t> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (sender_number))

        if user:
            wait()
            print('~' * 50)
            receiver_number = input('Enter receiver phone number\n\t> ')
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (receiver_number))

            if user:
                wait()
                print('~'*50)
                data_amount = input('Enter data amount \n\t> ')
                print('~' * 50)

                if data_amount.isnumeric():
                    data_amount = int(data_amount)

                    limit = 2000
                    if data_amount <= int(limit):

                        wait_and_count()
                        data_trans(sender_number,receiver_number,data_amount)
                        db.commit()

                        print(end='\r')
                        print(end='\r')
                        time.sleep(1)
                        clear()

                    else:
                        print("Can't make transfer more than 2000MB ")
                        time.sleep(0.7)
                        print('Service time out')

                else:
                    out()

            else:
                print('~' * 50)
                invalid()

        else:
            print('~' * 50)
            invalid()

    except Exception as e:
        print('~' * 50)
        print('An error occurred: ', e)


# GIFT DATA
def gift_data():
    print('~' * 50)
    print('\tGift Data')
    time.sleep(0.6)
    print('1.Transfer from data balance')
    time.sleep(0.6)
    print('2.Buy for a friend')
    time.sleep(0.6)
    print('~' * 50)
    opt = input('\t> ')

    if opt == '1':
        data_transfer()

    elif opt == '2':
        print()


# YouTube Video Packs
def youtube_video_packs():
    wait()
    while True:
        print('~' * 50)
        print("  YouTube Video Packs\n")
        print("1. 24 hour @ ₦100 for 800MB.")
        time.sleep(1)
        print("2. 24 hours @ ₦150 for 1.2GB.")
        time.sleep(1)
        print("3. 500MB at ₦50 24 hours.")
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            clear()
            wait_and_count()
            phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                break

        elif ans == '2':
            clear()
            wait_and_count()
            phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                break

        elif ans == '3':
            clear()
            wait_and_count()
            phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                break

        else:
            out()
            break
    clear()


# YouTubeOnlyDataAccess
def youtube_only_data_access():
    wait()
    while True:
        print('~' * 50)
        print("  Youtube Only and Data Access \n")
        time.sleep(1)
        print("1. ₦500 for Youtube Plus (1.5GB 2-Weeks Plan).")
        # time.sleep(1)
        # print("2. 2 hours plan for ₦100.")
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            clear()
            wait_and_count()
            phone_number = input('Please enter phone number again to continue\n\t>>> ')
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (phone_number))

            # check if user is in db
            if user:
                data_amount = 1500
                cost = 500
                days = 14

                buyData(phone_number, data_amount, cost,days)
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
                break

        else:
            out()
            break
    clear()


# Buffet Bundle
def buffet_bundle():
    wait()
    while True:
        print('~' * 50)
        print("\t Buffet Bundle \n")
        time.sleep(1)
        print("1. 24 hours(1.3GB) plan for ₦200.")
        time.sleep(1)
        print("2. 24 hours(600MB) plan for ₦100.")
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            clear()
            wait_and_count()
            phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                break

        elif ans == '2':
            clear()
            wait_and_count()
            phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                break
        else:
            out()
            break
    clear()


# Video Packs
def video_pack():
    wait()
    while True:
        print('~' * 50)
        print("\t Video Packs \n")
        time.sleep(1)
        print("1. Youtube video packs.")
        time.sleep(1)
        print("2. Buffet Bundle: This has a 12hrs & 24 hrs plan")
        time.sleep(1)
        print("3. 1GB(Youtube only) + 500MB (Data access)")
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

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

        else:
            out()
            break


# menu function
def main_menu():
    print('~' * 50)
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
    print('7. Recharge Airtime')
    time.sleep(1)  # Wait for 1 second
    print('8. Chat with Zigi')
    print('~' * 50)
    menu = input('\t>>> ')

    if menu == '1':
        dataPlan()

    elif menu == '2':
        social_bundles()

    elif menu == '3':
        print('f')

    elif menu == '4':
        print('account statement')

    elif menu == '5':
        video_pack()

    elif menu == '6':
        gift_data()

    elif menu == '7':
        recharge()

    elif menu == '8':
        print()

    else:
        print('Invalid Entry\nTry again\n')
        main_menu()


# ussd function
def ussd_code():
    print('~' * 50)
    ussd = input('Enter ussd\n\t>>> ')
    if ussd == '*312#':
        main_menu()

    else:
        print('~' * 50)
        print('Invalid ussd\nTry again\n')
        ussd_code()

# ussd_code()




