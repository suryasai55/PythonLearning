#encapsulation :- conmbines multiple units into single unit

#public data
'''
class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()
'''
#______________________________________________________________________________________________________________________
'''
class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)
'''

#______________________________________________________________________________________________________________________
'''
class parent():
    __privatedata="surya"
    def method1(slef):
        print(slef.__privatedata)
class child(parent):
    def method2(slef):
        print(slef._parent__privatedata)

obj1=child()
obj1.method1()
obj1.method2()
'''
#______________________________________________________________________________________________________________________

'''Abstraction:
    Hiding Unnecessary information from user is called abstraction 


Abstract class:
    if a class contain one or more than one abstract method then the class is called abstract class.

Abstract Method:
    If the method is declared without implementation is called abstract method.'''

#abstraction
'''
class parent():
  def method1(self):
      pass
a=parent()
a.method1()
'''
'''
class parent():
    def method1(self):
        print("data")
a=parent()
'''
'''
class A(ABC):
    def method(self):
        print("python")
obj1=A()
obj1.method1()
'''
'''from abc import ABC,abstract method'''
'''
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is executed")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj.method3()
'''
        
        















