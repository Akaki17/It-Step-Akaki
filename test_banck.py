import unittest
from bank import BankAccount

class TestBank(unittest.TestCase):
    
    def test_deposit(self):
        account = BankAccount('Test User', 0)
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)
        
    def test_withdraw(self):
        account = BankAccount('Test User', 100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)
        
    def test_insufficient_fund(self):
        account = BankAccount('Test User', 100)
        with self.assertRaises(ValueError):
            account.withdraw(150)
        self.assertEqual(account.get_balance(), 100)
            
    def test_negative_balance(self):
        account = BankAccount('Test user', 0)
        with self.assertRaises(ValueError):
            account.withdraw(50)
        self.assertEqual(account.get_balance(), 0)
        
if __name__ == '__main__':
    unittest.main()