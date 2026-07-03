#diff b/w _ and __:
'''
we generally use it for private variables,that means when ever we use __ our python interpreter treats it as a special
variable in order to avoild name conflits with methods and inner classes.
'''
'''
class Employee1():
    def __init__(self):
        self.name="surya"
        self._mailid="surya@codegnan.com"
        self.__salary=10000
class Employee2():
    def __init__(self):
        self.name="Yeswanth"
        self._mailid="yeswanth@srm.com"
        self.__salary=10000
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee1__salary)
b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._Employee2__salary)
'''

#polymorphism:
#operators overloading
'''
a=2;b=6
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(6))
print(a.__pow__(2))
print(a.__eq__(2))
print(a.__le__(5))
print(a.__ge__(11))
print(a.__ge__(12))
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a.__add__(b))
a="Surya"
b="Sai"
print(a.__add__(b).title())
'''

#Operator Overriding
'''
class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return se
    lf.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(4)
print(x+y)
'''
'''
class New():
    def sum(self,a=None,b=None,c=None):
      if a!=None and b!=None and c!=None:
          print("The sum is", a+b+c)
      elif a!=None and b!=None:
          print("The prooduct is",a+b)
      else:
          print("Programs ends.........")
a=New()
a.sum()
a.sum(4,5,6)
a.sum(6,3)
'''

class New():
    def sum(self,a=5,b=6,c=2):
      if a!=5 and b!=6 and c!=2:
          print("The sum is", a+b+c)
      elif a!=5 and b!=6:
          print("The prooduct is",a+b)
      else:
          print("Programs ends.........")
a=New()
a.sum()



















