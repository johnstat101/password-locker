import imp
import unittest # Importing the unittest module
from credentials import Credentials # Importing the contact class

class TestCredentials(unittest.TestCase):
    """
    class to define test cases for the credentials class behavior
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUP(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credentials("johnKim", "1234") #create an object of type Credentials