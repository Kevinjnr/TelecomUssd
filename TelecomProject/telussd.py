


## menu function
def main_menu():
    menu = input("Welcome to our USSD Service.\n"
                 '1. Data Plan\n'
                 '2. Social Bundles\n'
                 '3. Borrow Credit\n'
                 "4. Roaming\\int'l\n"
                 '5. Video Pack\n'
                 '6. Gift data\n'
                 '7. Chat with Zigi\n\t'

                 '>>> '
                 )

    if menu == '1':
        print('h')

    elif menu == '2':
        print('f')

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




