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
        brazil = Trip_Planner("Brazil")
        spain = Trip_Planner("Spain")
        italy = Trip_Planner("Italy")
        self.product_list = [brazil, spain, italy]
    cash = []
    def booking(self, destination, people, price):
        pass

#Create 3 different trips
#Add the trips to the products list in the Travel Agency
#
class Trip_Planner:
    def __init__(self, location):
        self.location = location
    people = []
    starting_point = ''
    ending_point = ''
    per_person = []
class Person:
    def __init__(self, person):
        self.person = person

#Attributes - starting point, and ending point, cost of the trip per person
#Attributes - number of people, cost to the company per person,
#Create a person
#Create another person
#Create a travel agency
#Book the 2 people to a trip to Brazil
