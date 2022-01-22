#!/usr/bin/env python3
from credentials import Credentials

def main():
    print("This applications enables you to:\ncreate, manage and generate new accounts passwords")
    print("*"*20)
    print("Welcome to pass locker. What would you like to do... ")    
    while True:
        print("Use these short codes: cc - create account, lc -login to your credentials, ex -exit the contact list")
        short_code = input()
        if short_code == 'cc':
            print("Choose a User Name ...")
            username = input()
        elif short_code == 'lc':
            print("Enter your User Name ...")
            username = input()
        elif short_code =='ex':
            print("Thank you ... Bye")
            break
        
        else:
            print("Invalid Entry")



if __name__ == '__main__':
    main()
