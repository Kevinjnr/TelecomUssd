import pymysql
import time
import sys
import os
import pyttsx3
import datetime
from decimal import Decimal
from TelecomProject.notification import send_notification
from animation.colors import *
from TelecomProject.ussd_short import wait, wait_and_count, clear, print_slowly, out, invalid, countdown_timer
from TelecomProject.return_menu import return_menu
from plyer import notification

engine = pyttsx3.init()

# Initialize the db and my_cur variables
db = pymysql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()


def recharge():
    try:
        print()
        print(f'{brt_black_bg}{brt_yellow}Recharge number{end}  {bold}{magenta} ')
        # Check user number
        engine.say("Enter phone number")
        engine.runAndWait()
        print(f'{brt_yellow}Enter phone number:{end}{bold}{magenta}')
        print('~~~~~~~~~~~~~~~~~~~')
        phone_number = input('>>> ').strip()
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        user = my_cur.execute(check_num, (phone_number))

        if user:
            while True:
                print()
                engine.say("Enter amount to recharge")
                engine.runAndWait()
                print(f'{brt_yellow}Enter amount to recharge:{end} {bold}{magenta} ')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                amount = input('>>> ').strip()

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
                            print()
                            engine.say(f"The recharge of {amount}naira was successful. Account balance: {amount}naira")
                            engine.runAndWait()
                            print_slowly(
                                f'{brt_green}The recharge of N{amount}.00 was successful\nAcct.bal N{amount}.00{end}{bold}{magenta}')

                            note = f'''
Account recharge of N{amount}.00 was successful. Get 1.5GB at N500.
Dial *312*1# to buy data bundle
                                                    '''
                            send_notification('ConsoleUssdSms', note, 'ConsoleRechargeSms')

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
                                    print_slowly(f'N{borrow_bal}.00 deducted from account')
                                    break

                                else:
                                    pass
                                    break

                            else:
                                time.sleep(0.6)
                                engine.say('no query returned')
                                engine.runAndWait()
                                print(f'{brt_red}::No query returned{end} {bold}{magenta}')
                                time.sleep(4)
                                clear()

                        else:
                            invalid()
                            time.sleep(4)
                            clear()

                    else:
                        time.sleep(0.8)
                        engine.say(f"amount must be more than 30 naira")
                        engine.runAndWait()
                        print(f'{brt_red}::Amount must be more than N30{end} {bold}{magenta}')
                        time.sleep(4)
                        clear()

                else:
                    out()
                    time.sleep(4)
                    clear()

            return_menu()

        else:
            invalid()
            time.sleep(3)
            clear()
            recharge()

    except Exception as e:
        engine.say(f"An error occurred")
        engine.runAndWait()
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)
        with open('error.txt', 'w') as file:
            file.write(str(e))


# Check data bal
def checkDataBal(phone_number):
    try:
        # Query to check and select data bal
        sel_bal = 'SELECT Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_bal, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            data_bal = result[0]

            sel_bal = 'SELECT Data_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
            my_cur.execute(sel_bal, (phone_number,))
            result = my_cur.fetchone()

            if result is not None:
                borrow_bal = result[0]

                if borrow_bal == 0:

                    if data_bal == 0:
                        engine.say(f"you have no active data bundle")
                        engine.runAndWait()
                        print(f'{brt_black_bg}{brt_red}{italic}{bold}You have no active data bundle{end} {bold}{magenta}')

                        note = f'''
Dear customer, you don't have any active data bundle.
Dial *312*1# to buy another bundle.
                                                                            '''
                        send_notification('ConsoleUssdSms', note, 'ConsoleBalSms')

                        return_menu()

                else:
                    print()
                    if borrow_bal != 0:
                        print_slowly(f'{brt_black_bg}{brt_green}Your data balance is {data_bal}MB.-{borrow_bal}MB {end}    {bold}{magenta}')

                        note = f'''
Your data balance: {data_bal}MB.-{borrow_bal}MB
Get 1.5GB @ N200 Tiktok, dial *312*2#.
                               '''
                        send_notification('ConsoleUssdSms', note, 'ConsoleBalSms')

                        return_menu()

                    else:
                        print_slowly(
                            f'{brt_black_bg}{brt_green}Your data balance is {data_bal}MB.    {bold}{magenta}')

                        note = f'''
Your data balance: {data_bal}MB.
Get 1.5GB @ N200 Tiktok, dial *312*2#.
                               '''
                        send_notification('ConsoleUssdSms', note, 'ConsoleBalSms')

                        return_menu()

        else:
            engine.say(f"No query returned")
            engine.runAndWait()
            print(f'{brt_red}::Error:No query returned{end} {bold}{magenta}')
            return_menu()

    except Exception as e:
        engine.say(f"an error occurred")
        engine.runAndWait()
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)


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
                        engine.say(
                            f"You have been credited with {bundle_size} for {cost}naira valid for {valid_days} days.")
                        engine.runAndWait()
                        print_slowly(
                            f"{brt_black_bg}{brt_yellow}You have been credited with {bundle_size} @ ₦{cost} valid for {valid_days} day(s).{end} {bold}{magenta}")
                        time.sleep(1)
                        note = f'''
Activation of {bundle_size} bundle for {valid_days}day(s) @ ₦{cost} was successful
and expires at {str(expiry_date_time)}
                        '''

                        send_notification('ConsoleUssdSms', note, 'ConsoleRechargeSms')

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

                                    print()
                                    engine.say(f"{borrow_bal}mb was deducted from your account")
                                    engine.runAndWait()
                                    print_slowly(f'{brt_yellow}{borrow_bal}MB was deducted from your account{end} {bold}{magenta}')
                                    return_menu()
                                    break

                                else:
                                    pass
                                    break

                            else:
                                time.sleep(0.6)
                                engine.say(f"no query returned")
                                engine.runAndWait()
                                print(f'{brt_red}::No query returned{end} {bold} {magenta}')
                                return_menu()
                                break

                        except Exception as e:
                            engine.say(f"an error occurred while updating data")
                            engine.runAndWait()
                            print(f"{brt_red}::An error occurred while updating data:", e, end, bold, magenta)
                            db.rollback()  # Rollback changes if an error occurs

                    else:
                        wait()
                        engine.say(f"insufficient airtime balance")
                        engine.runAndWait()
                        print(f'{brt_red}::Insufficient Airtime balance.{end} {bold}{magenta}')
                        return_menu()

                else:
                    engine.say(f"no query returned")
                    engine.runAndWait()
                    print(f'{brt_red}::Error: No query returned{end} {bold} {magenta}')
                    return_menu()
                    break

            return_menu()

        except Exception as e:
            engine.say(f"an error occurred")
            engine.runAndWait()
            print(f"{brt_red}::An error occurred:", e, end, bold, magenta)
            with open('error.txt', 'w') as file:
                file.write(str(e))
        clear()


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
                sel_balance = 'SELECT Airtime_balance,Data_balance,Talk_time_balance,Data_expires from Telecom_tbl WHERE Phone_number =%s'
                my_cur.execute(sel_balance, (phone_number,))
                result = my_cur.fetchone()

                if result is not None:
                    current_balance = result[0]
                    current_data_bal = result[1]
                    current_talk_bal = result[2] if len(result) > 2 else 0
                    data_expire = result[3] if len(result) > 3 else 0

                    # Check if data has expired
                    if data_expire and data_expire < datetime.date.today():
                        print('Your data has expired')

                        # Update data bal
                        update_bal = 'UPDATE Telecom_tbl SET Data_balance = 0,Talk_time = 0 WHERE Phone_number = %s'
                        my_cur.execute(update_bal, (phone_number,))
                        db.commit()
                        break

                    if current_balance >= cost:

                        # Print message
                        wait_and_count()
                        print()
                        engine.say(
                            f'you have been credited with {bundle_size}and {talk_time} talktime for {cost}naira, valid for {valid_days} days.')
                        engine.runAndWait()
                        print_slowly(
                            f"{brt_black_bg}{brt_yellow}You have been credited with {bundle_size}+{talk_time}talktime @ ₦{cost} valid for {valid_days} day(s).{end} {bold}{magenta}")
                        time.sleep(3)
                        clear()
                        note = f'''
Activation of {bundle_size}+{talk_time}talktime for {valid_days}day(s) @ ₦{cost} was successful
and expires at {expiry_date_time} ')
                                                '''
                        send_notification('ConsoleUssdSms', note, 'ConsoleRechargeSms')

                        # Deduct from bal
                        new_balance = current_balance - cost

                        # Add to data bal
                        new_data_bal = current_data_bal + data_amount

                        # Add to talk bal
                        new_talk_bal = current_talk_bal + talk_time
                        try:
                            # Query to update bal
                            update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s,Talk_time_balance = %s WHERE Phone_number = %s'
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

                                    print()

                                    print(f'{brt_black_bg}{brt_blue}{borrow_bal}MB deducted from account{end}{bold}{magenta}')

                                    return_menu()
                                    break

                                else:
                                    pass
                                    break

                            else:
                                time.sleep(0.6)
                                print(f'{brt_red}::No query returned{end}{bold}{magenta}')
                                return_menu()

                        except Exception as e:

                            print(f"{brt_red}::An error occurred while updating data:", e, end, bold, magenta)
                            # db.rollback()  # Rollback changes if an error occurs

                    else:
                        wait()
                        print(f'{brt_red}::Insufficient Airtime balance.{end}{bold}{magenta}')
                        return_menu()

                else:
                    print(f'{brt_red}::Error: No query returned{end}{bold}{magenta}')
                    return_menu()

            return_menu()

        except Exception as e:
            print(f'{brt_red}::Error', e, bold, magenta)
            with open('error.txt', 'w') as file:
                file.write(repr(e))

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

                            if receiver_number != sender_number:

                                # Add to receiver bal
                                new_receiver_bal = receiver_bal + data_amount

                                # Update receiver's balance
                                update_receiver_bal = 'UPDATE Telecom_tbl SET Data_balance = %s WHERE Phone_number = %s'
                                my_cur.execute(update_receiver_bal, (new_receiver_bal, receiver_number))

                                # Commit changes
                                db.commit()

                                wait_and_count()
                                print()
                                engine.say(
                                    f'Data transfer successful! {bundle_size} transferred from {sender_number} to {receiver_number}.')
                                engine.runAndWait()
                                print_slowly(
                                    f"{brt_black_bg}{brt_green}Data transfer successful! {bundle_size} transferred from {sender_number} to {receiver_number}.{end} {bold}{magenta}")

                                note = f'''
Y'ello Transfer of {bundle_size} from {sender_number} to {receiver_number} was successful.
Dial *312# to buy data
                                                                                '''
                                send_notification('ConsoleUssdSms', note, 'ConsoleDataTransSms')

                                return_menu()

                            else:
                                print(f'{brt_red}::Number cannot complete request{end}{bold}{magenta}')
                                return_menu()

                        else:
                            print(f'{brt_red}::No query returned{end}{bold}{magenta}')
                            return_menu()

                    else:
                        print(f'{brt_red}::Insufficient data balance for data transfer.{end}{bold}{magenta}')
                        return_menu()

                else:
                    print(f'{brt_red}::Airtime balance must be more than 100MB to continue this process.{end}{bold}{magenta}')
                    return_menu()

            else:
                print(f'{brt_red}::No query returned{end} {bold} {magenta}')
                return_menu()

    except Exception as e:
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)
        with open('error.txt', 'w') as file:
            file.write(str(e))


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

                        if sender_number != receiver_number:

                            new_data_bal = receiver_data_bal + data_amount

                            update_receiver_bal = 'UPDATE Telecom_tbl SET Data_balance = %s, Data_expires = %s WHERE Phone_number = %s '
                            my_cur.execute(update_receiver_bal, (new_data_bal, expiry_date, receiver_number))

                            db.commit()
                            # Print message
                            wait_and_count()
                            print()
                            print_slowly(
                                f"{brt_black_bg}{brt_green}You have gifted {bundle_size} @ ₦{cost} valid for {valid_days} day(s) to {receiver_number}.{end} {bold} {magenta}")
                            time.sleep(3)
                            clear()

                            note = f'''
Dear customer, Your gifting of {bundle_size} @ ₦{cost} valid for {valid_days} day(s) to {receiver_number} was successful.
and data expires at {expiry_date_time}. Dial *312*1# for more data offer.
                                  '''
                            send_notification('ConsoleUssdSms', note, 'ConsoleGiftDataSms')

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
                            clear()
                            print(f'{brt_red}::Number cannot complete request{end}{bold}{magenta}')
                            time.sleep(5)
                            clear()
                            return_menu()

                    else:
                        print(f'{brt_red}::Receiver not found{end} {bold} {magenta}')
                        invalid()
                        return_menu()

                else:
                    print(f'{brt_red}::Insufficient airtime balance.{end} {bold} {magenta}')
                    return_menu()

            else:
                print(f'{brt_red}::Sender not found{end} {bold} {magenta}')
                invalid()
                return_menu()

    except Exception as e:
        print(f'{brt_red}::An error occurred: ', e)
        with open('error.txt', 'w') as file:
            file.write(str(e))


def borrow_air(phone_number, amount):
    try:
        sel_bal = 'SELECT Airtime_balance FROM Telecom_tbl WHERE Phone_number = %s'
        my_cur.execute(sel_bal, (phone_number))
        result = my_cur.fetchone()

        if result is not None:
            sender_bal = result[0]

            if sender_bal <= 49.99:
                print(f"\t\t{brt_black_bg}{brt_yellow}Y'ello! you are qualified to borrow airtime{end}{bold}{magenta}")
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
                        print()
                        print(f"{brt_black_bg}{brt_green}Y'ello! you have been credited with N{amount} {end}{bold}{magenta}")

                        note = f'''
Dear customer, account has been credited with {amount}.
Dial *312# to recharge balance   
                              '''
                        send_notification('ConsoleUssdSms', note, 'ConsoleBorrowCreditSms')

                        return_menu()

                    else:
                        print()
                        print_slowly(f'{brt_red}::Pay outstanding debt to continue this process N{borrow_bal}{end}{bold}{magenta}')
                        return_menu()
                else:
                    print(f'{brt_red}::No query returned{end}{bold}{magenta}')
                    return_menu()

            else:
                print()
                print_slowly(
                   f"\t\t{brt_black_bg}{brt_blue}::Y'ello! you are qualified, but your airtime balance is high. You can borrow airtime or\n\t\tdata when your balance is lower than N49.99. {end}{bold}{magenta} ")
                return_menu()

        else:
            print(f'{red}::No query returned{end}{bold}{magenta}')
            return_menu()

    except Exception as e:
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)
        with open('error.txt', 'w') as file:
            file.write(str(e))


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
                        print()
                        print_slowly(f"{brt_black_bg}{brt_green}Y'ello! you have been credited with {bundle_size}{end} {bold}{magenta} ")

                        note = f'''
Dear customer,account has been credited with {bundle_size}.
Dial *312*1# to buy new active bundle  
                                                      '''
                        send_notification('ConsoleUssdSms', note, 'ConsoleBorrowCreditSms')

                        return_menu()

                    else:
                        print(f'{brt_red}::Pay outstanding debt to continue this process {borrow_bal}MB{end}{bold}{magenta}')
                        return_menu()

                else:
                    print(f'{brt_red}::No query returned{end}{bold}{magenta}')
                    return_menu()
            else:
                print()
                print_slowly(
                    f"\t\t{brt_black_bg}{brt_green}::Y'ello! you are qualified, but your airtime balance is high. You can borrow airtime or\n\t\tdata when your balance is lower than N49.99{end} {bold}{magenta} ")
                return_menu()

        else:
            print(f'{red}::No query returned{end}{bold}{magenta}')
            return_menu()

    except Exception as e:
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)
        with open('error.txt', 'w') as file:
            file.write(str(e))


def checkAirtimeBal(phone_number):
    try:
        # Query to check and select data bal
        sel_bal = 'SELECT Airtime_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_bal, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            air_bal = result[0]

            sel_bal = 'SELECT Airtime_borrowed_balance FROM Telecom_tbl WHERE Phone_number = %s'
            my_cur.execute(sel_bal, (phone_number,))
            result = my_cur.fetchone()

            if result is not None:
                borrow_bal = result[0]

                if borrow_bal != 0:
                    print_slowly(f'{brt_black_bg}{brt_green}Your airtime balance is N{air_bal}.N-{borrow_bal}{end}    {bold}{magenta}')

                    note = f'''
Console Main Account:N{air_bal}.N-{borrow_bal}
Get 1.5GB @ N200 for Tiktok, dial *312*2#.
                                                                            '''
                    send_notification('ConsoleUssdSms', note, 'ConsoleBalSms')

                    return_menu()

                else:
                    print()
                    engine.say(f"your airtime balance is {air_bal}Naira")
                    engine.runAndWait()
                    print_slowly(f'{brt_black_bg}{brt_green}Your airtime balance is N{air_bal}{end}    {bold}{magenta}')

                    note = f'''
Console Main Account:N{air_bal}.
Get 1.5GB @ N200 for Tiktok, dial *312*2#.
                                                                            '''
                    send_notification('ConsoleUssdSms', note, 'ConsoleBalSms')

                    return_menu()

        else:
            engine.say(f"No query returned")
            engine.runAndWait()
            print(f'{brt_red}::Error:No query returned{end} {bold}{magenta}')
            time.sleep(4)
            clear()
            return_menu()

    except Exception as e:
        engine.say(f"an error occurred")
        engine.runAndWait()
        print(f'{brt_red}::An error occurred: ', e, end, bold, magenta)


def check_data():
    try:
        while True:
            wait()
            print()
            print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            phone_number = input('>>> ').strip()
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (phone_number))
            if user:
                wait_and_count()
                checkDataBal(phone_number)

                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break

            else:
                invalid()
                time.sleep(4)
                clear()
                check_data()

    except Exception as e:
        print('Oops something went wrong: ', e)
        with open('error.txt', 'w') as file:
            file.write(str(e))


def check_airtime():
    try:
        while True:
            wait()
            print()
            print(f'{brt_yellow}Please enter phone number again to continue:{end} {bold}{magenta} ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            phone_number = input('>>> ').strip()
            check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
            user = my_cur.execute(check_num, (phone_number))
            if user:
                wait_and_count()
                checkAirtimeBal(phone_number)

                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break

            else:
                invalid()
                time.sleep(4)
                clear()
                check_data()

    except Exception as e:
        print('Oops something went wrong: ', e)
        with open('error.txt', 'w') as file:
            file.write(str(e))




# check_data()
