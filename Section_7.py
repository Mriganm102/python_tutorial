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
            money = 1.07 * money
            money3 = (money * (random.randint(0, 200) - 100) * percent) / 100
            money = money + money3
            money = round(money, 2)
            money1.append(money)
        import matplotlib.pyplot as mat
        mat.plot(money1)
        mat.show()
        self.money1 = money1
        print(money1)
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
Account(5000, 0.2, 50, 40)
account = Account(5000, 0.2, 50, 40)
account.json()
account.yaml()