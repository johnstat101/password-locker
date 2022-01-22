class Credentials:
    """
    class that generates new instances of password
    """
    credentialsList = []; #empty credentials list
    def __init__(self,username,password):

        self.username = username
        self.password = password