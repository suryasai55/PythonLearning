'''Generators :
    No tuple comprehension in above cases  if we remove those braces[] and keep () then the outcome is generator'''

'''a=[i for i in range(16)]
print(a)
type(a)'''

a=(i for i in range(16))
'''print(*a)
print(type(a))'''
#print(list(a))
#print(tuple(a))
#print(set(a))

#Generators:
'''A generator is also a function which can be used as an iterator(loop) by producing group of values where we use
yield key word.
                            yeild vs return
            return will terminate the function where as yield can pass the function and go on with every successive
            iteration'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        #yeild a
        a=a+1
        yield a
print(*check(a,b))'''

a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))
