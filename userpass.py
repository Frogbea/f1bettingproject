# USERNAME and password component
#**********IMPORTS***************
import csv, pandas as p

#********VARIBLES****************


#*************FUNCTIONS*************
def newUser():
    global username
    username = input('Please enter a username:')
    while True:
        password = input('Please create a password:')
        password2 = input('Please retype your password:')
        if password != password2:
            print('!ERROR! passwords do not match')
            continue
        else:
            break
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def previousUser():
    while True:

        username = input('Please enter your username:')
        password = input('Please enter your password:')
        data = []
        with open('users.csv') as file:
            check = csv.reader(file)
            for row in check:
                data.append(row)
        col = [x[0] for x in data]
        if username in col and password in col:
            print('Welcome back ', username)
            break
        else:
            print('!ERROR!User not found')


# MAIN***************************************************************************************************
while True:
    choice = input('Do you want to:\n 1.Sign in\n 2.Sign up \n Type what you would like to do:').lower()
    if choice =='sign in':
        previousUser()
        break
    elif choice == 'sign up':
        newUser()
        print('Welcome to the program ', username, ' hope you enjoy!!')
        break
    else:
        print('!ERROR! Please type in your command correctly.')


