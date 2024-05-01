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

#Social bundles code
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

def whatsapp():
    wait()
    while True:
        print("\t\tWhatsapp\n")
        print("1. Daily @ ₦25 for 25MB")
        time.sleep(1)
        print("2. Weekly @ ₦50 for 50MB")
        time.sleep(1)
        print("3. Monthly @ ₦150 for 150MB")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 25mb @ ₦25 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 50mb @ ₦50 valid for 7 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 3:
                wait_and_count()
                print("You have been credited with 150mb  @ N150 valid for 30days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            else:
                print('Invalid input. Please try again')
                whatsapp()


        else:
            print("Invalid character. Please try aagin")
            whatsapp()
    clear()
    print(end='\r')
    print(end='\r')

#Facebook
def facebook():
    wait()
    while True:
        print("\t\tFacebook\n")
        print("1. Daily @ ₦25 for 25MB")
        time.sleep(1)
        print("2. Weekly @ ₦50 for 50MB")
        time.sleep(1)
        print("3. Monthly @ ₦150 for 150MB")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 25mb @ ₦25 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 50mb @ ₦50 valid for 7 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 3:
                wait_and_count()
                print("You have been credited with 150mb  @ N150 valid for 30days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break


        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

#Instagram
def instagram():
    wait()
    while True:
        print("\t\tInstagram\n")
        print("1. ₦100 for 250MB/1 day.")
        time.sleep(1)
        print("2. ₦100 for 350MB/2 days.")
        time.sleep(1)
        print("3. ₦200 for 1GB/1 day.")
        time.sleep(1)
        print("4. ₦200 for 1GB/3-days.")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 250mb @ ₦100 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 350mb @ ₦100 valid for 2 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 3:
                wait_and_count()
                print("You have been credited with 1G @ N200 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 4:
                wait_and_count()
                print("You have been credited with 1G @ ₦200 valid for 3 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break


        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

#Tiktok
def tiktok():
    wait()
    while True:
        print("\t\tTiktok\n")
        print("1. ₦100 for 5MB/1 day.")
        time.sleep(1)
        print("2. ₦100 for 350MB/2 days.")
        time.sleep(1)
        print("3. ₦200 for 1GB/1 day.")
        time.sleep(1)
        print("4. ₦200 for 1GB/3-days.")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 5mb @ ₦100 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 350mb @ ₦100 valid for 2 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 3:
                wait_and_count()
                print("You have been credited with 1G @ N200 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 4:
                wait_and_count()
                print("You have been credited with 1G @ ₦200 valid for 3 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break


        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

#All Social Media Bundles
def all_social_bundles():
    wait()
    while True:
        print("\t\tAll Social Bundles\n")
        print("1. Daily @ ₦50 for 150MB.")
        time.sleep(1)
        print("2. Weekly @ ₦100 for 350MB.")
        time.sleep(1)
        print("3. Monthly @ ₦250 for 1GB.")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 150mb @ ₦50 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 350mb @ ₦100 valid for 7 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 3:
                wait_and_count()
                print("You have been credited with 1G @ N250 valid for 7 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break


        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

#YouTube, Instagram and Tiktok
def yit():
    wait()
    while True:
        print("\t\tYoutube,Instagram, and TikTok\n")
        print("1. Daily @ ₦100 for 350MB.")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 150mb @ ₦50 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

#Opera Mini and News
def operamini_and_news():
    wait()
    while True:
        print("\t\tOpera Mini & News\n")
        print("1. ₦20/25MB/1day.")
        time.sleep(1)
        print("2. ₦50/100MB/7days.")
        time.sleep(1)
        print("3. ₦100/300MB/30days.")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 25mb @ ₦20 valid for 24hours.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 100mb @ ₦50 valid for 7 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break

            elif ans == 3:
                wait_and_count()
                print("You have been credited with 300mb @ N250 valid for 30 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break


        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

#Social Mega Bundles
def social_mega_bundles():
    wait()
    while True:
        print("\t\tSocial Mega Bundles\n")
        print("1. 750MB for ₦200 (3 days).")
        time.sleep(1)
        print("2. 1GB for N300 (7 days).")
        time.sleep(1.5)
        ans = input("> ")
        if ans.isdigit():
            ans = int(ans)
            if ans == 1:
                wait_and_count()
                print("You have been credited with 750mb @ ₦200 valid for 3 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                time.sleep(1)
                clear()
                break
            elif ans == 2:
                wait_and_count()
                print("You have been credited with 1G @ ₦300 valid for 7 days.")
                time.sleep(3)
                clear()
                print(end='\r')
                print(end='\r')
                clear()
                break
        else:
            print("Invalid character")
    clear()
    print(end='\r')
    print(end='\r')

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
        ask = input("> ")

        if ask.isdigit():
            ask = int(ask)
            if ask == 1:
                clear()

                print(end='\r')
                print(end='\r')
                whatsapp()
                time.sleep(1)
                exit()
            elif ask == 2:
                clear()
                print(end='\r')
                print(end='\r')
                facebook()
                time.sleep(1)
                exit()

            elif ask == 3:
                clear()
                print(end='\r')
                print(end='\r')
                instagram()
                time.sleep(1)
                exit()

            elif ask == 4:
                clear()
                print(end='\r')
                print(end='\r')
                tiktok()
                time.sleep(1)
                exit()

            elif ask == 5:
                clear()
                print(end='\r')
                print(end='\r')
                all_social_bundles()
                time.sleep(1)
                exit()


            elif ask == 6:
                clear()
                print(end='\r')
                print(end='\r')
                yit()
                time.sleep(1)
                exit()


            elif ask == 7:
                clear()
                print(end='\r')
                print(end='\r')
                operamini_and_news()
                time.sleep(1)
                exit()


            elif ask == 8:
                clear()
                print(end='\r')
                print(end='\r')
                social_mega_bundles()
                time.sleep(1)
                exit()

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






