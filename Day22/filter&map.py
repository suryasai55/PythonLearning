#filter():
a=[10,20,30,40,70,90,99,105]
'''b=list(filter(lambda b:b/10,a))
print(b)'''
'''if a%2==0:
    print(a)'''
'''for i in a:
    if i%2!=0:
        print(i)'''
'''b=list(filter(lambda b:b%2==0,a))
print(b)'''
'''b=tuple(filter(lambda b:b%2==0,a))
print(b)'''

'''b=set(filter(lambda b:b%2==0,a))
print(b)'''


'''a=[[],(),{},set()," ",5,8.9,"python",8+9j,True,False]
b=list(filter(None,a))
print(b)'''


#map()->each object from a collection
'''a=[3,6,8,9,11,15,20,90]
b=[30,45,23,14,10,7,5,89]
c=list(map(max,(a,b)))
print(c)
d=list(map(min,(a,b)))
print(d)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''
'''a,b=input("enter the data").split(",")
print(a+b)'''


'''a,b=[x for x in input("enter x").split()]
print(a+b)'''


'''a=map(str,input("enter a value").split())
print(*a)

a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''d=input("enter key and value")
b=dict(i.split(":") for i in d.split(","))
print(b)'''
