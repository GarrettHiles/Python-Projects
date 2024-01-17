
#parent class
class User:
    name = 'Dave'
    email = 'hiimdave@gmail.com'
    password = 'vasdhf23'

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")
#child class employee

class Employee(User):
    base_pay = 14.00
    department = 'General'
    pin_number = "3333"

#The following is the same method it just used entry_pin instead of entry_password

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

#The following code invokes the methods inside of each class for user and employeee

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

