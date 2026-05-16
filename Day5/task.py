Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=3
>>> b=5
>>> #with variable
>>> a=4
>>> b=2
>>> c=4*2
>>> print(f"{c}")
8
>>> print("the product is: {}".format(c))
the product is: 8
>>> #without variable
>>> print(f"the product is {a*b}")
the product is 8
>>> print("the product is {}".format(a*b))
the product is 8
>>> a=10
>>> b=20
>>> a,b=b,a
>>> temp=o
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    temp=o
NameError: name 'o' is not defined
temp=0
temp=a
a=b
b=a
a
10
b
10
a=10
b=20
a=temp
temp=b
b=a
a
20
b
20
a=10
b=20
temp=a
a=b
b=temp
a
20
b
10
a=a+b
a=a-b
b=a-b
a
20
b
10
a=a+b
b=a-b
a=a-b
a
10
b
20
