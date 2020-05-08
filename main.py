import random
import string
from datetime import datetime
import os
import sys

staff = ['praise', 'praiseinua', 'p@snbank.com', 'Praise Inua']
f = open('log.txt', 'w+')
f.write(str(staff))
f.close()

print('WELCOME!')
print('___________________________')
staff_choice = input('A. login \nPress any key to Close App \nChoose action: ').lower()
if staff_choice == 'a':
    username = str(input('Enter your username: '))
    password = str(input('Enter your password: '))
    f = open('log.txt', 'r')
    if username != staff[0] or password != staff[1]:
        print('Invalid username or password. Try again')
    else:
        print('Logged in! Please select an operation: ')
        logged_in = True
        while logged_in:
            session = open('session.txt', 'w+')
            session.write(username + ' logged in at ' + (datetime.now().strftime('%d/%m/%y %H:%M:%S')))
            session.close()
            action = input(
                'A. Create New Bank Account \nB. Check Account Details \nC. Logout \n>> ').lower()
            if action == 'a':
                acct_name = input('Enter Account Name: ')
                acct_type = input('Enter Account Type: ')
                acct_email = input('Enter account email: ')
                opening_balance = float(input('Opening balance: '))
                acct_number = ''.join([random.choice(string.digits) for x in range(10)])
                print(f'Account number: {acct_number}')
                acct_details = open('customer.txt', 'w')
                acct_details.write(acct_name + ', ')
                acct_details.write(acct_type + ', ')
                acct_details.write(acct_email + ', ')
                acct_details.write(str(opening_balance) + ', ')
                acct_details.write(acct_number)
                acct_details.close()

            elif action == 'b':
                get_acct_number = input('Please enter account number: ')
                acct_details = open('customer.txt', 'r')
                acct_details_dict = {}
                for row in acct_details:
                    field = row.split(':')
                    key = 'account number'
                    value = field[0][-10:]
                    print(value)
                    acct_details_dict[key] = value
                while get_acct_number != acct_details_dict[key]:
                    retry = input('Invalid account number. Try again: ')

                else:
                    acct_details = open('customer.txt')
                    print(acct_details.read())

            elif action == 'c':
                if os.path.exists('session.txt'):
                    os.remove('session.txt')
                    print('session file removed!')
                    break

            else:
                print('Please select a valid option!')

        # break

    f.close()
else:
    sys.exit('Program Terminated!')

