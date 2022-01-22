
class UserAccounts:
    """
    class that generates new instances of user accounts
    """
    userAccounts_list = [] # empty userAccounts list

    def __init__(self,username,password):
        # initialize
        self.username = username
        self.password = password

    def save_userAccount(self):
        """
        save new userAccount into userAccounts_list
        """
        UserAccounts.userAccounts_list.append(self)
    
    def delete_userAccount(self):
        """
        remove userAccount
        """
        UserAccounts.userAccounts_list.remove(self)
    
    @classmethod
    def find_userAccounts_by_username(cls,username):
        """
        find userAccounts by usename(unique identifier)
        """
        for userAccount in cls.userAccounts_list:
            if userAccount.username == username:
                return userAccount

    @classmethod
    def userAccount_exists(cls,username):
        """
        return true if a userAccount exists
        """
        for userAccount in cls.userAccounts_list:
            if userAccount.username == username:
                return True
    
    @classmethod
    def display_userAccounts(cls):
        '''
        method that returns the userAccounts_list
        '''
        return cls.userAccounts_list
