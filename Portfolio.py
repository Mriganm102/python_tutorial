import random
class Account:

    def __init__(self, start, interest, randomI, years):

        self.interest = interest
        self.randomI = randomI
        self.years = years
        percent = randomI / 100
        money1 = []
        money = 0
        for i in range(0, years):
            money = start + money
            interest = interest/100
            money = (1+interest) * money
            money3 = (money * (random.randint(0, 200) - 100) * percent) / 100
            money = money + money3
            money = round(money, 2)
            money1.append(money)
        self.money1 = money1
    def plot(self):
        money1 = self.money1
        import matplotlib.pyplot as mat
        mat.plot(money1)
        mat.show()
    def json(self):
        json_simulation = (self.money1)
        import json
        print(json.dumps(json_simulation))
        jsonstring = json.dumps(json_simulation)
        jsonfilename = "simulation.json"
        file_handle = open(jsonfilename, "w")
        file_handle.write(jsonstring)
        file_handle.close()
    def yaml(self):
        yaml_simulation = self.money1
        import yaml
        print(yaml.dump(yaml_simulation))
        yamlfilename = "simulation.yaml"
        yamlstring = yaml.dump(yaml_simulation)
        file_handle = open(yamlfilename, "w")
        file_handle.write(yamlstring)
        file_handle.close()
    def __str__(self):
        return str(self.money1)
account = Account(start=5000, interest=0.2, randomI=50, years=4)
account.plot()
print(str(account))
#account.json()
#account.yaml()


class Portfolio:
    def __init__(self, accounts, money, years, interest):
        self.accounts = accounts
        self.money = money
        self.years = years
        self.interest = interest
        self.index = 0
        list1 = [Account(self.money, self.interest, 50, self.years) for i in range(0,self.accounts)]
        #list1.append(account)
        self.index = len(list1)
        self.list1 = list1
        #return self
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == self.accounts:
            raise StopIteration
        return self.list1[self.index]
    def __str__(self):
        return str([str(account) for account in self.list1])
    def plot(self):
        import matplotlib.pyplot as mat
        for account in self.list1:
            mat.plot(account.money1)
        mat.show()
portfolio = Portfolio(years=5, money=3569, accounts=2, interest=2)
print(portfolio)
iter(portfolio)
#[account.plot() for account in portfolio.list1]
portfolio.plot()
#for i in account.money1:
#    print(i)


