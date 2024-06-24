import pymysql
import time
import sys
import os
import pyttsx3
import datetime
from decimal import Decimal

engine = pyttsx3.init()

# Initialize the db and my_cur variables
db = pymysql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()


# phone_number = ''
# airtime_balance = ''


def clear():
    if os.name == 'nt':
        os.system('cls')
    sys.stdout.flush()


def wait():
    sys.stdout.flush()
    engine.say("Please wait..")
    engine.runAndWait()
    print("Please wait..", end='')
    time.sleep(2)
    clear()
    print(end='\r')
    print(end='\r')


# Whatsapp
def wait_and_count():
    for i in range(3, 0, -1):
        # sys.stdout.flush()
        # engine.say("Processing..:")
        # engine.runAndWait()
        print(f"Processing...{i}sec", end='')
        time.sleep(1)
        print(end='\r')
    clear()
    print(end='\r')
    print(end='\r')


def return_menu():
    print()
    print()
    time.sleep(1)
    print_slowly('\033[31;1;3mPress * to return to main menu\033[0m')
    time.sleep(0.7)
    print_slowly('\033[31;1;3mPress # to end this process\033[0m')
    print('~' * 50)
    opt = input('\t> ')

    if opt == '*':
        wait()
        main_menu()

    elif opt == '#':
        time.sleep(1)
        print_slowly('\033[34;1;3mProcess is about to end\033[0m')
        wait()
        wait_and_count()
        print_slowly('\033[34;1;3mThank you for using our service.\033[0m')

    else:
        out()
        time.sleep(0.5)
        return_menu()


def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)  # Print without newline and flush the output
        time.sleep(0.05)  # Adjust the delay (in seconds) as desired
    print()  # Print a newline at the end


def invalid():
    print('~' * 50)
    engine.say("Invalid phone number")
    engine.runAndWait()
    print('Invalid Phone number.')
    time.sleep(0.6)
    engine.say("Please try again")
    engine.runAndWait()
    print('Please try again')
    print('~' * 50)
    print()


def out():
    time.sleep(0.8)
    print('~' * 50)
    engine.say("invalid entry. Please try again")
    engine.runAndWait()
    print('Invalid Entry. Please try again')
    print()


def recharge():
    try:
        print('~' * 50)
        print()
        print('\033[34;1;3mRecharge number \033[0m')
        # Check user number
        engine.say("Enter phone number")
        engine.runAndWait()
        phone_number = input('\033[1mEnter phone number\033[0m\n\t>>> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))

        if user:
            print('~' * 50)
            while True:
                print()
                engine.say("Enter amount to recharge")
                engine.runAndWait()
                amount = input('\033[1mEnter amount to recharge\n\t>>> ')

                # Check if amount input is a numeric value
                if amount.isnumeric():
                    amount = int(amount)

                    # Check if amount input is a numeric value
                    if amount >= 30:

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

                            wait_and_count()
                            print('~' * 50)
                            print()
                            engine.say(f"The recharge of {amount}naira was successful. Account balance: {amount}naira")
                            engine.runAndWait()
                            print_slowly(
                                f'\033[32;1;3mThe recharge of N{amount}.00 was successful\nAcct.bal N{amount}.00\033[0m')
                            with open('sms.txt', 'w', encoding='utf-8') as fh:
                                fh.write(
                                    f'Account recharge of N{amount}.00 was successful. Get 1.5GB at N500.\nDial *312*1# to buy data bundle ')

                            sel_bal = 'SELECT Airtime_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
                            my_cur.execute(sel_bal, (phone_number,))
                            result = my_cur.fetchone()

                            if result is not None:
                                borrow_bal = result[0]

                                if borrow_bal != 0:
                                    rate = Decimal('0.15')
                                    interest = rate * Decimal(borrow_bal)
                                    new_bal = new_airtime_bal - borrow_bal - interest

                                    update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s,Airtime_borrowed_balance=0 WHERE Phone_number = %s'
                                    my_cur.execute(update_bal, (new_bal, phone_number))

                                    db.commit()

                                    time.sleep(1)
                                    print()
                                    engine.say(f"{borrow_bal}naira was deducted from account")
                                    engine.runAndWait()
                                    print_slowly(f'\033[1mN{borrow_bal}.00 deducted from account')
                                    with open('sms.txt', 'w', encoding='utf-8') as fh:
                                        fh.write(
                                            f'N{borrow_bal}.00 deducted was from account. \nnew acct.balN{new_bal}.00')

                                    break

                                else:
                                    pass
                                    break

                            else:
                                print('~' * 50)
                                time.sleep(0.6)
                                engine.say('no query returned')
                                engine.runAndWait()
                                print('No query returned')

                        else:
                            invalid()


                    else:
                        print('~' * 50)
                        time.sleep(0.8)
                        engine.say(f"amount must be more than 30 naira")
                        engine.runAndWait()
                        print('Amount must be more than N30')

                else:
                    out()

            return_menu()

        else:
            invalid()
            recharge()

    except Exception as e:
        engine.say(f"An error occurred")
        engine.runAndWait()
        print('An error occurred: ', e)


# Check data bal
def checkDataBal(phone_number):
    try:
        # Query to check and select data bal
        sel_bal = 'SELECT Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_bal, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            data_bal = result[0]

            if data_bal == 0:
                print('~' * 50)
                engine.say(f"you have no active data bundle")
                engine.runAndWait()
                print('You have no active data bundle')
                with open('sms.txt', 'w', encoding='utf-8') as fh:
                    fh.write(
                        f"Dear customer, you don't have any active data bundle.\nPlease dial *312*1# to buy another bundle.")

                return_menu()

            else:
                print('~' * 50)
                print()
                engine.say(f"your data balance is {data_bal}mb")
                engine.runAndWait()
                print_slowly(f'\033[1mYour data balance is {data_bal}MB')
                with open('sms.txt', 'w', encoding='utf-8') as fh:
                    fh.write(f"Your data balance: {data_bal}MB.\nGet 1.5GB @ N200 Tiktok, dial *312*2#.")

                return_menu()

        else:
            print('~' * 50)
            engine.say(f"No query returned")
            engine.runAndWait()
            print('Error:No query returned')
            return_menu()

    except Exception as e:
        print('~' * 50)
        engine.say(f"an error occurred")
        engine.runAndWait()
        print('An error occurred: ', e)


# db code for transaction
def buyData(phone_number, data_amount=0, cost=0, valid_days=1):
    # Calculate expiry date outside the loop
    expiry_date = datetime.date.today() + datetime.timedelta(days=valid_days)
    expiry_date_time = datetime.datetime.now() + datetime.timedelta(days=valid_days)

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
                        engine.say(f"your data has expired")
                        engine.runAndWait()
                        print('Your data has expired')
                        # Update data bal
                        update_bal = 'UPDATE Telecom_tbl SET Data_balance = 0 WHERE Phone_number = %s'
                        my_cur.execute(update_bal, (phone_number,))
                        db.commit()
                        break

                    if current_balance >= cost:
                        # Print message
                        wait_and_count()
                        print('~' * 50)
                        engine.say(
                            f"You have been credited with {bundle_size} for {cost}naira valid for {valid_days} days.")
                        engine.runAndWait()
                        print_slowly(
                            f"\033[1mYou have been credited with {bundle_size} @ ₦{cost} valid for {valid_days} day(s).")
                        time.sleep(3)

                        with open('sms.txt', 'w', encoding='utf-8') as fh:
                            fh.write(
                                f'Activation of {bundle_size} bundle for {valid_days}day(s) @ ₦{cost} was successful\nand expiires at {expiry_date_time} ')

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

                            sel_bal = 'SELECT Data_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
                            my_cur.execute(sel_bal, (phone_number,))
                            result = my_cur.fetchone()

                            if result is not None:
                                borrow_bal = result[0]

                                if borrow_bal != 0:
                                    rate = Decimal('0.15')
                                    interest = rate * Decimal(borrow_bal)
                                    new_bal = new_data_bal - borrow_bal - interest

                                    update_bal = 'UPDATE Telecom_tbl SET Data_balance = %s,Data_borrowed_balance=0 WHERE Phone_number = %s'
                                    my_cur.execute(update_bal, (new_bal, phone_number))

                                    db.commit()

                                    print('~' * 50)
                                    print()
                                    engine.say(f"{borrow_bal}mb was deducted from your account")
                                    engine.runAndWait()
                                    print_slowly(f'\033[1m{borrow_bal}MB was deducted from your account')
                                    with open('sms.txt', 'w', encoding='utf-8') as fh:
                                        fh.write(f'N{borrow_bal}MB deducted from data bal. \nnew data.balN{new_bal}MB')

                                    break

                                else:
                                    pass
                                    break

                            else:
                                print('~' * 50)
                                time.sleep(0.6)
                                engine.say(f"no query returned")
                                engine.runAndWait()
                                print('No query returned')
                                break

                        except Exception as e:
                            print('~' * 50)
                            engine.say(f"an error occurred while updating data")
                            engine.runAndWait()
                            print("An error occurred while updating data:", e)
                            db.rollback()  # Rollback changes if an error occurs

                    else:
                        wait()
                        print('~' * 50)
                        engine.say(f"insufficient airtime balance")
                        engine.runAndWait()
                        print('\033[1mInsufficient Airtime balance.')
                        return_menu()

                else:
                    print('~' * 50)
                    engine.say(f"no query returned")
                    engine.runAndWait()
                    print('Error: No query returned')
                    break

            return_menu()

        except Exception as e:
            print('~' * 50)
            engine.say(f"an error occurred")
            engine.runAndWait()
            print("An error occurred:", e)


def buyDataTalk(phone_number, data_amount=0, cost=0, talk_time=0, valid_days=1):
    # Calculate expiry date outside the loop
    expiry_date = datetime.date.today() + datetime.timedelta(days=valid_days)
    expiry_date_time = datetime.datetime.now() + datetime.timedelta(days=valid_days)

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
                        wait_and_count()
                        print('~' * 50)
                        print()
                        engine.say(
                            f'you have been credited with {bundle_size}and {talk_time} talktime for {cost}naira, valid for {valid_days} days.')
                        engine.runAndWait()
                        print_slowly(
                            f"\033[1;3mYou have been credited with {bundle_size}+{talk_time}talktime @ ₦{cost} valid for {valid_days} day(s).")
                        time.sleep(3)
                        clear()
                        with open('sms.txt', 'w', encoding='utf-8') as fh:
                            fh.write(
                                f'Activation of {bundle_size}+{talk_time}talktime bundle for {valid_days}day(s) @ ₦{cost} was successful\nand expires at {expiry_date_time} ')

                        # Deduct from bal
                        new_balance = current_balance - cost

                        # Add to data bal
                        new_data_bal = current_data_bal + data_amount

                        # Add to talk bal
                        new_talk_bal = current_talk_bal + talk_time
                        try:
                            # Query to update bal
                            update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s,Talk_time = %s WHERE Phone_number = %s'
                            my_cur.execute(update_bal, (new_balance, new_data_bal, new_talk_bal, phone_number))

                            # Query to update Data_expires
                            update_expiry = 'UPDATE Telecom_tbl SET Data_expires = %s WHERE Phone_number = %s'
                            my_cur.execute(update_expiry, (expiry_date, phone_number))

                            # Commit change
                            db.commit()

                            sel_bal = 'SELECT Data_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
                            my_cur.execute(sel_bal, (phone_number,))
                            result = my_cur.fetchone()

                            if result is not None:
                                borrow_bal = result[0]

                                if borrow_bal != 0:
                                    rate = Decimal('0.15')
                                    interest = rate * Decimal(borrow_bal)
                                    new_bal = new_data_bal - borrow_bal - interest

                                    update_bal = 'UPDATE Telecom_tbl SET Data_balance = %s,Data_borrowed_balance=0 WHERE Phone_number = %s'
                                    my_cur.execute(update_bal, (new_bal, phone_number))

                                    db.commit()

                                    print('~' * 50)
                                    print()

                                    print(f'\033[1;3m{borrow_bal}MB deducted from account')
                                    break

                                else:
                                    pass
                                    break

                            else:
                                print('~' * 50)
                                time.sleep(0.6)
                                print('No query returned')


                        except Exception as e:
                            print('~' * 50)
                            print("An error occurred while updating data:", e)
                            # db.rollback()  # Rollback changes if an error occurs

                    else:
                        wait()
                        print('~' * 50)
                        print('Insufficient Airtime balance.')


                else:
                    print('~' * 50)
                    print('Error: No query returned')
                    break

            return_menu()

        except Exception as e:
            print('Error', e)

        print(end='\r')
        print(end='\r')
        clear()


# Data transfer code
def data_trans(sender_number, receiver_number, data_amount=0):
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
                        my_cur.execute(update_bal, (new_sender_bal, sender_number))

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

                            wait_and_count()
                            print('~' * 50)
                            print()
                            engine.say(
                                f'Data transfer successful! {bundle_size} transferred from {sender_number} to {receiver_number}.')
                            engine.runAndWait()
                            print_slowly(
                                f"\033[1;3mData transfer successful! {bundle_size} transferred from {sender_number} to {receiver_number}.")
                            with open('sms.txt', 'w', encoding='utf-8') as fh:
                                fh.write(
                                    f"Y'ello Transfer of {bundle_size} from {sender_number} to {receiver_number} was successful.\n Dial *312# to buy data ")

                            return_menu()

                        else:
                            print('~' * 50)
                            print('No query returned')
                            return_menu()

                    else:
                        print('~' * 50)
                        print('Insufficient data balance for data transfer.')
                        return_menu()

                else:
                    print('~' * 50)
                    print('Airtime balance must be more than 100MB to continue this process.')
                    return_menu()

            else:
                print('~' * 50)
                print('No query returned')
                return_menu()

    except Exception as e:
        print('~' * 50)
        print('An error occurred: ', e)


def buy_friend_data(sender_number, receiver_number, data_amount=0, cost=0, valid_days=1):
    # Calculate expiry date outside the loop
    expiry_date = datetime.date.today() + datetime.timedelta(days=valid_days)
    expiry_date_time = datetime.datetime.now() + datetime.timedelta(days=valid_days)

    try:
        with db.cursor() as my_cur:
            if data_amount >= 1000:
                # Convert to gigabytes (GB) with one decimal place
                bundle_size = f"{data_amount / 1000:.1f}GB"
            else:
                # Keep in megabytes (MB)
                bundle_size = f"{data_amount}MB"

            # Check if sender has sufficient data amount
            sel_sender_bal = 'SELECT Airtime_balance FROM Telecom_tbl WHERE Phone_number = %s'
            my_cur.execute(sel_sender_bal, (sender_number))
            result = my_cur.fetchone()

            if result is not None:
                sender_airtime_bal = result[0]

                if sender_airtime_bal >= cost:
                    new_airtime_bal = sender_airtime_bal - cost

                    update_sender_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s WHERE Phone_number = %s'
                    my_cur.execute(update_sender_bal, (new_airtime_bal, sender_number))

                    # Select receiver data bal
                    sel_receiver_bal = 'SELECT Data_balance, Data_expires FROM Telecom_tbl WHERE Phone_number = %s'
                    my_cur.execute(sel_receiver_bal, (receiver_number))
                    result = my_cur.fetchone()

                    if result is not None:
                        receiver_data_bal = result[0]
                        data_expire = result[1]

                        new_data_bal = receiver_data_bal + data_amount

                        update_receiver_bal = 'UPDATE Telecom_tbl SET Data_balance = %s, Data_expires = %s WHERE Phone_number = %s '
                        my_cur.execute(update_receiver_bal, (new_data_bal, expiry_date, receiver_number))

                        db.commit()
                        # Print message
                        wait_and_count()
                        print('~' * 50)
                        print()
                        print_slowly(
                            f"\033[1;3mYou have gifted {bundle_size} @ ₦{cost} valid for {valid_days} day(s) to {receiver_number}.")
                        time.sleep(3)
                        clear()
                        with open('sms.txt', 'w', encoding='utf-8') as fh:
                            fh.write(
                                f'Dear customer, Your gifting of {bundle_size} @ ₦{cost} valid for {valid_days} day(s) to {receiver_number} was successful.\nand data expires at {expiry_date_time}  ')

                        return_menu()
                        # Check if data has expired
                        # if data_expire and data_expire < datetime.date.today():
                        #     print('~' * 50)
                        #     print('Your data has expired')
                        #     # Update data bal
                        #     update_bal = 'UPDATE Telecom_tbl SET Data_balance = 0 WHERE Phone_number = %s'
                        #     my_cur.execute(update_bal, (receiver_number,))
                        #     db.commit()

                    else:
                        print('~' * 50)
                        print('Receiver not found')
                        invalid()
                        return_menu()

                else:
                    print('~' * 50)
                    print('Insufficient airtime balance.')
                    return_menu()

            else:
                print('~' * 50)
                print('Sender not found')
                invalid()
                return_menu()

    except Exception as e:
        print('~' * 50)
        print('An error occurred: ', e)


def borrow_air(phone_number, amount):
    try:
        sel_bal = 'SELECT Airtime_balance FROM Telecom_tbl WHERE Phone_number = %s'
        my_cur.execute(sel_bal, (phone_number))
        result = my_cur.fetchone()

        if result is not None:
            sender_bal = result[0]

            if sender_bal <= 49.99:
                print("\t\t\033[34;3;1mY'ello! you are qualified to borrow airtime\033[0m")
                time.sleep(1)

                sel_bal = 'SELECT Airtime_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
                my_cur.execute(sel_bal, (phone_number))
                result = my_cur.fetchone()

                if result is not None:
                    borrow_bal = result[0]

                    if borrow_bal <= 3000:
                        pass

                        new_borrow_bal = borrow_bal + amount

                        update_bal = 'UPDATE Telecom_tbl SET Airtime_borrowed_balance = % s Where Phone_number = %s'
                        my_cur.execute(update_bal, (new_borrow_bal, phone_number))

                        db.commit()

                        wait_and_count()
                        print('~' * 50)
                        print()
                        print(f"\033[34;3;1mY'ello! you have been credited with N{amount} ")
                        with open('sms.txt', 'w', encoding='utf-8') as fh:
                            fh.write(
                                f'Dear customer, account has been credited with {amount}.\nDial *312# to rechage balance')

                        return_menu()

                    else:
                        print('~' * 50)
                        print()
                        print_slowly(f'Pay outstanding debt to continue this process N{borrow_bal}')
                        return_menu()
                else:
                    print('~' * 50)
                    print('No query returned')
                    return_menu()

            else:
                print('~' * 50)
                print()
                print_slowly(
                    "\t\t\033[34;1mY'ello! you are qualified, but your airtime balance is high. You can borrow airtime or\n\t\tdata when your balance is lower than N49.99 ")
                return_menu()

        else:
            print('~' * 50)
            print('No query returned')
            return_menu()

    except Exception as e:
        print('An error occurred: ', e)


def borrow_mydata(phone_number, data_amount):
    try:
        if data_amount >= 1000:
            # Convert to gigabytes (GB) with one decimal place
            bundle_size = f"{data_amount / 1000:.1f}GB"
        else:
            # Keep in megabytes (MB)
            bundle_size = f"{data_amount}MB"

        sel_bal = 'SELECT Airtime_balance FROM Telecom_tbl WHERE Phone_number = %s'
        my_cur.execute(sel_bal, (phone_number))
        result = my_cur.fetchone()

        if result is not None:
            sender_bal = result[0]

            if sender_bal <= 49.99:
                pass

                sel_bal = 'SELECT Data_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
                my_cur.execute(sel_bal, (phone_number))
                result = my_cur.fetchone()

                if result is not None:
                    borrow_bal = result[0]

                    if borrow_bal <= 1000:
                        pass

                        new_borrow_bal = data_amount + borrow_bal

                        update_bal = 'UPDATE Telecom_tbl SET Data_borrowed_balance = % s Where Phone_number = %s'
                        my_cur.execute(update_bal, (new_borrow_bal, phone_number))

                        db.commit()

                        wait_and_count()
                        print('~' * 50)
                        print()
                        print_slowly(f"\033[3;1mY'ello! you have been credited with {bundle_size} ")
                        with open('sms.txt', 'w', encoding='utf-8') as fh:
                            fh.write(
                                f'Dear customer,account recharge of {bundle_size} was successful.\nDial *312*1# to buy new active bundle')

                        return_menu()

                    else:
                        print(f'Pay outstanding debt to continue this process {borrow_bal}MB')
                        return_menu()

                else:
                    print('~' * 50)
                    print('No query returned')
                    return_menu()
            else:
                print('~' * 50)
                print()
                print_slowly(
                    "\t\t\033[34;3;1mY'ello! you are qualified, but your airtime balance is high. You can borrow airtime or\n\t\tdata when your balance is lower than N49.99\033[0m ")
                return_menu()

        else:
            print('~' * 50)
            print('No query returned')
            return_menu()

    except Exception as e:
        print('An error occurred: ', e)


# Data plan
def data_plans_subscription():
    wait()
    print('~' * 50)
    print()
    print('\t\t\t\033[31;40;3;1mBUY DATA PLANS\033[0m')
    time.sleep(0.6)
    print_slowly('\033[1m1. Daily Plan')
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
    print_slowly('0. Back\033[0m')


def daily_plan():
    wait()
    while True:
        print('~' * 50)
        print()
        print('\t\t\t\033[31;40;3;1mDaily Plan\033[0m\n')
        print('1.\033[1;3m 100MB for N100')
        time.sleep(0.6)
        print('2. 200MB for N200')
        time.sleep(0.6)
        print('3. 350MB for N300')
        time.sleep(0.6)
        print('4. 1.5GB for N500')
        time.sleep(0.6)
        print('5. 2GB for N600')
        time.sleep(0.6)
        print('0. Back\033[0m')
        print('~' * 50)
        opt = input('\t> ')

        if opt == '1':
            wait_and_count()
            while True:
                print()
                phone_number = input('\033[3;1mPlease enter phone number again to continue\n\t>>> ')
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
                    break

                else:
                    invalid()

        elif opt == '2':
            wait_and_count()
            while True:
                print()
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
                    break

                else:
                    invalid()

        elif opt == '3':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif opt == '4':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif opt == '5':
            wait_and_count()
            while True:
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
        print('~' * 50)
        print()
        print('\t\t\t\033[30;47;3;1mWeekly Plan\033[0m\n')
        print('\033[1;3m1. N300 for 350MB')
        time.sleep(0.6)
        print('2. N500 for 700MB/7days')
        time.sleep(0.6)
        print('3. N600 for 1GB')
        time.sleep(0.6)
        print('4. N1000 for 1.5GB')
        time.sleep(0.6)
        print('0. Back\033[0m')
        time.sleep(0.6)
        print('~' * 50)
        option = input('\t> ')

        if option == '1':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    break

                else:
                    invalid()

        elif option == '3':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '4':
            wait_and_count()
            while True:
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
        print('~' * 50)
        print()
        print('\t\t\t\033[30;42;3;1mMonthly Plan\033[0m\n')
        print('\033[1;3m1. N1000 for 1.2GB')
        time.sleep(0.6)
        print('2. N1200 for 1.5GB')
        time.sleep(0.6)
        print('3. N2000 for 4GB')
        time.sleep(0.6)
        print('4. N3000 for 8GB')
        time.sleep(0.6)
        print('0. Back\033[0m')
        time.sleep(0.6)
        print('~' * 50)
        option = input('\t> ')

        if option == '1':
            wait_and_count()
            while True:
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
            while True:
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
            while True:
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
            while True:
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

        elif option == '0':
            dataPlan()

        else:
            out()


def _2_3month_plan():
    wait()
    while True:
        print('~' * 50)
        print()
        print('\t\t\t\033[32;40;3;1m2-3 Month Plan\033[0m\n')
        print('\033[1;3m1. N8000 for 30GB/60days')
        time.sleep(0.6)
        print('2. N20000 for 100GB/60days')
        time.sleep(0.6)
        print('3. N30000 for 160GB/60days')
        time.sleep(0.6)
        print('4. N50000 for 400GB/90days')
        time.sleep(0.6)
        print('0. Back\033[0m')
        time.sleep(0.6)
        print('~' * 50)
        option = input('\t> ')

        if option == '1':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '2':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '3':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '4':
            wait_and_count()
            while True:
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
        print('~' * 50)
        print()
        print('\t\t\t\033[91;44;3;1mAlways on Bundle\033[0m\n')
        print('\033[1;3m1. N60 for 200MB/24hrs')
        time.sleep(0.6)
        print('2. N120 for 450MB/7days')
        time.sleep(0.6)
        print('3. N3000 for 15GB/30days')
        time.sleep(0.6)
        print('4. N6000 for 45GB/30days')
        time.sleep(0.6)
        print('0. Back\033[0m')
        print('~' * 50)
        option = input('\t> ')

        if option == '1':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '2':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '3':
            wait_and_count()
            while True:
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
                    break

                else:
                    invalid()

        elif option == '4':
            wait_and_count()
            while True:
                print()
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
        print('~' * 50)
        print()
        print('\t\t\t\033[30;47;3;1mHot Deals Plan\033[0m\n')
        print('1. N500-750MB +500 Talk time/14days')
        time.sleep(0.6)
        print('2. N1000-1.5GB +1000 Talk time/30days')
        time.sleep(0.6)
        print('3. N2000-4.5GB +2000 Talk time/30days')
        time.sleep(0.6)
        print('0 back')
        time.sleep(0.6)
        print('~' * 50)
        option = input('\t> ')

        if option == '1':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            while True:
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

        elif option == '0':
            dataPlan()

        else:
            out()


def manage_data_plan():
    wait()
    while True:
        print('~' * 50)
        print()
        print('\t\t\t\033[32;40;1mManage Data Plan\033[0m\n')
        print('\033[1;3m1. VIEW ACTIVE DATA BUNDLE')
        time.sleep(0.6)
        print('0. back\033[0m')
        time.sleep(0.6)
        print('~' * 50)
        option = input('\t> ')

        if option == '1':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))
                if user:
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
    wait()
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
        main_menu()

    else:
        out()
        time.sleep(1)
        dataPlan()


# SOCIAL BUNDLE CODE
def whatsapp():
    try:
        wait()
        while True:
            print('~' * 50)
            print()
            print("\t\t\t\033[31;40;3;1mWhatsapp\033[0m\n")
            print("\033[1;3m1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 200MB")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")
            if ans.isnumeric():
                if ans == '1':
                    wait_and_count()
                    while True:
                        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                        phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[37;40;3;1mFacebook\033[0m\n")
            print("\033[1;3m1. Daily @ ₦25 for 50MB")
            time.sleep(1)
            print("2. Weekly @ ₦50 for 100MB")
            time.sleep(1)
            print("3. Monthly @ ₦150 for 250MB")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ask = input("\t> ")

            if ask == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[91;40;1mInstagram\033[0m\n")
            print("\033[1;3m1. ₦100 for 250MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦250 for 1.5GB/3-days.")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            opt = input("\t> ")

            if opt == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[32;40;1mTiktok\033[0m\n")
            print("\033[1;3m1. ₦100 for 200MB/1 day.")
            time.sleep(1)
            print("2. ₦150 for 350MB/2 days.")
            time.sleep(1)
            print("3. ₦200 for 1GB/1 day.")
            time.sleep(1)
            print("4. ₦200 for 1.5GB/3-days.")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[91;47;3;1mAll Social Bundles\033[0m\n")
            print("\033[1;3m1. Daily @ ₦50 for 150MB.")
            time.sleep(1)
            print("2. Weekly @ ₦100 for 350MB.")
            time.sleep(1)
            print("3. Monthly @ ₦250 for 1GB.")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[31;40;1mYoutube,Instagram, and TikTok\033[0m\n")
            print("\033[1;3m1. Daily @ ₦100 for 350MB.")
            time.sleep(0.6)
            print('0.back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[30;44;3;1mOpera Mini & News\033[0m\n")
            print("\033[1;3m1. ₦20/50MB/1day.")
            time.sleep(1)
            print("2. ₦50/100MB/7days.")
            time.sleep(1)
            print("3. ₦100/500MB/30days.")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
            print('~' * 50)
            print()
            print("\t\t\t\033[91;40;1mSocial Mega Bundles\033[0m\n")
            print("\033[1;3m1. 750MB for ₦200 (3 days).")
            time.sleep(1)
            print("2. 1GB for N300 (7 days).")
            time.sleep(1)
            print('0. back\033[0m')
            time.sleep(1.5)
            print('~' * 50)
            ans = input("\t> ")

            if ans == '1':
                wait_and_count()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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
wait()


def social_bundles():
    wait()
    print('~' * 50)
    print()
    print('\t\t\t\033[32;40;1mSocial Bundles\033[0m')
    time.sleep(1)
    print_slowly("\033[3;1m1. Whatsapp")
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
    print_slowly('0. Back\033[0m')
    time.sleep(1)
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

    elif ask == '0':
        main_menu()

    else:
        out()
        time.sleep(0.5)
        social_bundles()


# Borrow airtime
def borrow_airtime():
    try:
        wait()
        while True:
            print('~' * 50)
            print()
            print('\t\t\t\033[30;47;1mBorrow Airtime\033[0m')
            time.sleep(0.6)
            print('\033[1;3m1. N50 ')
            time.sleep(0.6)
            print('2. N100 ')
            time.sleep(0.6)
            print('3. N500')
            time.sleep(0.6)
            print('0. back\033[0m')
            time.sleep(0.6)
            print('~' * 50)
            opt = input('\t> ')

            if opt == '1':
                wait()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

            elif opt == '2':
                wait()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

            elif opt == '3':
                wait()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

            elif opt == '0':
                borrow_credit()

            else:
                out()

    except Exception as e:
        print('An error Occurred: ', e)


# Borrow data
def borrow_data():
    try:
        while True:
            wait()
            print('~' * 50)
            print()
            print('\t\t\t\033[32;40;3;1mBorrow Data\033[0m')
            time.sleep(0.6)
            print('1. 100MB ')
            time.sleep(0.6)
            print('2. 150MB ')
            time.sleep(0.6)
            print('3. 500MB')
            time.sleep(0.6)
            print('0. back')
            time.sleep(0.6)
            print('~' * 50)
            opt = input('\t> ')

            if opt == '1':
                wait()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

            elif opt == '2':
                wait()
                while True:
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

            elif opt == '0':
                borrow_credit()

            else:
                out()

    except Exception as e:
        print('An error Occurred: ', e)


# Borrow airtime & Data
def borrow_credit():
    wait()
    print('~' * 50)
    time.sleep(0.6)
    print()
    print_slowly('\t\t\t\033[30;44;3;1mBorrow credit\033[0m ')
    time.sleep(0.6)
    print_slowly('\033[3;1m1.Borrow Airtime')
    time.sleep(0.6)
    print_slowly('2. Borrow Data')
    time.sleep(0.6)
    print_slowly('0. Back\033[0m')
    time.sleep(0.6)
    print('~' * 50)
    opt = input('\t> ')

    if opt == '1':
        borrow_airtime()

    elif opt == '2':
        borrow_data()

    elif opt == '0':
        main_menu()

    else:
        out()
        borrow_credit()


# Travel Pass Plan
def travel_pass_plan():
    wait()
    while True:
        print('~' * 50)
        print()
        print(" \t\t\t\033[30;47;3;1mTravel Pass Plan\033[0m \n")
        time.sleep(1)
        print("1. 7days(voice) 4000talktime and 100MB @ ₦10,000.")
        time.sleep(1)
        print("2. 7days 1GB Data @ ₦10,000.")
        time.sleep(1)
        print('0. back')
        # time.sleep(1)
        # print("3. Inflight Roaming Data.")
        # time.sleep(1)
        # print("4. Roaming Balance Check.")
        time.sleep(1.5)
        print('~' * 50)
        ans = input("> ")

        if ans == '1':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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


        elif ans == '2':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        elif ans == '0':
            roaming_int()

        else:
            out()


# Data Hybrid
def data_hybrid():
    wait()
    while True:
        print('~' * 50)
        print()
        print(" \t\t\t\033[31;40;1mData Hybrid\033[0m \n")
        time.sleep(1)
        print("1. ₦2,000 for 4GB.")
        time.sleep(1)
        print("2. ₦3,000 for 8GB.")
        time.sleep(1)
        print("3. ₦3,500 for 10GB.")
        time.sleep(1)
        print("4. ₦4,000 for 12GB.")
        time.sleep(1)
        print('0. back')
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        elif ans == '2':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        elif ans == '3':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        elif ans == '4':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        elif ans == '0':
            roaming_int()

        else:
            out()


# Inflight Roaming Data
def inflight_roaming_data():
    wait()
    while True:
        print('~' * 50)
        print()
        print(" \t\t\t\033[91;40;3;1mInflight Roaming Data\033[0m \n")
        time.sleep(1)
        print("1. 50MB @ ₦200.")
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            wait_and_count()
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            out()


def roaming_int():
    while True:
        wait()
        print()
        print("\t\t\t\033[30;47;3;1mRoaming\033[0m \n")
        time.sleep(1)
        print_slowly("\033[3;1m1. Travel Pass Plan.")
        time.sleep(1)
        print_slowly("2. Data Hybrid")
        time.sleep(1)
        print_slowly("3. Inflight Roaming Data")
        time.sleep(1)
        print_slowly('0. Back\033[0m')
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

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
            roaming_int()


# YouTube Video Packs
def youtube_video_packs():
    wait()
    while True:
        print('~' * 50)
        print()
        print(" \t\t\t\033[91;40;3;1mYouTube Video Packs\033[0m\n")
        print("1. 24 hour @ ₦100 for 800MB.")
        time.sleep(1)
        print("2. 24 hours @ ₦150 for 1.2GB.")
        time.sleep(1)
        print("3. 500MB at ₦50 24 hours.")
        time.sleep(1)
        print('0. back')
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            clear()
            wait_and_count()
            while True:
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


        elif ans == '2':
            clear()
            wait_and_count()
            while True:
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


        elif ans == '3':
            clear()
            wait_and_count()
            while True:
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


        elif ans == '0':
            video_pack()

        else:
            out()


# YouTubeOnlyDataAccess
def youtube_only_data_access():
    wait()
    while True:
        print('~' * 50)
        print()
        print("\t\t\t\033[32;40;3;1mYoutube Only and Data Access\033[0m\n")
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
            while True:
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
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

        else:
            out()
            break
    clear()


# Buffet Bundle
def buffet_bundle():
    wait()
    while True:
        print('~' * 50)
        print()
        print("\t\t\t\033[34;40;3;1mBuffet Bundle\033[0m \n")
        time.sleep(1)
        print("1. 24 hours(1.3GB) plan for ₦200.")
        time.sleep(1)
        print("2. 24 hours(600MB) plan for ₦100.")
        time.sleep(1)
        print('0. back')
        time.sleep(1.5)
        print('~' * 50)
        ans = input("\t> ")

        if ans == '1':
            clear()
            wait_and_count()
            while True:
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

        elif ans == '2':
            clear()
            wait_and_count()
            while True:
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

        elif ans == '0':
            video_pack()

        else:
            out()


# Video Packs
def video_pack():
    wait()
    while True:
        print('~' * 50)
        print()
        print("\t\t\t\033[31;40;3;1mVideo Packs\033[0m\n")
        time.sleep(1)
        print_slowly("\033[3;1m1. Youtube video packs.")
        time.sleep(1)
        print_slowly("2. Buffet Bundle: This has a 12hrs & 24 hrs plan")
        time.sleep(1)
        print_slowly("3. 1GB(Youtube only) + 500MB (Data access)")
        time.sleep(1)
        print_slowly('0. Back\033[0m')
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

        elif ans == '0':
            main_menu()

        else:
            out()


# Transfer data
def data_transfer():
    try:
        wait()
        print('~' * 50)
        while True:
            sender_number = input('\033[3;1mPlease enter your phone number to continue\033[0m\n\t> ')
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (sender_number))

            if user:
                wait()
                print('~' * 50)
                while True:
                    receiver_number = input('\033[3;1mEnter receiver phone number\033[0m\n\t> ')
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (receiver_number))

                    if user:
                        wait()
                        print('~' * 50)
                        while True:
                            data_amount = input('\033[3;1mEnter data amount\033[0m\n\t> ')

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
                                    print("\033[31;3;1mCan't make transfer more than 2000MB ")
                                    time.sleep(0.7)
                                    print('Re-enter amount')

                            else:
                                out()

                    else:
                        invalid()

            else:
                invalid()

    except Exception as e:
        print('~' * 50)
        print('An error occurred: ', e)


# Buy for a friend
def buy_friend():
    try:
        wait()
        while True:
            print('~' * 50)
            print()
            sender_number = input('\033[1mPlease enter your phone number to continue\033[0m\n\t> ')
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (sender_number))

            if user:
                wait()
                while True:
                    print('~' * 50)
                    print()
                    print('\t\t\t\033[31;40;3;1mWelcome to our gifting service.Select data plan to gift.\033[0m')
                    time.sleep(0.6)
                    print_slowly('\033[1;3m1. Data Plans')
                    time.sleep(0.6)
                    print_slowly('2. Social Bundles')
                    time.sleep(0.6)
                    print_slowly('3. Video Pack')
                    time.sleep(0.6)
                    print_slowly('0. Back\033[0m')
                    print('~' * 50)
                    opt = input('\t> ')

                    if opt == '1':
                        wait()
                        while True:
                            print('~' * 50)
                            print()
                            print('\t\t\t\033[32;3;40;1mBUY DATA PLANS\033[0m')
                            time.sleep(0.6)
                            print_slowly('\033[1;3m1. Daily Plan')
                            time.sleep(0.6)
                            print_slowly('2. Weekly Plan')
                            time.sleep(0.6)
                            print_slowly('3. Monthly Plan')
                            time.sleep(0.6)
                            print_slowly('4. 2-3Month Plan \033[0m')
                            print('~' * 50)
                            ans = input('\t> ')

                            if ans == '1':
                                wait()
                                while True:
                                    print('~' * 50)
                                    print()
                                    print('\t\t\t\033[31;3;40;1mDaily Plan\033[0m\n')
                                    print('1. 100MB for N100')
                                    time.sleep(0.6)
                                    print('2. 200MB for N200')
                                    time.sleep(0.6)
                                    print('3. 350MB for N300')
                                    time.sleep(0.6)
                                    print('4. 1.5GB for N500')
                                    print('~' * 50)
                                    res = input('\t> ')

                                    if res == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m\n\t> ")
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

                                    elif res == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m\n\t> ")
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

                                    elif res == '4':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    else:
                                        out()

                            elif ans == '2':
                                wait()
                                while True:
                                    print('~' * 50)
                                    print()
                                    print('\t\t\t\033[;3;47;30;1mWeekly Plan\033[0m\n')
                                    print('1. N300 for 350MB')
                                    time.sleep(0.6)
                                    print('2. N500 for 700MB/7days')
                                    time.sleep(0.6)
                                    print('3. N600 for 1GB')
                                    time.sleep(0.6)
                                    print('4. N1000 for 1.5GB')
                                    time.sleep(0.6)
                                    print('~' * 50)
                                    res = input('\t> ')

                                    if res == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '4':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                            elif ans == '3':
                                wait()
                                while True:
                                    print('~' * 50)
                                    print()
                                    print('\t\t\t\033[31;40;3;1mMonthly Plan\033[0m\n')
                                    print('1. N1000 for 1.2GB')
                                    time.sleep(0.6)
                                    print('2. N1200 for 1.5GB')
                                    time.sleep(0.6)
                                    print('3. N2000 for 4GB')
                                    time.sleep(0.6)
                                    print('4. N3000 for 8GB')
                                    time.sleep(0.6)
                                    print('~' * 50)
                                    res = input('\t> ')

                                    if res == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '4':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                            elif ans == '4':
                                wait()
                                while True:
                                    print('~' * 50)
                                    print()
                                    print('\t\t\t\033[34;3;40;1m2-3 Month Plan\033[0m\n')
                                    print('1. N8000 for 30GB/60days')
                                    time.sleep(0.6)
                                    print('2. N20000 for 100GB/60days')
                                    time.sleep(0.6)
                                    print('3. N30000 for 160GB/60days')
                                    time.sleep(0.6)
                                    print('4. N50000 for 400GB/90days')
                                    time.sleep(0.6)
                                    print('~' * 50)
                                    res = input('\t> ')

                                    if res == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif res == '4':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    else:
                                        out()
                            else:
                                out()
                                time.sleep(0.5)

                    elif opt == '2':
                        wait()
                        while True:
                            print('~' * 50)
                            print()
                            print('\t\t\t\033[31;3;40;1mSocial Bundles\033[0m')
                            time.sleep(1)
                            print_slowly("\033[1;3m1. Whatsapp")
                            time.sleep(1)
                            print_slowly("2. Facebook")
                            time.sleep(1)
                            print_slowly("3. Instagram")
                            time.sleep(1)
                            print_slowly("4. Tiktok")
                            time.sleep(1)
                            print_slowly('0.Back\033[0m')
                            time.sleep(1)
                            ask = input('\t> ')

                            if ask == '1':
                                while True:
                                    wait()
                                    print('~' * 50)
                                    print()
                                    print("\t\t\t\033[30;3;47;1mWhatsapp\033[0m\n")
                                    print("1. Daily @ ₦25 for 50MB")
                                    time.sleep(1)
                                    print("2. Weekly @ ₦50 for 100MB")
                                    time.sleep(1)
                                    print("3. Monthly @ ₦150 for 200MB")
                                    time.sleep(1.5)
                                    print('~' * 50)
                                    ans = input("\t> ")

                                    if ans == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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
                                    else:
                                        out()

                            elif ask == '2':
                                while True:
                                    wait()
                                    print('~' * 50)
                                    print()
                                    print("\t\t\t\033[3;32;40;1mFacebook\033[0m\n")
                                    print("1. Daily @ ₦25 for 50MB")
                                    time.sleep(1)
                                    print("2. Weekly @ ₦50 for 100MB")
                                    time.sleep(1)
                                    print("3. Monthly @ ₦150 for 250MB")
                                    time.sleep(1.5)
                                    print('~' * 50)
                                    ans = input("\t> ")

                                    if ans == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    else:
                                        out()

                            elif ask == '3':
                                wait()
                                while True:
                                    print('~' * 50)
                                    print()
                                    print("\t\t\t\033[31;40;3;1mInstagram\033[0m\n")
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
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '4':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    else:
                                        out()

                            elif ask == '4':
                                while True:
                                    wait()
                                    print('~' * 50)
                                    print()
                                    print("\t\t\t\033[30;47;3;1mTiktok\033[0m\n")
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
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ans == '4':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    else:
                                        out()

                            elif ask == '0':
                                buy_friend()

                            else:
                                out()

                    elif opt == '3':
                        while True:
                            wait()
                            print('~' * 50)
                            print()
                            print("\t\t\t\033[32;3;40;1m Video Packs\033[0m \n")
                            time.sleep(0.6)
                            print("\033[1;3m1. Youtube video packs.\033[0m")
                            time.sleep(0.6)
                            ans = input('\t> ')

                            if ans == '1':
                                wait()
                                while True:
                                    print('~' * 50)
                                    print()
                                    print(" \t\t\t\033[31;3;40;1mYouTube Video Packs\033[0m\n")
                                    print("1. 24 hour @ ₦100 for 800MB.")
                                    time.sleep(1)
                                    print("2. 24 hours @ ₦150 for 1.2GB.")
                                    time.sleep(1)
                                    print("3. 500MB at ₦50 24 hours.")
                                    time.sleep(1.5)
                                    print('~' * 50)
                                    ask = input("\t> ")

                                    if ask == '1':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ask == '2':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    elif ask == '3':
                                        while True:
                                            print('~' * 50)
                                            print()
                                            receiver_number = input("\033[1mEnter recipient's number\033[0m \n\t> ")
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

                                    else:
                                        out()

                            else:
                                out()

                    elif opt == '0':
                        buy_friend()

                    else:
                        out()

            else:
                invalid()

    except Exception as e:
        print('An error occurred: ', e)


# GIFT DATA
def gift_data():
    wait()
    print('~' * 50)
    print()
    print('\t\t\033[91;44;3;1mGift Data\033[0m')
    print()
    time.sleep(0.6)
    print_slowly('\033[3;1m1.Transfer from data balance')
    time.sleep(0.6)
    print_slowly('2.Buy for a friend')
    time.sleep(0.6)
    print_slowly('0. Back\033[0m')
    time.sleep(0.6)
    print('~' * 50)
    opt = input('\t> ')

    if opt == '1':
        data_transfer()

    elif opt == '2':
        buy_friend()

    elif opt == '0':
        main_menu()

    else:
        out()
        gift_data()


def chat_zigi():
    wait()
    print('~' * 100)
    print()
    engine.say(f""" Y'ello! Need help, chat with Zigi on preferred network such
                   as;whatsapp,facebook messenger
                   Web and Telegram.Details via sms.

    """)
    engine.runAndWait()
    time.sleep(0.7)
    message = '''\033[31;3;1m\t\t\t\tY'ello! Need help, chat with Zigi on preferred network such
                   \tas;whatsapp,facebook messenger
                   Web and Telegram.Details via sms.\033[0m
                   '''
    print(message)
    time.sleep(14)
    print()
    return_menu()


def check_data():
    try:
        wait()
        print('~' * 50)
        print()
        phone_number = input('\033[31;1;3mPlease enter phone number\033[0m\n\t> ')
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))
        if user:
            wait_and_count()
            checkDataBal(phone_number)

            print(end='\r')
            print(end='\r')
            time.sleep(1)
            clear()

        else:
            invalid()
            check_data()

    except Exception as e:
        print('Oops something went wrong: ', e)


# menu function
def main_menu():
    wait()
    print('~' * 50)
    print()
    engine.say(f'Welcome to our USSD Service.')
    engine.runAndWait()
    print_slowly("\t\t\t\033[32;107;40;3;1mWelcome to our USSD Service.\033[0m")
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'data plan')
    engine.runAndWait()
    print_slowly('\033[3;1m1. Data Plan')
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'social bundles')
    engine.runAndWait()
    print_slowly('2. Social Bundles')
    time.sleep(0.3)
    engine.say(f'borrow credit')
    engine.runAndWait()
    # time.sleep(0.3)  # Wait for 1 second
    print_slowly('3. Borrow Credit')
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'roaming internationally')
    engine.runAndWait()
    print_slowly("4. Roaming\\int'l")
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'video pack')
    engine.runAndWait()
    print_slowly('5. Video Pack')
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'gift data')
    engine.runAndWait()
    print_slowly('6. Gift data')
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'recharge airtime')
    engine.runAndWait()
    print_slowly('7. Recharge Airtime')
    time.sleep(0.3)  # Wait for 1 second
    engine.say(f'chat with zigi.')
    engine.runAndWait()
    print_slowly('8. Chat with Zigi\033[0m')
    print()
    print('~' * 50)
    menu = input('\t>>> ')

    if menu == '1':
        dataPlan()

    elif menu == '2':
        social_bundles()

    elif menu == '3':
        borrow_credit()

    elif menu == '4':
        roaming_int()

    elif menu == '5':
        video_pack()

    elif menu == '6':
        gift_data()

    elif menu == '7':
        recharge()

    elif menu == '8':
        chat_zigi()

    else:
        engine.say(f'invalid')
        engine.runAndWait()
        print('Invalid Entry\nTry again\n')
        main_menu()

    clear()


# ussd function
def ussd_code():
    print('~' * 50)
    print()
    engine.say(f'enter u s s d')
    engine.runAndWait()
    ussd = input('\033[1mEnter ussd\033[0m\n\t>>> ')

    if ussd == '*312#':
        main_menu()

    elif ussd == '*312*1#':
        dataPlan()

    elif ussd == '*312*2#':
        social_bundles()

    elif ussd == '*312*7#':
        recharge()

    elif ussd == '*310#':
        check_data()

    else:
        print('~' * 50)
        print('Invalid ussd\nTry again\n')
        ussd_code()

    clear()


# ussd_code()
