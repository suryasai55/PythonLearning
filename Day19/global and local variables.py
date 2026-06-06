#Local and Global Variables:
#----------------------------
#A VARIABLE IN INSIDE THE FUNCTION AND OUT SIDE THE FUNCTION IS GLOBAL AND LOCAL VARIABLES
#A variable is defined above the function and is accessible to the entire global space is called global variable
#A variable inside the  finction is called local variable.

'''a=2
def check():
    print("inside value is:",a)
check()
print("outside value is ",a)'''

#Second case:
'''a=3
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()'''

#third case
'''a=4
b=8
def check2():
    a=6
    print("inside value is ",a)
    a=10
    print("updated value",a+5)
    b=12
    b=a+b
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is ",b)'''

#Usage of global keyword:
#When user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we need to use global keyword

#global keyword
'''a=5
def final():
    global a,b
    print("Inside value is ",a)
    a=7
    print("updated value is",a)
    global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#ASCII
#chr()
'''chr(90)
chr(65)
chr(23)
chr(91)
#ord()
ord("a")
ord("z")


for i in range(97,123):
    print(chr(i),end=" ")
for i in range(65,91):
    print(chr(i),end=" ")'''

name=input("enter name:")
for i in name:
    print(i,ord(i))
    
















