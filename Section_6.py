import fibo

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)

fib = fibo.fib
print(fib(500))

import fibo as fib
fib.fib(500)

from fibo import fib as fibonnaci
fibonnaci(500)

from fibo import fib as baz
baz(500)

import sys
sys.path.append('/ufs/guidp/lib/python')

print(dir(print))
print(dir(fibo))
print(dir(set))
print(dir(dir))
print(dir(input))
print(dir(zip))
print(dir(int))
