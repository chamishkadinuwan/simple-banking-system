import bankapp
import unittest
class testapplication(unittest.Testcase):
    def test_one(self) :
        bankapp.create_account()
