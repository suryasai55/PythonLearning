#oops
#syntax:
'''
class calssname():
    name="surya"
    age=28
    place="vja"
    def fname(method_name):
        print("Statement.........")
    obj=classname()
    obj.fname()'''

#class Declaration:
'''class Details():
    name="surya"
    age=28
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("surya",20,"vja")
a.display()
b=Details()
print(dir(b))
b.data("yeswanth",21,"vja")
b.display()'''

#object Initialization
class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input(),input(),input())
print(dir(a))
a.display()
