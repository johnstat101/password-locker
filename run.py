#!/usr/bin/env python3
from user import UserAccounts
from credentials import Credentials
import random

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
    account.save_userAccount()

def delete_account(account):
    """
    Function to delete account
    """
    account.delete_userAccount()

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
    return UserAccounts.display_userAccounts()

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
    credential.save_credential()

def delete_credential(credential):
    """
    Function to delete credential
    """
    credential.delete_credential()

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
    return Credentials.display_credentials()


# ****************************** main() ***************************************
def main():
    print(f"{'*'*24} PASS-LOCKER WEBSITE {'*'*24}")
    print("Welcome to Pass Locker.This applications enables you to:\ncreate, manage and generate new accounts passwords\n")
    while True:
        print(f"{'*'*25} USER ACCOUNTs {'*'*25}")
        print("What would you like to do?. (CHOOSE NUMBER CODES)")
        print("1)CREATE ACCOUNT\n2)LOGIN\n3)EXISTING ACCOUNTs\n4)EXIT\n")
        short_code = int(input())
        if short_code == 1:
            print("Please Create User Name and Password")
            print("USER NAME: ")
            username = input()
            print("PASSWORD: ")
            password = input()

            save_account(create_account(username,password))
            print(f"'{username}' account has been created\n")

            while True:
                print(f"{'*'*25} PAGEs INFORMATION {'*'*25}")
                print(f"Welcome {username}, Please select:")
                print("1)CREATE OWN PAGE PASSWORD.. e.g twitter\n2)AUTO_GENERATE PAGE PASSWORD\n3)DISPLAY EXISTING PASSWORDs\n4)DELETE PAGE PASSWORD\n5)BACK\n")
                user_log = int(input())

                if user_log == 1:
                    print(f"{'*'*25} SAVE PAGE PASSWORDs {'*'*25}")
                    print("Enter Page Name and Password: e.g twitter")
                    print("PAGE: ")
                    page_name = input()
                    print("PASSWORD: ")
                    password = input()

                    # save new password
                    save_credential(create_credential(page_name,password))
                    print(f"page saved\n")
                
                elif user_log == 2:
                    print(f"{'*'*25} AUTO GENERATE PASSWORDs {'*'*25}")
                    print("Enter Page Name e.g twitter")
                    print("PAGE: ")
                    page_name = input()
                    
                    # randomly generate 4-digit password
                    password = ''.join(str(e) for e in random.sample([0,1,2,3,4,5,6,7,8,9],4))

                    # save new password
                    save_credential(create_credential(page_name,password))
                    print(f"page saved\n with password: {password}")

                elif user_log == 3:
                    print(f"{'*'*25} DISPLAY PASSWORDs {'*'*25}")
                    if display_credentials():
                        for cred in display_credentials():
                            print(f"{cred.page_name}:{cred.password}")
                    else:
                        print(f"NO PASSWORD FOUND\n")

                elif user_log == 4:
                    print(f"{'*'*25} DELETE PASSWORDs {'*'*25}")
                    print(f"Enter Page you want to delete")
                    print(f"PAGE")
                    page_name = input()
                    if credential_exists(page_name):
                        page_name = (page_name)
                        delete_credential(page_name)
                        # delete page passwords
                        print(f"page deleted\n")
                    else:
                        print(f"page NOT FOUND\n")

                elif user_log == 5:
                    break

                else:
                    print("Invalid Entry")

        elif short_code == 2:
            print(f"{'*'*25} LOGIN {'*'*25}")
            print("Enter Your Login Information")
            print("USER NAME: ")
            username = input()
            print("PASSWORD: ")
            password = input()

            if account_exists(username) and find_account(username).password == password:
                while True:
                    print(f"{'*'*25} PAGEs INFORMATION {'*'*25}")
                    print(f"Welcome {username}, Please select:")
                    print("1)CREATE OWN PAGE PASSWORD.. e.g twitter\n2)AUTO_GENERATE PAGE PASSWORD\n3)DISPLAY EXISTING PASSWORDs\n4)DELETE PAGE PASSWORD\n5)BACK\n")
                    user_log = int(input())

                    if user_log == 1:
                        print(f"{'*'*25} SAVE PAGE PASSWORDs {'*'*25}")
                        print("Enter Page Name and Password: e.g twitter")
                        print("PAGE: ")
                        page_name = input()
                        print("PASSWORD: ")
                        password = input()

                        # save new password
                        save_credential(create_credential(page_name,password))
                        print(f"page saved\n")
                    
                    elif user_log == 2:
                        print(f"{'*'*25} AUTO GENERATE PASSWORDs {'*'*25}")
                        print("Enter Page Name e.g twitter")
                        print("PAGE: ")
                        page_name = input()

                        # randomly generate 4-digit password
                        password = ''.join(str(e) for e in random.sample([0,1,2,3,4,5,6,7,8,9],4))

                        # save new password
                        save_credential(create_credential(page_name,password))
                        print(f"page saved\n with password: {password}")
                    
                    elif user_log == 3:
                        print(f"{'*'*25} DISPLAY PASSWORDs {'*'*25}")
                        if display_credentials():
                            for cred in display_credentials():
                                print(f"{cred.page_name}:{cred.password}")
                        else:
                            print(f"NO PASSWORD FOUND\n")
                    
                    elif user_log == 4:
                        print(f"{'*'*25} DELETE PASSWORDs {'*'*25}")
                        print(f"Enter Page you want to delete")
                        print(f"PAGE")
                        page_name = input()
                        if credential_exists(page_name):
                            page_name = (page_name)
                            delete_credential(page_name)
                            # delete page passwords
                            print(f"page deleted\n")
                        else:
                            print(f"page NOT FOUND\n")
                    
                    elif user_log == 5:
                        break
                    
                    else:
                        print("Invalid Entry")

            else:
                print(f"User Name '{username}' NOT FOUND")
                print(f"Wrong UserName OR Password\n")


        elif short_code == 3:
            print(f"{'*'*25} DISPLAY EXISTING ACCOUNTS {'*'*25}")
            if display_accounts():
                for acc in display_accounts():
                    print(f"{acc.username}\n")
                
            else:
                print("NO ACCOUNTs FOUND\n")
        
        elif short_code == 4:
            print("Thank you ... Bye")
            break

        else:
            print("Invalid Entry\n")



if __name__ == '__main__':
    main()
