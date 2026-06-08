#yield vs return
'''
def mygen():
    #return "python"
    #return "java"
    #return "ml"
    return "python","java","ml"
print(*mygen())

def mygen():
    yield "vja"
    yield "hyd"
    yield "vzg"
print(*mygen(),end=" ")
'''
#next()
'''d=mygen()
print(next(d))
print(next(d))
print(next(d))
#print(next(d))'''
'''
#fromkeys()
a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"pooja")
print(b)
b["c","o","g"]="surya"
print(b)
'''
#eval()
'''a=float(input())
b=float(input())
print(a+b)'''
'''
while True:
    a=input()
    b=input()
    print(a+b)
    '''
'''
while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection
'''a=[10,20,30,40,5060]
names=["vardhan","dinesh","praneeth","surya","vishnu","sai"]
print(a+names)
'''
'''b=zip(a,names)
print(b)'''
'''
c=list(zip(a,names))
print(c)
c=tuple(zip(a,names))
print(c)
'''


#enumerate()->we can give counter to the collection
'''names=["anand","srikar","sasi","dileep","ganesh"]
''''''for i in range(len(names)):
    print(i,names[i])'''
'''b=dict(enumerate(names))
print(b)
b=dict(enumerate(names,100))
print(b)
'''
##annonymous functions are name less functions and we use a keyword called as lambda to create annonymous functions.
#write a function to calculate 2*x+5 where x=5

'''def a(x=5):
    print(2*x+5)
a()'''

#syntax

#a=lambda ard:expr

'''a=lambda x:2*x+6
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

'''a="python"
b=lambda x:x.upper()
print(b(a))'''

'''a="python course"
b=lambda x:x.title()
print(b(a))'''

'''a=input()
b=input()
f=a+" "+b
c=lambda x:f.title()
print(c(f))'''


'''a=input()
b=input()
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=[x for x in input("names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

a,b=input("names:").split(",")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))


    
