import random
import time

from telussd import *


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
    fnum = random.choice(['080','070','090','081'])

    last_num = ''.join([str(random.randint(0, 9)) for _ in range(8)]).strip()
    phone_number = fnum + last_num
    return phone_number


def re_charge():
    global airtime_balance
    print('~' * 50)
    airtime_balance = input('Enter amount to recharge\n\t>>> ')
    if airtime_balance.isnumeric():
        pass
    else:
        print('~' * 50)
        print('Invalid Entry. Please enter a numeric value')
        re_charge()


# prompt first time user's to register their number
def register_num():
    global airtime_balance
    print('~' * 50)
    print('Welcome!')
    time.sleep(1)
    print('Please register your sim with us')
    time.sleep(2)
    #Creating an empty list
    _list = []
    while True:
        print('~' * 50)
        first_name = str(input('Enter first name\n\t>>> ')).capitalize()
        if first_name.isalpha():
            break
        time.sleep(0.5)
        print('~' * 50)
        print('First name is required and must contain only alphabetic characters. Please try again.')
        time.sleep(1)
    while True:
        print('~' * 50)
        last_name = str(input('Enter last name\n\t>>> ')).capitalize()
        if last_name.isalpha():
            break
        time.sleep(0.5)
        print('~' * 50)
        print('Last name is required and must contain only alphabetic characters. Please try again.')
        time.sleep(1)

    #Error handling
    try:
        re_charge()
        gen_number()
        _list.append(first_name)
        _list.append(last_name)
        _list.append(gen_number())
        details = ' '.join(_list)
        sp_details = details.split(' ')
        full_name = sp_details[0] +' '+ sp_details[1]
        # print(full_name)
        # print(sp_details)
        wait_and_count()
        time.sleep(1)
        print('~' * 50)
        print('Registration successful')
        time.sleep(2)
        print(f'Full name: {full_name}\nPhone number: {sp_details[-1]}')
        time.sleep(1)
        print(f'Account has been credited with N{airtime_balance}\nAcct.bal:{airtime_balance} ')

        # Sql insert query
        insert_dt = 'INSERT INTO telecom_tbl(first_name,last_name,phone_number,airtime_balance) VALUES (%s,%s,%s,%s)'

        #Execute query with user input
        my_cur.execute(insert_dt,(first_name,last_name,phone_number,airtime_balance))

        db.commit()
        my_cur.close()
        db.close()

        time.sleep(2)
        print('~' * 50)
        print('Welcome to our service')
        time.sleep(1)
        return ussd_code()

    except Exception:
        print('~' * 50)
        print('Sim registration failed')


# Function for if user is already registered
def already_user():
    print('~' * 50)
    phone_number = input('Enter phone number\n\t>>> ')

    try:
        #Query to check if number already exist's in db
        check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
        my_cur.execute(check_num,(phone_number))
        user = my_cur.fetchone()

        #If user is already in the db the code proceed's to show ussd
        while True:
            if user:
                wait()
                print('~' * 50)
                print('1. Continue')
                print('2. Cancel')
                print('~' * 50)
                res = input('\t>>> ')
                if res == '1' and res.isnumeric():
                    wait_and_count()
                    print('~' * 50)
                    print('Welcome to our service')
                    wait()
                    ussd_code()
                    break

                elif res == '2' and res.isnumeric():
                    print('~' * 50)
                    print('Thank you for using our service')
                    break

                else:
                    print('~' * 50)
                    print('Invalid response. Please try again')
                    time.sleep(0.5)
                    print('Service time out')

            else:
                print('~' * 50)
                print('Invalid number\nPlease register your number to continue this process')
                break

    except Exception as e:
        print('~' * 50)
        print(f"An error occurred: {e}")


# Function to ask a user if they already have their number registered to the db or not
def option():
    print('~' * 50)
    print('Welcome to our service')
    time.sleep(1)
    print('Would you like to:')
    time.sleep(1)
    print('1. Register number')
    time.sleep(0.8)
    print('2. User')

    while True:
        print('~' * 50)
        opt = input('\t>>> ')
        if opt == '1' and opt.isnumeric():
            wait()
            time.sleep(1)
            register_num()
            break

        elif opt == '2' and opt.isnumeric():
            wait()
            already_user()
            break

        else:
            time.sleep(1)
            print('~' * 50)
            print('Invalid Response. Please try again')
            time.sleep(0.5)


option()