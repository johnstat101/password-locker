#!/usr/bin/env python3
from credentials import Credentials

# methods
def create_account(username, password):
    """
    Function to create new account
    """
    new_account = Credentials(username,password)
    return new_account

def save_account(account):
    """
    Function to save new account info
    """
    Credentials.save_credential(account)

def delete_account(account):
    """
    Function to delete account
    """
    Credentials.delete_credential(account)

def find_account(username):
    """
    Function to search for account
    """
    return Credentials.find_credentials_by_username(username)

def account_exists(username):
    """
    Function to check if account exists
    """
    return Credentials.credential_exists(username)

def display_accounts():
    """
    Function to display all available accounts
    """
    Credentials.display_credentials()


# *********************************************************************
def main():
    print("This applications enables you to:\ncreate, manage and generate new accounts passwords")
    print("*"*20)
    print("Welcome to pass locker. What would you like to do... ")    
    while True:
        print("Use these short codes: cc - create account, lc -login to your credentials, ex -exit the contact list")
        short_code = input()
        if short_code == 'cc':
            print("Please Create User Name and Password\n *******************")
            print("Create a User Name ...")
            username = input()
            print("Create a Password ...")


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
