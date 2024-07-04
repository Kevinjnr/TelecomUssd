import time
from animation.colors import *
from TelecomProject.ussd_short import invalid, out, wait, clear, print_slowly
import pyttsx3

engine = pyttsx3.init()


def chat_zigi():
    from TelecomProject.return_menu import return_menu
    wait()
    print()
    engine.say(f""" Yello! Need help, chat with Zigi on preferred network such
                   as;whatsapp,facebook messenger
                   Web and Telegram.Details via sms.

    """)
    engine.runAndWait()
    time.sleep(0.7)
    message = f'''\t\t\t\t{brt_black_bg}{brt_cyan}{italic}{bold}Y'ello! Need help, chat with Zigi on preferred network such{end}
                   {brt_black_bg}{brt_cyan}{italic}{bold}\tas;whatsapp,facebook messenger{end}
                   {brt_black_bg}{brt_cyan}{italic}{bold}Web and Telegram.Details via sms.{end} {bold}{magenta}
                   '''
    print_slowly(message)
    time.sleep(7)
    clear()
    return_menu()


clear()
