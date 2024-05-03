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

#db code for transaction
def buyData(phone_number,data_amount,cost):
    while True:
        # query to select airtime bal
        sel_balance = 'SELECT Airtime_balance,Data_balance from Telecom_tbl WHERE Phone_number =%s'
        my_cur.execute(sel_balance, (phone_number,))
        result = my_cur.fetchone()

        if result is not None:
            current_balance = result[0]
            current_data_bal = result[1]
            if current_balance >= cost:

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
                print('Insufficient Airtime balance.')
                break

        else:
            print('Error: No query returned')
            break

    print(end='\r')
    print(end='\r')
    clear()



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
                        wait()
                        print(f"You have been credited with {data_amount}mb @ ₦{cost} valid for 24hours.")
                        time.sleep(3)
                        clear()

                        #Query to select current balance from db
                        sel_balance = 'SELECT Airtime_balance,Data_balance from Telecom_tbl WHERE Phone_number =%s'
                        my_cur.execute(sel_balance,(phone_number,))
                        result = my_cur.fetchone()

                        #Check if bal is sufficient
                        if result is not None:
                            current_balance = result[0]
                            current_data_bal = result[1]
                            if current_balance >= cost:

                                #Deduct from current bal
                                new_balance = current_balance - 25

                                #Add to data bal
                                new_data_bal = current_data_bal + data_amount

                                #Query to update bal
                                update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s WHERE Phone_number = %s'
                                my_cur.execute(update_bal, (new_balance,new_data_bal, phone_number))

                                #commit change
                                db.commit()
                                break

                            else:
                                print('Insufficient Airtime balance. Please recharge and try again')
                                print(end='\r')
                                print(end='\r')
                                time.sleep(1)
                                clear()


                                break

                        else:
                            print('Error: No results returned from query')
                            break

                    else:
                        print('Invalid number. Please try again')

                elif ans == '2':
                    wait_and_count()
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 100
                        cost = 50
                        print(f"You have been credited with {data_amount}mb @ ₦{cost} valid for 7 days.")
                        time.sleep(3)
                        clear()

                        # Query to select current balance from db
                        sel_balance = 'SELECT Airtime_balance,Data_balance from Telecom_tbl WHERE Phone_number =%s'
                        my_cur.execute(sel_balance, (phone_number,))
                        result = my_cur.fetchone()

                        # Check if bal is sufficient
                        if result is not None:
                            current_balance = result[0]
                            current_data_bal = result[1]
                            if current_balance >= cost:

                                # Deduct from current bal
                                new_balance = current_balance - cost

                                # Add to data bal
                                new_data_bal = current_data_bal + data_amount

                                # Query to update bal
                                update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s WHERE Phone_number = %s'
                                my_cur.execute(update_bal, (new_balance, new_data_bal, phone_number))

                                # commit change
                                db.commit()
                                break

                            else:
                                print('Insufficient Airtime balance. Please recharge and try again')
                                print(end='\r')
                                print(end='\r')
                                time.sleep(1)
                                clear()
                                break

                        else:
                            print('Error: No results returned from query')

                elif ans == '3':
                    wait_and_count()
                    phone_number = input('Please enter phone number again to continue\n\t>>> ')
                    check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                    user = my_cur.execute(check_num, (phone_number))
                    if user:
                        data_amount = 200
                        cost = 150
                        print(f"You have been credited with {data_amount}mb  @ N{cost} valid for 30days.")
                        time.sleep(3)
                        clear()

                        #query to select airtime bal
                        sel_balance = 'SELECT Airtime_balance,Data_balance from Telecom_tbl WHERE Phone_number =%s'
                        my_cur.execute(sel_balance, (phone_number,))
                        result = my_cur.fetchone()

                        if result is not None:
                            current_balance = result[0]
                            current_data_bal = result[1]
                            if current_balance >= cost:

                                #Deduct from bal
                                new_balance = current_balance - cost

                                # Add to data bal
                                new_data_bal = current_data_bal + data_amount

                                # Query to update bal
                                update_bal = 'UPDATE Telecom_tbl SET Airtime_balance = %s, Data_balance = %s WHERE Phone_number = %s'
                                my_cur.execute(update_bal, (new_balance, new_data_bal, phone_number))

                                #Commit change
                                db.commit()
                                break

                            else:
                                print('Insufficient Airtime balance.')
                                print(end='\r')
                                print(end='\r')
                                clear()
                                break

                        else:
                            print('Error: No query returned')
                            break

                    else:
                        return 'Invalid Phone number'

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
                    print(f"You have been credited with {data_amount}MB @ ₦{cost} valid for 24hours.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,50,25)
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
                    print(f"You have been credited with {data_amount}MB @ ₦{cost} valid for 7 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,100,50)
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
                    print(f"You have been credited with {data_amount}MB  @ N{cost} valid for 30days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
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
                    print(f"You have been credited with {data_amount}MB @ ₦{cost} valid for 24hours.")
                    time.sleep(3)
                    clear()

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
                    print(f"You have been credited with {data_amount}MB @ ₦{cost} valid for 2 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
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
                    print("You have been credited with 1G @ N200 valid for 24hours.")
                    time.sleep(3)
                    clear()

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
                    print("You have been credited with 1.5GB @ ₦200 valid for 3 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
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
                    print("You have been credited with 200MB @ ₦100 valid for 24hours.")
                    time.sleep(3)
                    clear()

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

            elif ans == 2:
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 350
                    cost = 150
                    print("You have been credited with 350MB @ ₦150 valid for 2 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == 3:
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1000
                    cost = 200
                    print("You have been credited with 1GB @ N200 valid for 24hours.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
                    db.commit()

                    print(end='\r')
                    print(end='\r')
                    clear()
                    break

                else:
                    invalid()
                    break

            elif ans == 4:
                wait_and_count()
                phone_number = input('Please enter phone number again to continue\n\t>>> ')
                check_num = 'SELECT * FROM Telecom_tbl WHERE phone_number = %s'
                user = my_cur.execute(check_num, (phone_number))

                # check if user is in db
                if user:
                    data_amount = 1500
                    cost = 250
                    print("You have been credited with 1.5GB @ ₦250 valid for 3 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
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
                    print("You have been credited with 150mb @ ₦50 valid for 24hours.")
                    time.sleep(3)
                    clear()

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
                    print("You have been credited with 350mb @ ₦100 valid for 7 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
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
                    print("You have been credited with 1G @ N250 valid for 7 days.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number,data_amount,cost)
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
                    print("You have been credited with 150MB @ ₦50 valid for 24hours.")
                    time.sleep(3)
                    clear()

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
                    print("You have been credited with 50MB @ ₦20 valid for 24hours.")
                    time.sleep(3)
                    clear()

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
                    print("You have been credited with 100MB @ ₦50 valid for 24hours.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number, data_amount, cost)
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
                    print("You have been credited with 500MB @ ₦250 valid for 24hours.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number, data_amount, cost)
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
                    print("You have been credited with 750MB @ ₦200 valid for 24hours.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number, data_amount, cost)
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
                    print("You have been credited with 1GB @ ₦300 valid for 24hours.")
                    time.sleep(3)
                    clear()

                    buyData(phone_number, data_amount, cost)
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
        print('h')

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





