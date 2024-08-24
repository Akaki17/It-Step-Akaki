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