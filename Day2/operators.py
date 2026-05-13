Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthematic Operators
a=2
b=4

print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a**b)
16
print(a//b)
0
print(a/b)
0.5
print(a%b)
2
#Assingment Operators
a=5
b=8
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
13
a-=2
a
11
a*=3
a
33
a//=3
a
11
a/=2
a
5.5
a**=4
a
915.0625
a%=5
a
0.0625
a=5
b+=a
b
13
b-=3
b
10
b*=10
b
100
b//=5
b
20
b/=2
b
10.0
b**=2
b
100.0
b%=10
b
0.0
#Comparision Operators
a=5
b=10
a>b
False
a<b
True
b>a
True
b<a
False
a!=b
True
a=b
a=5
b=10
a==b
False
a>=b
False
a<=b
True
b>=a
True
b<=a
False
b=10
a=b
a==b
True
#Logical Operators
a=4
b=6
a<b and b>a
True
a>=b and b>=a
False
a<=b and b>=a
True
a==b and a!=b
False
a<b or b>a
True
a<=b and b<=a
False
a<=b or b<=a
True
a==b or a!=b
True
not True
False
not False
True
#Identify Operators
a=6
if type(a) is int:
    print("it is true")

    
it is true
if type(a) is not int:
    print("true:")

    

a="hii"
if type(a) is str:
    print("true")

    
true
if type(a) is not str:
    print("False")
... 
...     
>>> #Membership Operators:
...     
>>> a=2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print(5)
... 
...     
5
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> a="C","java","python"
>>> if "C" in a:
...     print("car")
... 
...     
car
>>> if "C" not in a:
...     print("bike")
... 
...     
