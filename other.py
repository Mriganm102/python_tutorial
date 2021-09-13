import math
print("This is a function to calculate the area of your 2d shape")
a = input("What is your shape?")
if a == "circle":
    radius = int(input("What is the radius of the circle?"))
    cunit = input("What is the unit?")
    carea = int((radius*radius)*(math.pi))
    print(f"The area of the {a} is {carea} {cunit}")
if a == "square":
    length = int(input(f"What is the length of the {a}"))
    squnit = input("What is the unit?")
    sqarea = length**2
    print(f"The area of the {a} is {sqarea} {squnit}")
if a == "rectangle":
        length = int(input(f"What is the length of the {a}"))
        width = int(input(f"What is the width of the {a}"))
        squnit = input("What is the unit?")
        sqarea = length * width
        print(f"The area of the {a} is {sqarea} {squnit}")
if a == "parallelogram":
        length = int(input(f"What is the length of the {a}"))
        width = int(input(f"What is the width of the {a}"))
        squnit = input("What is the unit?")
        sqarea = length * width
        print(f"The area of the {a} is {sqarea} {squnit}")
if a == "trapezoid":
        base1 = int(input(f"What is the length of base 1 of the {a}"))
        base2 = int(input(f"What is the length of base 2 of the {a}"))
        length = (base2+base1)/2
        width = int(input(f"What is the height of the {a}"))
        squnit = input("What is the unit?")
        sqarea = length * width
        print(f"The area of the {a} is {sqarea} {squnit}")


