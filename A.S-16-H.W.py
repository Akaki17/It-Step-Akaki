#####  #1

# class BankAccount:
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





#####  #2

# Student Class
# class Student:
    
#     # Initialize Student Attribute
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.courses = []
        
#     # Add a Course to the Student's list
#     def add_course(self, course_name):
#         self.courses.append(course_name)
        
#     # Display Student Information
#     def display_info(self):
#         print(f'Students name: {self.name}')
#         print(f'Student ID: {self.student_id}')
#         print(f'Enrolled Courses:')
#         for course in self.courses:
#             print(f' - {course}')
            
# # Creating Student Object
# student1 = Student('Akaki' ,'A2900100')
# student2 = Student('Giorgi', 'H346588')

# # Register for Courses
# student1.add_course('python')
# student1.add_course('Full Stack')
# student2.add_course('Math')
# student2.add_course('Management')

# # Display Student Information
# student1.display_info()
# print('\n')
# student2.display_info()

