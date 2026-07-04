#Hierarchical Inheritance
'''It means one parent class is inherited by multiple child classes'''
'''
class Employee():
    company_name=input("Enter the company")
    print(  company_name)
class Trainer(Employee):
    def train(self):
        print("teaches the code at",self.company_name)
class Developer(Employee):
    def develope(self):
        print("Develope the code at ",self.company_name)
obj=Trainer()
obj1=Developer()
obj.train()
obj1.develope()
'''
#Hybrid Inheritence
#It means combining more than one type of inheritence for example hierarchical + multiple inheritence
'''
class Person():
    name=input("Enter Name:")
    marks=int(input("Enter marks:"))
    t_name=input("Enter the Trainer Name:")
    print("Person class")
    print(name,marks)
class student(Person):
    def stu_details(self):
        print("student class")
        print("student name is :",self.name)
        print("Student marks are:",self.marks)
class trainer(Person):
    def trainer_details(self):
        print("trainer class")
        print("Name of the Trainer:",self.t_name)
class teaching_assisstant(student,trainer):
    def assist(self):
        print("assisst class")
        print("trainer and student details are:",self.name,self.marks,self.t_name)
o=student()
o.stu_details()
o1=trainer()
o1.trainer_details()
o2=teaching_assisstant()
o2.assist()
'''
#super():

class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("pooja",28)
print(a.name)
print(a.age)
        
