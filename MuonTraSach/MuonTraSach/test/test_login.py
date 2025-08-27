import unittest
from MuonTraSach.dao import auth_user

class TestLogin(unittest.TestCase):
    def testcase_1(self):
        self.assertTrue(auth_user("user", "123"))

    def testcase_2(self):
        self.assertFalse(auth_user("user", "456"))

    def testcase_3(self):
        self.assertTrue(auth_user("admin", "345"))

    def testcase_4(self):
        self.assertFalse(auth_user("admin", "456"))

if __name__ == '__main__':
    unittest.main()
