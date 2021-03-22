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
#    location = self.location
    people = []
    starting_point = ''
    ending_point = ''
    per_person = []
class Person:
    def __init__(self, person):
        self.person = person
        self.people = Trip_Planner.people
        self.people.append(self.person)
        print(self.people)
        b = self.people

Person("Al")
Person("Jill")
a = Trip_Planner("Brazil")



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
    def booking(self, destination, people, price):
        if destination == None:
            destination = str(a)
        if people == None:
            people = Person(self.people)
        print(str(people), "go on a trip to", destination, "for", price, "dollars.")
Travel_Agency.booking(self="", destination=None, people=None, price=1200)


#Create 3 different trips
#Add the trips to the products list in the Travel Agency
#

#Attributes - starting point, and ending point, cost of the trip per person
#Attributes - number of people, cost to the company per person,
#Create a person
#Create another person
#Create a travel agency
#Book the 2 people to a trip to Brazil
