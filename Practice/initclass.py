

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Garrett",21)

class Student(Person):
    pass

x = Student("Daryl", 28)






if __name__ == "__main__":
    print(p1.name)
    print(x.name)


    
