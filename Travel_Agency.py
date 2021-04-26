class Corporation(object):
    """A class for a corporation"""
    def __init__(self, owner, state):
        self.owner = owner
        self.state = state
    owner_list = []
    customers = []
    vendors = []
    employees = []
    managers = []
    products = []
    services = []
    inputs = []

class Travel_Agency(Corporation):
    def __init__(self, customers):
        self.customers = customers
        self.brazil = Trip_Planner("Brazil")
        self.spain = Trip_Planner("Spain")
        self.italy = Trip_Planner("Italy")
        self.product_list = [self.brazil, self.spain, self.italy]
        self.corportation = Corporation.products
        for i in self.product_list:
            i = str(i)
            self.corportation.append(i)
    cash = []
    def booking(self, destination, people, price):
        pass


class Trip_Planner:
    def __init__(self, location):
        self.location = location
    def __str__(self):
        return str(self.location)
    starting_point = ''
    ending_point = ''
    per_person = []
    people = []
class Person:
    def __init__(self, person):
        self.person = person
        self.people = Trip_Planner.people
        self.people.append(self.person)
    def __str__(self):
        return str(self.person)


c = Person("Al")
d = Person("Jill")
a = Trip_Planner("Brazil")
Trip_Planner("Brazil")
Al = Person('Al')
Jill = Person("Jill")
Brazil = Trip_Planner("Brazil")
customers3 = [str(c), str(d)]
and1 = " and "
customers3 = and1.join(customers3)




#Attributes - starting point, and ending point, cost of the trip per person
#Attributes - number of people, cost to the company per person,
#Create a person
#Create another person
#Create a travel agency
#Book the 2 people to a trip to Brazil


class Travel_Agency(Corporation):
    def __init__(self, customers):
        self.customers = customers
        self.brazil = Trip_Planner("Brazil")
        self.spain = Trip_Planner("Spain")
        self.italy = Trip_Planner("Italy")
        self.product_list = [self.brazil, self.spain, self.italy]
        self.corportation = Corporation.products
        for i in self.product_list:
            i = str(i)
            self.corportation.append(i)
    cash = []
    def __str__(self):
        return str(self.spain)
    def booking(self, destination, people, price):
        print(people, "go on a trip to", destination, "for", price, "dollars.")
TA = Travel_Agency(c)
TA.booking(Brazil, customers3, 12000)

#Create 3 different trips
#Add the trips to the products list in the Travel Agency
#

#Attributes - starting point, and ending point, cost of the trip per person
#Attributes - number of people, cost to the company per person,
#Create a person
#Create another person
#Create a travel agency
#Book the 2 people to a trip to Brazil
