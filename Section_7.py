year = 2021
event = 'party'
print(f"It's {year} and time to go to a {event}")
yes_votes = (5_6_7)
no_votes = (10_11_12)
print("{:-9}".format(yes_votes))

file_name = "firstfile.text"
file_handle = open(file_name, "w")
file_handle.write("Hello")
file_handle.write(" World")
file_handle.close()
file_handle = open(file_name, "r")
file_text = file_handle.read()
file_handle.close()
print(file_text)
pickle_this = {"1": "a", "2": "b", "3": "c"}
import json
print(json.dumps(pickle_this))
import yaml
print(yaml.dump(pickle_this))
pickle_jsonstring = json.dumps(pickle_this)
pickle_jsonfilename = "pickle.json"
pickle_yamlfilename = "pickle.yaml"
pickle_yamlstring = yaml.dump(pickle_this)
file_handle = open(pickle_jsonfilename, "w")
file_handle.write(pickle_jsonstring)
file_handle.close()
file_handle = open(pickle_yamlfilename, "w")
file_handle.write(pickle_yamlstring)
file_handle.close()

s = ("Hello, world")
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = (f"The value of x is {repr(x)} and y is {repr(y)}...")
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

print(repr((x, y, ('spam', 'eggs'))))

import math
print(f"The value of pi is approximately {math.pi:3f}.")
table = {"Sjoerd" : 4127, "Jack" : 4098, "Dcab" : 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

import math
print('The value of pi is approximately %5.3f.' % math.pi)

f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()


