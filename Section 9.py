def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class MyClass:
    """A simple example class"""
    i = 12345
    def message(self):
        return ('hello World')
    def get_i(self):
        return (self.i)
    def set_message(self, new_message):
        self.message = new_message
    def get_message(self):
        return self.message
x = MyClass()
print(x.i)
print(x.message())
print(x.get_i())
x.set_message("hello")
print(x.message)
x.set_message("hello world")
print(x.get_message())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
print(d.add_trick('roll over'))
print(e.add_trick('play dead'))
print(d.tricks)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.add_trick('roll over'))
print(e.add_trick('play dead'))
print(d.tricks)
print(e.tricks)


class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)