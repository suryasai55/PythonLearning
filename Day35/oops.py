#method Overriding:
'''
class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()
'''
'''
class Vehicals():
    def sound(self):
        print("Vehicals can make sound")
class Car():
    def sound(self):
        print("jaguar buzzzz...")
class bike():
    def sound(self):
        print("kawasaki Ninja wroomm....")
a=Vehicals()
b=Car()
c=bike()
a.sound()
b.sound()
c.sound()
'''

#inheritence:

#single Inheritence:
'''
class RBI():
    cash=100000
    def available_cash(cls):
        print("available cash is:",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print("new cash is:",cls.cash+RBI.cash)
a=HDFC()
a.new_cash()
b=RBI()
b.available_cash()
'''
#Multiple inheritence:
'''
class father():
    weight=80
    def wt1(wt):
        print("available cash is:",wt.weight)
class mother():
    height=175
    def ht1(ht):
        print("available cash is:",ht.height)
class kid(father,mother):
    print("DOB is:10-11-1005")
    def kid_wt(wt):    
        print("kid weight is:",father.weight)
    def kid_ht(ht):
        print("kid height is:",mother.height)
a=kid()                                                                                                                                                                                                                                                                                                                                                                                 
a.kid_wt()
a.kid_ht()
'''
#multi level inheritence
'''
class gfather():
    weight=80
    def wt1(wt):
        print("available cash is:",wt.weight)
class father(gfather):
    height=175
    def ht1(ht):
        print("available cash is:",ht.height)
class kid(father):
    print("DOB is:10-11-1005")
    def kid_wt(wt):    
        print("kid weight is:",gfather.weight)
    def kid_ht(ht):
        print("kid height is:",father.height)
a=kid()                                                                                                                                                                                                                                                                                                                                                                                 
a.kid_wt()
a.kid_ht()
'''




