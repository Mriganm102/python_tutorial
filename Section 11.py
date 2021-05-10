a = 'abcdefghijklmnopqrstuvwxyz'
print(set(a))
import reprlib
print(reprlib.repr(set(a)))
import pprint
listlist = [["Blue", "Green"], "Black",
            [["Red", "Yellow"]],
            "White"]
pprint.pprint(listlist)
print(listlist)

import logging
logging.debug("Debugging Information")
logging.info("Information Message")
logging.warning("Warning:config file %s not found", 'server.conf')
logging.error("Error Continued")
logging.critical("Critical error -- shutting down")

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])

del a
print(gc.collect())


from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))

print(a[1:3])

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))

print(round(.70 * 1.05, 2))


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)