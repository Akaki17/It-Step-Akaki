# # question= input("what type of media ? ").lower().strip() 
# # question_split=question.split('.')[-1]
# # print(question_split)

# # if  question_split == "gif" or  question_split == "jpeg" or question_split == "png" :     
# #     print("image/",question_split,sep="") 
    
# # elif question_split== "jpg":     
# #     print("image/","jpeg",sep="") 
    
# # elif question_split== "txt":     
# #     print("text/","plain",sep="") 
    
# # elif question_split== "zip":     
# #     print("application/",question_split,sep="") 
    
# # elif question_split== "pdf":     
# #     print("application/",question_split,sep="")
    
# # else :     
# #     print("application/octet-stream")


# def main():
#     user_time = input('Enter file name and extension: ')
#     result = file_extension(user_time)
#     print(result)

# def file_extension(arg):
#     arg = arg.lower().strip()
#     arg = arg.replace(" ", "")
#     result = arg.rfind('.')
#     if result != -1:
#         extracted_extension = arg[result + 1:]
        
#         if extracted_extension == 'gif':
#             return 'img/gif'
#         elif extracted_extension == 'jpg':
#             return 'img/jpg'
#         elif extracted_extension == 'jpeg':
#             return 'img/jpeg'
#         elif extracted_extension == 'png':
#             return 'img/png'
#         elif extracted_extension == 'txt':
#             return 'text/plain'
#         elif extracted_extension == 'zip':
#             return 'application/zip'
#         elif extracted_extension == 'pdf':
#             return 'application/pdf'
#         elif extracted_extension == 'bin':
#             return 'application.bin'
#         else:
#             return extracted_extension
#     else:
#         return 'No file extension found'

# main()




# import mimetypes

# def get_mime_type(filename):
#     # Normalize the filename (remove leading/trailing spaces and convert to lowercase)
#     filename = filename.strip().lower()

#     # Get the MIME type based on the file extension
#     mime_type, _ = mimetypes.guess_type(filename)

#     # If the MIME type is not found, return 'application/octet-stream'
#     return mime_type or 'application/octet-stream'

# def main():
#     user_time = input("Enter a file name (with extension): ")
#     mime_type = get_mime_type(user_time)

#     print(f"{mime_type}")

# if __name__ == "__main__":
#     main()













# class BankAccount:
    
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = initial_balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f'Deposited ${amount}. New balance: ${self.balance}')
#         else:
#             print(f'Invalid deposit amount')
            
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f'Withdraw ${amount}. New balance: ${self.balance}')
#         else:
#             print(f'Invalid withdraw amount or insufficient funds.')
            
# account1 = BankAccount('1001', 'Alice Johnson', 1000)
# account2 = BankAccount('1002', 'Bob Smith', 500)

# account1.deposit(1000)
# account1.withdraw(200)

# account2.deposit(1000)
# account2.withdraw(1200)
# account2.withdraw(300)

# print(f'account {account1.account_holder} - {account1.account_number} balance: ${account1.balance}')
# print(f'account {account2.account_holder} - {account2.account_number} balance: ${account2.balance}')









# class BankAccount:
    
#     def __init__(self, account_number, account_holder, initial_balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = initial_balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f'Deposit ${amount}. New Deposit ${self.balance}')
#         else:
#             print(f'Invalid deposit amount.')
            
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f'Withdrew ${amount}. New Deposit ${self.balance}')
#         else:
#             print(f'Invalid withdraw or insufficient funds.')
            

# account1 = BankAccount('1001', 'Alisa Kays', 1000)
# account2 = BankAccount('1002', 'Bob smith', 500)

# account1.deposit(500)
# account1.withdraw(200)

# account2.deposit(1000)
# account2.withdraw(1200)
# account2.withdraw(300)

# print(f'Account holder: {account1.account_holder} - balance: ${account1.balance}')
# print(f'Account holder: {account2.account_holder} - balance: ${account2.balance}')





# class BankAccount:
#     def __init__(self, account_number, account_holder, init_balance):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = init_balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f'Deposit ${amount}. New Balance: ${self.balance}')
#         else:
#             print(f'Invalid deposit amount.')
            
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f'Withdrew ${amount}. Balance: ${self.balance}')
#         else:
#             print(f'Invalid withdrawal or insufficient funds.')
            
# account1 = BankAccount('1001', 'Alice Johnson', 1000)
# account2 = BankAccount('1002', 'John Doe', 500)

# account1.deposit(500)
# account1.withdraw(200)

# account2.deposit(1000) 
# account2.withdraw(1000)
# account2.withdraw(300)

# print(f'Account holder: {account1.account_holder}. Balance: ${account1.balance}')
# print(f'Account holder: {account2.account_holder}. Balance: ${account2.balance}')











# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.courses = []
        
#     def add_course(self, course_name):
#         self.courses.append(course_name)
        
#     def display_info(self):
#         print(f'Students name: {self.name}')
#         print(f'Students ID: {self.student_id}')
#         print(f'Enrolled Courses:')
#         for course in self.courses:
#             print(f' - {course}')
            
# student1 = Student('Akaki Surmava', 'AB234765')
# student2 = Student('Inga Inadye', 'XC65878')

# student1.add_course('Python')
# student1.add_course('Math')
# student2.add_course('Management')
# student2.add_course('Full Stack')

# student1.display_info()
# print(f'\n')
# student2.display_info()















# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.courses = []
        
#     def add_course(self, course):
#         self.courses.append(course)
        
#     def display_info(self):
#         print(f'Students name: {self.name}')
#         print(f'Students id: {self.id}')
#         print(f'Courses: ')
#         for course in self.courses:
#             print(f'- {course}')
            
# student1 = Student('Akaki Surmava', 'DS987435')
# student2 = Student('Lela linio', 'HG6576438')

# student1.add_course('Python')
# student1.add_course('Full Stuck')
# student1.add_course('Math')
# student1.add_course('Management')

# student1.display_info()
# print(f'\n')
# student2.display_info()









# def split(math_input):
#     numbers = math_input.split(' ')
#     num1 = int(numbers[0])
#     num2 = int(numbers[2])
#     operator = numbers[1]
#     print(f'{num1} {operator} {num2}')
#     return num1, operator, num2
    
# def calculator(num1, num2, operator):
    
#     operators_dict = {
#         '+' : lambda x, y: x + y,
#         '-' : lambda x, y: x - y,
#         '*' : lambda x, y: x * y,
#         '/' : lambda x, y: x / y,
#     }
#     result = operators_dict.get(operator, lambda x, y: None) (num1, num2)
#     print(f'{int(result)}')
          
# user_time = input('Enter num1 operator num2: ')

# num1, operator, num2 = split(user_time)
# calculator(num1, num2, operator)












# def main(user):
#     user_time = input('Enter the current time: ')
    
#     time_int = convert(user_time)
#     if 5.0 <= time_int < 11.5:
#         print(f'breakfast time')
#     elif 11.5 <= time_int < 15.0:
#         print(f'lunch time')
#     elif 15.0 <= time_int < 22.0:
#         print('dinner time')

# def convert(time):
#     hours, minutes = map(int, time.split(':'))
#     return hours + minutes / 60
    
# if __name__ == "__main__":
#     main(user)


# numbers = ['1', '2', '3']
# int_numbers = map(int, numbers)
# print(list(int_numbers))

# numbers = ['1', '2', '3', '4']
# int_numbers = map(int, numbers)
# print(list(int_numbers))

# number_list = ['7','8','9','10','11']
# int_list = map(int, number_list)
# print(list(int_list))



# def main():
#     user_time = input('Enter current time (format 24h): ')
#     current_time = convert(user_time)
    
#     if  7 <= current_time <= 8:
#         print(f'breakfast time')
#     elif 12 <= current_time <= 13:
#         print(f'lunch time') 
#     elif 18 <= current_time <= 19:
#         print(f'dinner time')
    

# def convert(time):
#     hour, minutes = map(int, time.split(':'))
#     return hour + minutes / 60
    
# if __name__ == "__main__":
#     main()



















# def main():
#     input_time = input('Enter current time (24H format): ')
#     current_time = convert(input_time)
    
#     if 7 <= current_time <= 8:
#         print(f'breakfast time')
#     if 12 <= current_time <= 13:
#         print(f'lunch time')
#     if 18 <= current_time <= 19:
#         print(f'dinner time')
    
    
# def convert(time):
#     hour, minutes = map(int, time.split(':'))
#     result = hour + minutes / 60
#     print(result)

#     return result
    

# if __name__ == '__main__':
#     main()


# print('Roar!\n' * 3, end='')

# for _ in range (3):
#     print('Roar!')

# i = 0
# while i < 3:
#     print(f'Roar!') 
#     i += 1



# print('Roar!')
# print('Roar!')
# print('Roar!')

# n = int(input('Pleas enter a positive number: '))

# while n <= 0:
#     n = int(input('Pleas enter a positive number: '))


# while True:
#     n = int(input('Please enter a positive number: '))
#     if n <= 0:    
#         continue
#     else:
#         break
    
# for _ in range(n):
#     print(f'Roar!')


# def main():
#     number = get_number()
#     roar(number)

# #Gets number from user
# def get_number():

#     while True:
#         n = int(input('Please enter a positive number: '))
#         if n >= 0:    
#             return n

# # prints 'Roar!' in the terminal for n number of times.
# def roar(n):
            
#     for _ in range(n):
#         print(f'Roar!')
        
# main()







# animals = ['Dog', 'Cat', 'Pigeon', 'Mosquito', 'Snake']
# for animal in animals:
#     print(animal)

# dog = animals[0]
# print(dog)

# print(animals[5])

# for index in range(len(animals)):
#     print(f'{index + 1}.', animals[index], sep='')

# types = ['animal', 'animal', 'bird', 'insect', 'reptile']
# number_of_legs = [4, 2, 4, 0]


# for index in range(len(animals)):
#     print(f'{index + 1}.', animals[index], types[index])


    
# animals = {
#     'Dog': 'animal',
#     'Pigeon': 'animal',
#     'Mosquito': 'insect',
#     'Snake': 'reptile',
# }

# print(animals['Snake'])

# for key in animals:
#     print(key, animals[key])

# for key in animals:
#     print(key, animals[key])

# for key in animals:
#     print(key, animals[key])
    
# animals = [
#     {'name': 'Dog', 'type': 'animal', 'nol': '4'},
#     {'name': 'Cat', 'type': 'animal', 'nol': '4'},
#     {'name': 'Pigeon', 'type': 'animal', 'nol': '2'},
#     {'name': 'insect', 'type': 'insect', 'nol': '6'},
#     {'name': 'Snake', 'type': 'reptile', 'nol': None},
# ]
# for animal in animals:
#     print(animal['name'], animal['type'], animal['nol'])



# print('#')
# print('#')
# print('#')

# def main():
#     # print_column(5)
#     # print_row(10)
#     print_square(10)
    
    
# def print_square(size):
#     # For each row in a square
#     for i in range(size):
#         print_row(size)
        


# def print_row(width):
#     print('#' * width)

# def print_column(height):
#     for _ in range(height):
#         print('#')
        
# main()


# def main():
#     user_iterate = input('Enter camel case style iterate name: ')
    
#     new_iterate = snake(user_iterate)
#     print(new_iterate)

# def snake(iterate):
#     new_string = ''
#     for i in iterate:
#         if(i.isupper()):
#             new_string += '_' + i
#         else:
#             new_string += i
            
#     return new_string.lower()
        
# main()






# def main():
#     price = 50
#     balance = 0
    
#     while balance < price:
#         user_input = int(input(f'Insert Coin: '))
        
#         balance += user_input
#         print(f'Amount Doe: {price - balance} ')
        
#         # print(f'Insert Coin: {balance}')

#         # if user_input in[5, 10, 25]:
            
            
#         # else: 
#         #     print(f'Invalid input. Please insert 5, 10 or 25 cents.')
            
#     print(f'Change owned {balance - price}')

# main()










# def write_file(file_counter, lines_lst):
#     with open(f'filtered {file_counter}.txt', 'w') as new_file: 
#         new_file.writelines(lines_lst)

    
# def manage_file(file_name):
#     with open(file_name, 'r') as file:
#         file_counter = 1
#         lines_lst = []
        
#         for line in file.readlines():
#             if lines_lst and len(lines_lst) % 10 == 0:
#                     write_file(file_counter, lines_lst)
#                     lines_lst.clear()
#                     file_counter += 1
#                     lines_lst.append(line)
#             else:
#                 lines_lst.append(line)
#         else:
#             write_file(file_counter, lines_lst)

# manage_file('test.txt')




# def clean_file(old_file, new_file):
#     lines = []
    
#     with open(old_file, 'r') as file:
#         for line in file.readlines():
#             if line !='\n':
#                 lines.append(line)
                
#     with open(new_file, 'w') as file:
#         file.writelines(lines)
        
        
# clean_file('test.txt', 'cleaned.txt')



# class Mother:
#     def __init__(self, name, eye_color):
#         self.name = name
#         self.eye_color = eye_color
        
#     def greet(self):
#         print(f'Hello From: {self.name}')
        
#     def bake_cookies(self):
#         print(f'{self.name} is baking delicious cookies')
        
    
# class Father:
#     def __init__(self, name , hair_color):
#         self.name = name
#         self.hair_color = hair_color
    
#     def greet(self):
#         print(f'Hello From: {self.name}')
        
#     def tell_jokes(self):
#         print(f'{self.name} crack a funny jokes')
        
        
# class Child(Mother, Father):
#     def __init__ (self, name, eye_color, hair_color, profession, mother, father):
#         Mother.__init__(self, name, eye_color)
#         Father.__init__(self, name, hair_color)
#         self.profession = profession
#         self.mother = mother 
#         self.father = father
    
#     def inherited_methods(self):
#         print('Child Inherited both methods', self.mother.eye_color)
        
# mom = Mother('Kate', 'Blue')
# dad = Father('Bob', 'Black')
# child =  Child('John', mom.eye_color, dad.hair_color, 'Developer', mom ,dad)

# mom.greet()
# dad.greet()
# child.greet()
# child.inherited_methods()






# class owner_person:
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age
    
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         self.__name = value
        
#     @name.getter
#     def name(self):
#         return self.__name
    
#     # @name.deleter
#     # def name (self):
#     #     del self.__name         
    
    
# owner_person  = owner_person('John', 25)
# print(owner_person.name)

# owner_person.name = 'Bob'
# print(owner_person.name)

# del owner_person.name
# print(owner_person.name)








# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def calculate_area(self):
#         pass
    
#     def standard_method(self):
#         print('Hello')



# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
    
#     def print_radius(self):
#         print(self.radius)
        
        
        
# class Rectangle(Shape): 
#     pass

# circle = Circle(10)
# circle.standard_method()
# rect = Rectangle()

# circle . print_radius()
# print(circle.calculate_area())




# class Calculator:
#     def add(self, a, b):
#         if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#             result = a + b
#             print(f'Integer result: {result}')
            
#         if isinstance(a, str) and isinstance(b, str):
#             result = a + b 
#             print(f'String Result: {result}')
            
# calc = Calculator()
# calc.add(10, 20)
# calc.add('10', '20')
# calc.add()







# from multipledispatch import dispatch

# class Calculator:
    
#     @dispatch(int, int)
#     def add(self, a, b):
#         return a * b 
    
#     @dispatch(int, int, int)
#     def add(self, a, b, c):
#         return a + b + c
    
#     @dispatch(str, str)
#     def add(self, a, b):
#         return a + b 
    
    
# calc = Calculator()
# print(calc.add(10, 11))
# print(calc.add('10', '11'))
# print(calc.add(10, 10, 10))









# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             raise TypeError('Other must be Vector')
        
#         return Vector(self.x + other.x, self.y + other.y)

# vector1 = Vector(1, 2)
# vector2 = Vector(3, 4)
# vector3 = vector1 + vector2
# print(vector3.x, vector3.y)




# class Book:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
        
#     # def __str__(self):
#         # return self.name
    
#     def __repr__(self):
#         return str(self.year)
        
# book = Book('Rame saxeli', 1900)

# print(book)



# def main():
#     Amount_Due = 50
#     Insert = 0 
#     print(f'Amount Due: {Amount_Due}')
    
#     while Insert < Amount_Due:
#         user_insert = int(input('Insert Coin: '))
        
#         if Insert < Amount_Due:
            
#             if user_insert in [5, 10, 25, 50]:
#                 Insert += user_insert
                
#                 if Insert == Amount_Due:
#                     print(f'Change owed: {Insert - Amount_Due}')
#                     break
    
#                 elif Insert > Amount_Due:
#                     print(f'Change owed: {Insert - Amount_Due}')
#                     break

#                 print(f'Amount Due: {Amount_Due - Insert}')
        
# main()




# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Deposited ${amount}. New balance: ${self.balance}')
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f'Withdrew: ${amount}. New balance: ${self.balance}')
#         else: 
#             print(f'Insufficient funds!')
            
# my_account = BankAccount('John Doe', 1000)
# my_account.deposit(500)
# my_account.withdraw(200)


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self, amount):
#         print(f'Start deposit: ${self.balance}')
#         self.balance += amount
#         print(f'Deposit: ${amount}. New balance: ${self.balance}')
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f'Withdrew: ${amount}. New balance: ${self.balance}')
#         else:
#             print(f'Insufficient funds!')
            
# my_account = BankAccount('john Doe', 1000)

# my_account.deposit(500)
# my_account.withdraw(200)


# class owner_person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# owner_person1 = owner_person('Alice', 30)

# class Student(owner_person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         student_id = student_id
        
#     def greet(owner_person):
#         print(f'Hello, {owner_person. name}')
        
# alice = owner_person('Alice', 30)
# bob = Student('Bob', 25, '12345')

# alice.greet(alice)
# bob.greet(bob)




# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
        
# car = Vehicle('Toyota', 180, 12)


# class Bus(Vehicle):
#     pass

# school_bus = Bus('School Volvo', 180, 12)


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     @property
#     def pi(self):
#         return 3.14

# def check_type(obj):
#     print(f'Type of {obj}: {type(obj).__name__}')

# car = Vehicle("Toyota", 180, 12)
# school_bus = Bus("School Volvo", 180, 12)
# circle = Circle(5)

# print(f"Vehicle Name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}")
# print(f"Vehicle Name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
# print(f"Circle Radius: {circle.radius}, Pi Value: {circle.pi}")

# print(isinstance(school_bus, Circle))



# Empty class
# class Dog:
#     pass


# class Dog:
#     def __init__(self, breed, age, gender):
        
#         self.breed = breed 
#         self.age = age
#         self.gender = gender
        
#     def bark(self):
#         return(f'Woof!')
    
    
# my_dog = Dog('Golden Retriever', 3, 'female')

# print(f"My Dog's breed is: {my_dog.breed}. It's {my_dog.gender}. She is {my_dog.age} years old. She likes make louder: {my_dog.bark()}")






# class Animal:
#     def speak(self):
#         return 'Some animal speaks'
        
# class Dog(Animal):
#     def bark(self):
#         return 'Woof!'
        
# my_dog = Dog()

# print(f'{my_dog.speak()} {my_dog.bark()}')

# class Cat(Animal):
#     def speak(self):
#         return 'Meow!'
        
# def animal_sound(animal):
#     animal.speak()
    
# my_cat = Cat()
# animal_sound(my_dog)
# animal_sound(my_cat)

# print(f'{my_dog.speak()} {my_dog.bark()} and {my_cat.speak()}')










# class owner_person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# owner_person1 = owner_person('Alice', 30)

# print(f'owner_person: {owner_person1.name}. Age: {owner_person1.age}')


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius **2

# circle1 = Circle(5)
# print(f'Circle area:  {circle1.area()}')


# class MyClass:
#     count = 0
    
#     @classmethod
#     def increment_count(cls):
#         cls.count += 1
        
# MyClass.increment_count()
# print(MyClass.count)


# class MathOperations:
#     def add(self, a, b=None):
#         if b is None:
#             return a
#         else:
#             return a + b
# math_ops = MathOperations()
# print(math_ops.add(2))
# print(math_ops.add(2, 3))


# class ComplexNumber:
#     def __init__(self, real, image):
#         self.real = real
#         self.image = image
        
#     def __str__(self):
#         return f'{self.real} + {self.image}'
    
# c1 = ComplexNumber(3,4)
# print(c1)

# class MyClass1:
#     @staticmethod
#     def static_method():
#         print(f'This is static method')

#     @classmethod
#     def class_method(cls):
#         print(f'Tis is a class method of {cls.__name__}')
        
# MyClass1.static_method()
# MyClass1.class_method()   






######################################################  ###########


            
        
# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
    
#     def __str__ (self):
#         return f'Person: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}'
        
#     def add_deposit(self,amount):
#         if amount > 0:
#             self.deposit += amount
#             print(f'Deposit added. New balance: {self.deposit}')
        

# class House:
#     def __init__ (self, ID, price, owner=None, status='for sale'):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = status
        
#     def apartment_sale(self, buyer, loan_amount=None):
#         if loan_amount is None:
#             self.owner.deposit -= self.price
#             self.owner = buyer
#             self.status = 'sold'
#             print(f'Apartment {self.ID} sold to {buyer.name}')
#         else:
#             self.owner.deposit -= self.price
#             self.owner = buyer
#             self.status = 'sold'
#             buyer.loan += loan_amount
#             print(f'Apartment {self.ID} sold to {buyer.name} with a loan of {loan_amount}.')
        
#     def __str__ (self):
#         return f'House: {self.ID}, Price: {self.price}, owner: {self.owner.name}, Status: {self.status}'

# owner = Person('John Doe')
# buyer = Person('Alice Smith')
           
# apartment = House(ID='A123', price=150000, owner=owner)

# apartment.apartment_sale(buyer, loan_amount=50000) 
            
# print(owner)
# print(buyer)
# print(apartment)






# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
        
#     def __str__(self):
#         return f'Person: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}'
    
#     def add_deposit(self, amount):
#         if amount > 0:
#             self.deposit += amount
#             print(f'Deposit added. New balance: {self.deposit}')
            

# class House: 
#     def __init__(self, ID, price, owner=None, status='for sale'):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = status
        
#     def apartment_sale(self, buyer, loan_amount=None): 
#         if loan_amount is None:
#             self.owner.deposit -= self.price
#             self.owner = buyer
#             self.status = 'sold'
#             print(f'Apartment {self.ID} sold to {buyer.name}')
#         else:
#             self.owner.deposit -= self.price
#             self.owner = buyer
#             self.status = 'sold'
#             buyer.loan += loan_amount
#             print(f'Apartment {self.ID}, sold to {buyer.name} with a loan of {loan_amount}.')
            
#     def __str__(self):
#         return f'House ID: {self.ID}, Price: {self.price}, Owner: {self.owner.name}, status: {self.status}'
    
# owner = Person('John DOe')
# buyer = Person('Alice Smith')
# apartment =  House(ID='A123', price=150000, owner=owner)
    
# apartment.apartment_sale(buyer, loan_amount=50000)

# print(owner)
# print(buyer)
# print(apartment)






# class Person:
#     def __init__(self, name, deposit=1000, loan=0):
#         self.name = name
#         self.deposit = deposit
#         self.loan = loan
        
#     def __str__(self):
#         return f'Person name: {self.name}, deposit: {self.deposit}, Loan: {self.loan}'
    
#     def add_deposit(self, amount):
#         if amount > 0:
#             self.deposit += amount
#             print(f'Deposit added. New balance: {self.deposit}')
            
# class House:
#     def __init__(self, ID, price, owner=None, status='for sale'):
#         self.ID = ID
#         self.price = price
#         self.owner = owner
#         self.status = status
        
#     def apartment_sale(self, buyer, loan_amount=None):
#         if loan_amount is None:
#             self.owner.deposit -= self.price
#             self.owner = buyer
#             self.status = 'sold'
#             print(f'Apartment {self.ID} sold to {buyer.name}')
#         else:
#             self.owner.deposit -= self.price
#             self.owner = buyer
#             self.status = 'sold'
#             buyer.loan += loan_amount
#             print(f'Apartment {self.ID} sold by {buyer.name}, with loan: {loan_amount}')
            
#     def __str__(self):
#         return f'House ID: {self.ID}, Price: {self.price}, Owner: {self.owner.name}, Status: {self.status}'
    


# owner = Person('John DOe')
# buyer = Person('Alice Smith')
# apartment = House(ID='A1213', price=150000, owner=owner)
        
# apartment.apartment_sale(buyer, loan_amount=50000)

# print(owner)
# print(buyer)
# print(apartment)





class Person:
    def __init__ (self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan
        
    def __str__ (self):
        return f'Person: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}'
    
    def add_deposit(self, amount):
        if amount > 0:
            self.deposit += amount
            print(f'Deposit added. New balance: {self.deposit}')
    
class House:
    def __init__ (self, ID, price, owner=None, status='sale'):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status
        
    def apartment_sale(self, buyer, loan_amount=None):
        if loan_amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = 'Sold'
            print(f'Apartment: {self.ID} bought {buyer.name}')
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = 'Sold'
            buyer.loan = loan_amount
            print(f'Apartment {self.ID}, sold to {buyer.name} whit a loan of {loan_amount}')
        
    def __str__(self):
        return f'House ID: {self.ID}, Price: {self.price}, Owner: {self.owner.name}, Status: {self.status}'

owner = Person('John Doe')
buyer = Person('Alice Smith')
apartment = House(ID='A123', price=15000, owner=owner)

apartment.apartment_sale(buyer, loan_amount=50000)

print(owner)
print(buyer)
print(apartment)