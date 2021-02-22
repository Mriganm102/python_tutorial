#while True:
#    print("Hello World")

#try:
#    x = int(input("Hello"))
#    print(x)
#except ValueError:
#    print("There was a value error")
#while True:
#    try:
#        x = int(input("Please try again"))
#        break
#    except ValueError:
#        print("Oops!    That was no valid number. Try again...")


def this_fails():
        x = 1 / 0


try:
        this_fails()
except ZeroDivisionError as err:
        print('Handling run-time error:', err)

#raise NameError('HiThere')

try:
    raise NameError("HiThere")
except NameError:
    print('An exception flew by')
#    raise


def func():
    raise IOError

#try:
#    func()
#except IOError:
#    raise RuntimeError("Failed to open database")
#
#try:
#    open('database.sqlite')
#except IOError:
#    raise RuntimeError from None
#
#try:
#    raise KeyboardInterrupt
#finally:
#    print('Goodbye, world!')

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")