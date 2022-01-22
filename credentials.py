
class Credentials:
    """
    class that generates new instances of password
    """

    def __init__(self,page_name,password):
        # initialize
        self.page_name = page_name
        self.password = password

    credentials_list = [] # empty credentials list

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
    def find_credentials_by_page_name(cls,page_name):
        """
        find credentials by usename(unique identifier)
        """
        for credential in cls.credentials_list:
            if credential.page_name == page_name:
                return credential

    @classmethod
    def credential_exists(cls,page_name):
        """
        return true if a credential exists
        """
        for credential in cls.credentials_list:
            if credential.page_name == page_name:
                return True
    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials_list
        '''
        return cls.credentials_list


