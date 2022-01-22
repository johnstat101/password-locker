#!/usr/bin/env python3
from user import UserAccounts
from credentials import Credentials

# *********************** userAccounts Methods ****************************************
def create_account(username, password):
    """
    Function to create new account
    """
    new_account = UserAccounts(username,password)
    return new_account

def save_account(account):
    """
    Function to save new account info
    """
    UserAccounts.save_userAccount(account)

def delete_account(account):
    """
    Function to delete account
    """
    UserAccounts.delete_userAccount(account)

def find_account(username):
    """
    Function to search for account
    """
    return UserAccounts.find_userAccounts_by_username(username)

def account_exists(username):
    """
    Function to check if account exists
    """
    return UserAccounts.userAccount_exists(username)

def display_accounts():
    """
    Function to display all available accounts
    """
    UserAccounts.display_userAccounts()

def create_account(username, password):
    """
    Function to create new account
    """
    new_account = UserAccounts(username,password)
    return new_account

def save_account(account):
    """
    Function to save new account info
    """
    UserAccounts.save_userAccount(account)

def delete_account(account):
    """
    Function to delete account
    """
    UserAccounts.delete_userAccount(account)

def find_account(username):
    """
    Function to search for account
    """
    return UserAccounts.find_userAccounts_by_username(username)

def account_exists(username):
    """
    Function to check if account exists
    """
    return UserAccounts.userAccount_exists(username)

def display_accounts():
    """
    Function to display all available accounts
    """
    UserAccounts.display_userAccounts()

# *********************** Credentials Methods ***************************************
def create_credential(page_name, password):
    """
    Function to create new credential
    """
    new_credential = Credentials(page_name,password)
    return new_credential

def save_credential(credential):
    """
    Function to save new credential info
    """
    Credentials.save_credential(credential)

def delete_credential(credential):
    """
    Function to delete credential
    """
    Credentials.delete_credential(credential)

def find_credential(page_name):
    """
    Function to search for credential
    """
    return Credentials.find_credentials_by_username(page_name)

def credential_exists(page_name):
    """
    Function to check if credential exists
    """
    return Credentials.credential_exists(page_name)

def display_credentials():
    """
    Function to display all available credentials
    """
    Credentials.display_credentials()


# ****************************** main() ***************************************
def main():
    print("Welcome to Pass Locker.This applications enables you to:\ncreate, manage and generate new accounts passwords")
    print("*"*100)
    print("What would you like to do... ")
    while True:
        print("Use these short codes: cc - create account, lc -login to your userAccounts, ex -exit the contact list")
        short_code = input()
        if short_code == 'cc':
            print("Please Create User Name and Password\n *******************************")
            print("Create a User Name ...")
            username = input()
            print("Create a Password ...")
            password = input()

            save_account(create_account(username,password))
            print(f"'{username}' account has been created")

        elif short_code == 'lc':
            print("Enter your User Name ...")
            username = input()
            if account_exists(username):
                print("Enter your Password ...")
                password = input()
                if find_account(username).password == password:
                    print("Your existing userAccounts")
                    print(display_accounts())
                    print("choose codes: ac - to add userAccounts, dc - delete userAccounts")
                    ac = input()

                else:
                    print("invalid password")
            else:
                print(f"'{username}' acount NOT FOUND")


        elif short_code =='ex':
            print("Thank you ... Bye")
            break

        else:
            print("Invalid Entry")



if __name__ == '__main__':
    main()
