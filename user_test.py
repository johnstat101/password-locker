import unittest # Importing the unittest module
from user import UserAccounts # Importing the contact class

class TestUserAccounts(unittest.TestCase):
    """
    class to define test cases for the userAccounts class behavior
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_userAccount = UserAccounts("johnKim", "1234") #create an object of type UserAccounts

    def test_init(self):
        """
        Test whether the object is initialized correctly
        """
        self.assertEqual(self.new_userAccount.username,"johnKim")
        self.assertEqual(self.new_userAccount.password,"1234")
    
    def test_save_userAccount(self):
        """
        A test case to test if userAccount is saved in userAccountsList
        """
        self.new_userAccount.save_userAccount()
        self.assertEqual(len(UserAccounts.userAccounts_list),1)
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        UserAccounts.userAccounts_list = []
    
    def save_multiple_userAccounts(self):
        """
        test saving of multiple userAccounts
        """
        self.new_userAccount.save_userAccount()
        test_userAccount = UserAccounts("kimJohn","4321")
        test_userAccount.save_userAccount()
        self.assertEqual(len(UserAccounts.userAccounts_list),2)
    
    def test_delete_userAccounts(self):
        """
        test case for userAccounts deletion
        """
        self.new_userAccount.save_userAccount()
        test_userAccount = UserAccounts("kimJohn", "4321")
        test_userAccount.save_userAccount()
        self.new_userAccount.delete_userAccount()
        self.assertEqual(len(UserAccounts.userAccounts_list),1)
    
    def test_find_userAccounts_by_username(self):
        """
        test case to search for user userAccounts by username
        """
        self.new_userAccount.save_userAccount()
        test_userAccount = UserAccounts("kimJohn", "4321")
        test_userAccount.save_userAccount()

        found_userAccount = UserAccounts.find_userAccounts_by_username("kimJohn")
        self.assertEqual(found_userAccount.password, test_userAccount.password)
    
    def test_userAccount_exist(self):
        """
        return true if a contact exists
        """
        self.new_userAccount.save_userAccount()
        test_userAccount = UserAccounts("kimJohn", "4321")
        test_userAccount.save_userAccount()

        userAccount_exists = UserAccounts.userAccount_exists("kimJohn")
        self.assertTrue(userAccount_exists)

    def test_display_userAccounts(self):
        '''
        method that returns a list of all userAccounts saved
        '''
        self.assertEqual(UserAccounts.display_userAccounts(),UserAccounts.userAccounts_list)


if __name__ == '__main__':
    unittest.main()