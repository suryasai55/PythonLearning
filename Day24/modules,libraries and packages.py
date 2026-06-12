'''Difference between Moudule , library and Package:


Module:
    A module in python is a single python file it consists python code
    It typically consists of functions,classes and variables that can be used in other python scripts or programs
    Examples od modules include math.py,random.py or mymodule.py


Package:
    A package in python is a directory containing one or ,\more python modules and an __init__.py file
    The __init__.py file can be empty or contain initialization code for the package
    Examples of packages include numpy,pandas,django

Library:
    Libraries can consists of multiple modules and packages,organised to serve a particular purpose or domain
    Examples of Libraries such as requests,numpy,pandas and matplotlib

Note:
    Every ppython file is a module and import is a keyword and every python file is saved internally with vsriable name as __main__.
'''

#math module


'''import math
print(math.pi)
print(math.pi*3)
print(math.log(2))
print(math.factorial(5))
print(math.sin(30))
print(math.cos(60))
print(pow(2,4))
print(math.ceil(2.99))
print(math.floor(4.899))'''

'''from math import pi,sqrt,log,sin,cos,factorial
print(pi)
print(factorial(10))
print(log(4))'''

n=int(input())
for i in range(1,21):
    print(f"{n} x {i} = {n*i}")
    
