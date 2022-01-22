import unittest # Importing the unittest module
from credentials import Credentials # Importing the contact class

class TestCredentials(unittest.TestCase):
    """
    class to define test cases for the credentials class behavior
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credentials("johnKim", "1234") #create an object of type Credentials

    def test_init(self):
        """
        Test whether the object is initialized correctly
        """
        self.assertEqual(self.new_credential.username,"johnKim")
        self.assertEqual(self.new_credential.password,"1234")
    
    def test_save_credential(self):
        """
        A test case to test if credential is saved in credentialsList
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
    
    def save_multiple_credentials(self):
        """
        test saving of multiple credentials
        """
        self.new_credential.save_credential()
        test_credential = Credentials("kimJohn","4321")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credentials(self):
        """
        test case for credentials deletion
        """
        self.new_credential.save_credential()
        test_credential = Credentials("kimJohn", "4321")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()