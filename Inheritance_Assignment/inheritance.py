

class User:
    name = 'No Name Given'
    email = ' '
    password = 'mypasswordrocks'
    account_id = 0
#has the have the parent class in () so that it knows it's a child class
class Employee(User):
    wage = 20.00
    department = 'Floral'

class Customer(User):
    mailing_address = ' '
    mailing_list = True

