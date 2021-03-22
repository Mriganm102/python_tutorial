import os
print(os.getcwd())

print(os.system('mkdir today'))
print(dir(os))
print(help(os))
import shutil
#print(shutil.copyfile('data.db', 'archive.db'))
import glob
print(glob.glob('*.py'))
import sys
print(sys.argv)
print(sys.stderr.write('Warning, log file not found starting a new one\n'))
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

import math
print(math.cos(math.pi / 4))
print(int(math.log(1024, 2)))
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))

print(statistics.median(data))

print(statistics.variance(data))

#from urllib.request import urlopen
#with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#    for line in response:
#        line = line.decode('utf-8')  # Decoding the binary data to text.
#        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#            print(line)

from datetime import date
now = date.today()
print(now)

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

p = zlib.crc32(s)
print(p)

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

def average(values):
    return sum(values) / len(values)
import doctest
doctest.testmod()
