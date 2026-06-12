#sys module
'''import sys
#print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)
'''

#os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir())                                                                         
print(os.listdir())'''

#random module:
'''To generate random number in python,randint function in used to generate random numbers
this function is definied in random modules
python defines a set of functions that are used to generate or manipulate random numbers through the random module.'''

'''import random
#a=random.sample(range(10,50),1)
while True:
a=random.randint(1,69)
print(a)'''

#choice()
'''import random
a=[10,30,50,70,90]
b=random.choice(a)
print(b)'''




import random
while True:
    input("Roll of the dice")
    a=random.randint(1,6)
    print(a)
    b=int(input("Choose the options 1.Yes 2.No"))
    if b==1:
        pass
    else:
        break
    
    
    
