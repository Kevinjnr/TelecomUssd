import random
import pymysql
import time
import sys
import os
import pyttsx3
import datetime
from TelecomProject.main_menu import ussd_code
from TelecomProject.ussd_short import wait, wait_and_count, clear, print_slowly, countdown_timer
from animation.colors import *
from TelecomProject.notification import send_notification
import re

engine = pyttsx3.init()

db = pymysql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()

phone_number = ''
airtime_balance = ''


# Generate user phone number
def gen_number():
    global phone_number
    fnum = random.choice(['080', '070', '090', '081'])

    last_num = ''.join([str(random.randint(0, 9)) for _ in range(8)]).strip()
    phone_number = fnum + last_num
    return phone_number


# recharge during registration code
def re_charge():
    global airtime_balance
    print(f'{brt_yellow}\nEnter amount to recharge:{end} ')
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    airtime_balance = input('>>> ').strip()
    if airtime_balance.isnumeric():
        pass
    else:
        print(f'{brt_red}::Invalid Entry. Please enter a numeric value{end}')
        re_charge()


# prompt first time user's to register their number
def register_num():
    global airtime_balance, first_name
    print()
    engine.say("Welcome")
    engine.runAndWait()
    print_slowly(f'{brt_yellow}{bold}Welcome!{end}')
    time.sleep(0.3)
    engine.say("Please kindly register your number here by filling the following question")
    engine.runAndWait()
    print_slowly(f'{brt_yellow}{bold}Please kindly register your number here by filling the following question{end}\n')
    time.sleep(2)
    # Creating an empty list
    _list = []
    while True:
        engine.say("\nEnter first name")
        engine.runAndWait()
        print(f'{brt_yellow}Enter first name:{end} ')
        print('~~~~~~~~~~~~~~~~~')
        first_name = input('>>> ').strip().capitalize()
        if first_name.isalpha():
            break
        time.sleep(0.5)

        engine.say("First name is required and must contain only alphabetic characters. Please try again.")
        engine.runAndWait()
        print(f'{brt_red}::First name is required and must contain only alphabetic characters. Please try again.{end} ')
        time.sleep(4)
        clear()
    if re.search('^.*(back|return).*$', first_name, re.IGNORECASE):
        # If the user types 'back' or 'return', exit the function.
        clear()
        return option()

    while True:
        engine.say("Enter last name.")
        engine.runAndWait()
        print(f'{brt_yellow}\nEnter last name:{end} ')
        print('~~~~~~~~~~~~~~~~~')
        last_name = input('>>> ').capitalize().strip()
        if last_name.isalpha():
            break
        time.sleep(0.5)

        engine.say("Last name is required and must contain only alphabetic characters. Please try again.")
        engine.runAndWait()
        print(f'{brt_red}::Last name is required and must contain only alphabetic characters. Please try again.{end}{bold}{magenta}')
        time.sleep(3)
        clear()

    # Error handling
    try:
        re_charge()
        gen_number()
        _list.append(first_name)
        _list.append(last_name)
        _list.append(gen_number())
        details = ' '.join(_list)
        sp_details = details.split(' ')
        full_name = sp_details[0] + ' ' + sp_details[1]
        # print(full_name)
        # print(sp_details)
        countdown_timer('Creation of number', 'in', countdown=5)
        clear()
        time.sleep(1)
        print()
        engine.say("Registration successful.")
        engine.runAndWait()
        print_slowly(f'{brt_blue}{bold}Registration successful!\n')
        time.sleep(2)
        engine.say(f"Hello!, {full_name} Thank you for registering with us..")
        engine.runAndWait()
        print_slowly(f'Hello!, {full_name} Thank you for registering with us.')
        time.sleep(1)
        engine.say(f'Phone number: {sp_details[-1]}')
        engine.runAndWait()
        print_slowly(f'Phone number: {sp_details[-1]}{end}{bold}{magenta}')
        time.sleep(1)
        note = f'''
Thank you for registering with Console Ussd 
Name: {full_name}
Phone Number: {sp_details[-1]} 
'''
        send_notification('Console ussd sms', note, 'ConsoleSms')
        print()
        engine.say(f'Account has been credited with {airtime_balance}naira\nAccount balance:{airtime_balance}naira')
        engine.runAndWait()
        print_slowly(f'{brt_blue}Account has been credited with N{airtime_balance}\nAcct.bal:{airtime_balance} {end}{bold}{magenta} ')
        time.sleep(1)
        clear()

        # Sql insert query
        insert_dt = 'INSERT INTO telecom_tbl(first_name,last_name,phone_number,airtime_balance) VALUES (%s,%s,%s,%s)'

        # Execute query with user input
        my_cur.execute(insert_dt, (first_name, last_name, phone_number, airtime_balance))

        db.commit()
        my_cur.close()
        db.close()

        while True:

            engine.say("Press 1 to Continue this process.")
            engine.runAndWait()
            time.sleep(0.7)
            engine.say("press 2 to Cancel.")
            engine.runAndWait()
            print(f'{bold}{brt_yellow}1. Continue{end}  {bold}{magenta}|{end}  {bold}{brt_yellow}2. Cancel{end}')
            print(f'{bold}{magenta}~~~~~~~~~~~     ~~~~~~~~~~{end} {bold}{magenta}')
            time.sleep(0.7)
            opt = input('\t>>> ').strip()

            if opt == '1':
                time.sleep(2)
                clear()
                print()
                engine.say("Welcome to our service.")
                engine.runAndWait()
                print_slowly(f'{brt_black_bg}{brt_yellow}Welcome to our service{end}    {bold}{magenta}')
                time.sleep(1)
                ussd_code()

            elif opt == '2':
                print()
                engine.say("Thank you for using our service.")
                engine.runAndWait()
                print_slowly(f'{brt_yellow}Thank you for using our service{end}')
                countdown_timer(_register='System logging off in', countdown=5)
                sys.exit()

            elif re.search('^.*(back|return).*$', opt, re.IGNORECASE):
                # If the user types 'back' or 'return', exit the function.
                return option()

            else:
                engine.say("Invalid Entry. Service time out.")
                engine.runAndWait()
                print(f'{brt_red}::Invalid Entry. Service time out{end}{bold}{magenta}')
                time.sleep(3)
                clear()

    except Exception as e:
        engine.say("Sim registration failed:")
        engine.runAndWait()
        print(f'{brt_red}::Sim registration failed: ', e)


# Function for if user is already registered
def already_user():
    print()
    engine.say("Enter phone number:")
    engine.runAndWait()
    print(f'{brt_yellow}Enter phone number: {end} {bold}{magenta}')
    print('~~~~~~~~~~~~~~~~~~')
    phone_number = input('>>> ').strip()

    try:
        # Query to check if number already exists in db
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        my_cur.execute(check_num, (phone_number))
        user = my_cur.fetchone()

        # If user is already in the db the code proceeds to show ussd
        while True:
            if user:
                try:
                    wait()
                    check_name = f'SELECT First_name, Last_name FROM Telecom_tbl WHERE phone_number = %s'
                    my_cur.execute(check_name, (phone_number))
                    result = my_cur.fetchone()
                    if result:
                        # Convert the tuple to a string
                        f_name, l_name = result
                        full_name = f"{f_name} {l_name}"
                        # name = (f"Full Name: {full_name}")
                        note = f'''
Hello {full_name} thank you for choosing console ussd.
Get data for price as low as N25 
                        '''
                        send_notification('Console login sms', note, 'ConsoleLogSms')
                    else:
                        print("No user found with that phone number.")
                finally:
                    # Close the connection
                    my_cur.close()
                print()
                engine.say("press 1 to Continue this process")
                engine.runAndWait()
                engine.say("press 2 to cancel this process")
                engine.runAndWait()
                print(f'{bold}{brt_yellow}1. Continue{end}  {bold}{magenta}|{end}  {bold}{brt_yellow}2. Cancel{end} {bold}{magenta}')
                print(f'{bold}{magenta}~~~~~~~~~~~     ~~~~~~~~~~{end} {bold}{magenta}')
                res = input(f'\t>>> ').strip()
                if res == '1' and res.isnumeric():
                    wait()
                    engine.say("Welcome to our service")
                    engine.runAndWait()
                    print(f'\n\t{brt_black_bg}{brt_green}Welcome to our service{end}   {bold}{magenta}')
                    ussd_code()
                    break

                elif res == '2' and res.isnumeric():
                    clear()
                    print()
                    engine.say("Thank you for using our service")
                    engine.runAndWait()
                    print_slowly(f'{brt_black_bg}{brt_yellow}Thank you for using our service{end}')
                    countdown_timer(_register='System logging off in', countdown=5)
                    break

                elif re.search('^.*(back|return).*$', res, re.IGNORECASE):
                    # If the user types 'back' or 'return', exit the function.
                    option()

                else:
                    print()
                    engine.say("invalid response. Please try again.")
                    engine.runAndWait()
                    print(f'{brt_red}::Invalid response. Please try again{end} {bold}{magenta}')
                    time.sleep(3)
                    clear()

            else:
                print()
                engine.say("invalid number. Please enter a valid number to continue this process")
                engine.runAndWait()
                print(f'{brt_red}::Invalid number\nPlease enter a valid number to continue this process')
                time.sleep(5)
                clear()
                already_user()

    except Exception as e:
        engine.say("An error occurred")
        engine.runAndWait()
        print(f"{brt_red}An error occurred: {e}")
        time.sleep(5)
        clear()
        option()


# Function to ask a user if they already have their number registered to the db or not
def option():
    engine.say("Welcome to our service")
    engine.runAndWait()

    while True:
        print()
        print_slowly(f'\t\t{brt_black_bg}{brt_green}{bold}{italic}Welcome to our service{end}   {bold}{magenta}\n')
        time.sleep(0.3)

        engine.say("Would you like to: ")
        engine.runAndWait()

        print_slowly(f'{brt_yellow}Would you like to:{end}        {magenta}')
        print('~~~~~~~~~~~~~~~~~~')
        time.sleep(0.3)

        engine.say("1. Register number")
        engine.runAndWait()

        engine.say("2. User")
        engine.runAndWait()

        print(end='\n')
        print(bold, magenta, "+~~~~~~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~+"
              , sep='')
        print(f"|      {brt_black_bg}{brt_yellow}1. REGISTER NUMBER{end}   {bold}{magenta}|     "
              f"{brt_black_bg}{brt_yellow}2. USER{end}     {bold}{magenta}        |        ")
        print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~+")
        opt = input('\t>>> ').strip()
        if opt == '1' and opt.isnumeric():
            wait()
            register_num()
            break

        elif opt == '2' and opt.isnumeric():
            wait()
            already_user()
            break

        else:
            time.sleep(1)
            print(f'{brt_red}::Invalid Response. Please try again{end}')
            time.sleep(3)
            clear()


clear()

# option()
