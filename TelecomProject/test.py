import time
from TelecomProject.ussd_short import wait, countdown_timer, clear, print_slowly, invalid, out
import pyttsx3
from animation.colors import *
import re
from TelecomProject.main_menu import ussd_code
# from TelecomProject.data_plan import dataPlan
# from TelecomProject.social_bundle import social_bundles
# from TelecomProject.borrow_credit import borrow_credit
# from TelecomProject.roaming_int import roaming_int
# from TelecomProject.video_pack import video_pack
# from TelecomProject.gift_data import gift_data
# from TelecomProject.recharge_airtime import recharge
# from TelecomProject.chat_zigi import chat_zigi

engine = pyttsx3.init()


def main_menu():
    from TelecomProject.data_plan import dataPlan
    from TelecomProject.social_bundle import social_bundles
    from TelecomProject.borrow_credit import borrow_credit
    from TelecomProject.roaming_int import roaming_int
    from TelecomProject.video_pack import video_pack
    from TelecomProject.gift_data import gift_data
    from TelecomProject.recharge_airtime import recharge
    from TelecomProject.chat_zigi import chat_zigi
    wait()
    print()
    engine.say(f'Welcome to our USSD Service.')
    engine.runAndWait()
    print_slowly(f"\t\t{brt_black_bg}{brt_blue}{bold}Welcome to our USSD Service.{end}   {bold}{magenta}")
    time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'data plan')
    # engine.runAndWait()
    # print_slowly(f'1. Data Plan')
    # time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'social bundles')
    # engine.runAndWait()
    # print_slowly('2. Social Bundles')
    # time.sleep(0.3)
    # engine.say(f'borrow credit')
    # engine.runAndWait()
    # # time.sleep(0.3)  # Wait for 1 second
    # print_slowly('3. Borrow Credit')
    # time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'roaming internationally')
    # engine.runAndWait()
    # print_slowly("4. Roaming\\int'l")
    # time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'video pack')
    # engine.runAndWait()
    # print_slowly('5. Video Pack')
    # time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'gift data')
    # engine.runAndWait()
    # print_slowly('6. Gift data')
    # time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'recharge airtime')
    # engine.runAndWait()
    # print_slowly('7. Recharge Airtime')
    # time.sleep(0.3)  # Wait for 1 second
    # engine.say(f'chat with zigi.')
    # engine.runAndWait()
    # print_slowly(f'8. Chat with Zigi')

    print(end='\n')
    print("+~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~+")
    print(
        f'|   {brt_black_bg}{brt_yellow}1. DATA PLAN{end}    {bold}{magenta}|  {brt_black_bg}{brt_yellow}2. SOCIAL BUNDLES{end} {bold}{magenta}| {brt_black_bg}{brt_yellow}3. BORROW CREDIT{end} {bold}{magenta}|')
    print("+~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~+")
    print(
        f'|   {brt_black_bg}{brt_yellow}4. ROAMING\\INT\'L{end}{bold}{magenta}|  {brt_black_bg}{brt_yellow}5. VIDEO PACK{end}     {bold}{magenta}|   {brt_black_bg}{brt_yellow}6. GIFT DATA{end}   {bold}{magenta}|')
    print("+~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~+")
    print(
        f'|   {brt_black_bg}{brt_yellow}7. RECHARGE AIRTIME{end}       {bold}{magenta}|        {brt_black_bg}{brt_yellow}8. CHAT WITH ZIGI{end} {bold}{magenta}   |         ')
    print("+~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~+")
    menu = input('>>> ').strip()

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

    elif re.search('^.*(back|return).*$', menu, re.IGNORECASE):
        clear()
        ussd_code()

    else:
        engine.say(f'invalid')
        engine.runAndWait()
        print('Invalid Entry\nTry again\n')
        time.sleep(4)
        clear()
        main_menu()

    clear()
