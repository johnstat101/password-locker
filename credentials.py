
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
    
    def find_credentials_by_username(self):
        """
        find credentials by usename(unique identifier)
        """
        
