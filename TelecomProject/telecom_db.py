import pymysql as sql
import random
import time
import sys

db = sql.connect(
    user='vicjnr',
    password='kevjnr7890',
    host='localhost',
    database='Telecom_db'
)

my_cur = db.cursor()

#Error handlingd
# try:
phone_number = ''
airtime_balance = ''

    #Generate user phone number
def gen_number():
    global phone_number
    fnum = '080'

    last_num = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    phone_number = fnum + last_num
    return phone_number

def re_charge():
    global airtime_balance
    airtime_balance = (input('Enter amount to recharge\n\t>>> '))
    if airtime_balance.isnumeric():
        pass
    else:
        print('Invalid amount')
        re_charge()
#promp first time user's to register their number
def register_num():
    global airtime_balance
    print('Welcome!')
    time.sleep(1)
    print('Please register your sim with us')
    time.sleep(2)
        #Creating an empty list
    _list = []
    first_name = input('Enter first name\n\t>>> ').capitalize()
    last_name = input('Enter last name\n\t>>> ').capitalize()
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
        time.sleep(1)
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

        return 'success'


    except ValueError:
        print('invalid sim registration')



#Function to ask a user if they already have their number registered to the db or not
def option():
    print('Welcome to our service\nWould you like to:')
    time.sleep(1)
    opt = input('1. Register number\n'
                '2. Enter number\n\t'
                '>>> '
                )
    if opt == '1':
        time.sleep(0.5)
        register_num()

    elif opt == '2':
        print('gg')
