class BankAccount:
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         # Initialize BankAccount object with account number, account holder, and initial balance
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = initial_balance        

#     def deposit(self, amount):
#         # Deposit money into the account if the amount is greater than 0
#         if amount > 0:
#             # Add the deposit amount to the balance
#             self.balance += amount
#             print(f'Deposited ${amount}. New balance: ${self.balance}')
#         else:
#             # If the deposit amount is not valid (<= 0), show an error message
#             print('Invalid deposit amount.')

#     def withdraw(self, amount):
#         # Withdraw money from the account if the amount is greater than 0 and less than or equal to the current balance
#         if 0 < amount <= self.balance:
#             # Subtract the withdrawal amount from the balance
#             self.balance -= amount
#             print(f'Withdrew ${amount}. New balance: ${self.balance}')
#         else:
#             # If the withdrawal amount is not valid or exceeds the balance, show an error message
#             print('Invalid withdrawal amount or insufficient funds.')
            

# # Create two BankAccount instances
# account1 = BankAccount('1001', 'Alice Johnson', 1000)
# account2 = BankAccount('1002', 'Bob Smith', 500)

# # Perform deposit and withdrawal operations on account1 and account2
# account1.deposit(500)
# account1.withdraw(200)

# account2.deposit(1000)
# account2.withdraw(1200)
# account2.withdraw(300)

# # Display the final balances for account1 and account2
# print(f'Account {account1.account_number} balance: ${account1.balance}')
# print(f'Account {account2.account_number} balance: ${account2.balance}')