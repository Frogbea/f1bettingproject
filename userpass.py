# USERNAME and password component
#**********IMPORTS***************
import csv

#********VARIBLES****************
username = 'blank'
password = 'blank'

#*************FUNCTIONS*************
def newUser():
    username = input('Please enter a username:')
    password = input('Please create a password')

def previousUser():
    print('sign in')




# MAIN***************************************************************************************************
while True:
    choice = input('Do you want to:\n 1.Sign in\n 2.Sign up \n Type what you would like to do:').lower()
    if choice =='sign in':
        previousUser()
        break
    elif choice == 'sign up':
        newUser()
        break
    else:
        print('!ERROR! Please type in your command correctly.')
   

with open('users.csv', 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)

    

with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["SNo", "Name", "Subject"])
    writer.writerow([1, "Ash Ketchum", "English"])
    writer.writerow([2, "Gary Oak", "Mathematics"])
    writer.writerow([3, "Brock Lesner", "Physics"])

