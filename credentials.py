
class Credentials:
    """
    class that generates new instances of password
    """
    credentials_list = [] #empty credentials list

    def __init__(self,username,password):
        # initialize
        self.username = username
        self.password = password

    def save_credential(self):
        """
        save new credential into credentials_list
        """
        Credentials.credentials_list.append(self)
    
    def delete_credential(self):
        """
        remove credential
        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credentials_by_username(cls,username):
        """
        find credentials by usename(unique identifier)
        """
        for credential in cls.credentials_list:
            if credential.username == username:
                return credential

    @classmethod
    def credential_exists(cls,username):
        """
        return true if a credential exists
        """
        for credential in cls.credentials_list:
            if credential.username == username:
                return True
    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials_list
        '''
        return cls.credentials_list


