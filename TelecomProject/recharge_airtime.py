from TelecomProject.ussd_short import wait, wait_and_count, clear, print_slowly, out, invalid, countdown_timer
from animation.colors import *
from TelecomProject.notification import send_notification
import time
from TelecomProject.return_menu import return_menu
import pymysql
import pyttsx3
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


def recharge():
    try:
        while True:
            clear()
            print()
            print(f'{brt_black_bg}{brt_cyan}\tRecharge airtime\n{end}  {bold}{magenta} ')
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
                            # clear()

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
                                    f'{brt_black_bg}{brt_yellow}The recharge of N{amount}.00 was successful\nAcct.bal N{amount}.00{end}{bold}{magenta}')

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
                                        print_slowly(f'{brt_black_bg}{brt_yellow}N{borrow_bal} deducted from account{end}')
                                        time.sleep(3)
                                        clear()
                                        break

                                    else:
                                        pass
                                        break

                                else:
                                    time.sleep(0.6)
                                    engine.say('no query returned')
                                    engine.runAndWait()
                                    print(f'{brt_red}::No query returned{end} {bold}{magenta}')
                                    time.sleep()
                                    clear()

                            else:
                                invalid()
                                time.sleep(3)
                                clear()

                        else:
                            time.sleep(0.8)
                            engine.say(f"amount must be more than 30 naira")
                            engine.runAndWait()
                            print(f'{brt_red}::Amount must be more than N30{end} {bold}{magenta}')
                            time.sleep(3)
                            clear()

                    else:
                        out()
                        time.sleep(3)
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


clear()
    # recharge()