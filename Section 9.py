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
print(e.tricks)
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

class carnivore(object):
    favorite_food = "meat"

class canine(object):
    sound = "bark"
    color = "gray"
class dog(canine, carnivore):
    sound = "woof"
    color = "brown"
class wolf(canine):
    sound = "Howl"
fido = dog()
print(fido.favorite_food)

class poodle(dog):
    __sound_ = "bark"

class Employee:
    pass
john = Employee()
john.name = "John Doe"
john.department = "computer lab"
print(john.name)
print(john.department)



class Portfolio:
    def __init__(self, accounts, money):
        self.accounts = accounts
        self.money = money
        list1 = []
        for i in range(0, accounts):
            import random
            money1 = money - 1000
            money2 = money + 1000
            money = random.randint(money1, money2)
            list1.append(money)
        print(list1)
        import matplotlib.pyplot as mat
        mat.plot(list1)
        mat.show()

Portfolio(19, 3569)


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("firstfile.text"):
    print(line, end='!')

s = 'abc'
it = iter(s)
next(it)
next(it)
next(it)

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
        print(char)

print(sum(i*i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

mapping_object = Mapping([1, 2, 3])
mapping_object.update([4, 5, 6])
print(mapping_object.items_list)
mapping_subclass_object = MappingSubclass([1, 2, 3])
mapping_subclass_object.update([4, 5, 6], [7, 8, 9])
print(mapping_subclass_object.items_list)

def foo():
    yield 1
    yield 2
    yield 3
print(foo())
print(foo())
print(foo())
print(foo())
for value in foo():
    print(value)

def foo1():
    yield 1
    yield 2
    yield 3
    yield "a"
    yield "b"
for value in foo1():
    print(value)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)

print(sum(i*i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))

