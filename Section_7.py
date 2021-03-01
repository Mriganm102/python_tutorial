
class Account:

    def __init__(self, start, interest, random, years):
        self.interest = interest
        self.random = random
        self.years = years
        percent = random / 100
        money1 = []
        money = 0
        for i in range(0, years):
            money = start + money
            money = 1.07 * money
            money3 = money * percent
            money = money + money3
            money = round(money, 2)
            money1.append(money)
        import matplotlib.pyplot as mat
        mat.plot(money1)
        mat.show()

        print(money1)
        def json(self):
            json_simulation = (money1)
            import json
            print(json.dumps(json_simulation))
            jsonstring = json.dumps(json_simulation)
            jsonfilename = "simulation.json"
            file_handle = open(jsonfilename, "w")
            file_handle.write(json_simulation)
            file_handle.close()
        def yaml(self):
            json_simulation = {money1}
            import yaml
            print(yaml.dump(json_simulation))
            yamlfilename = "simulation.yaml"
            yamlstring = yaml.dump(json_simulation)
            file_handle = open(yamlfilename, "w")
            file_handle.write(money1)
            file_handle.close()
Account(5000, 0.2, 8, 13)