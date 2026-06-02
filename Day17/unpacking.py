#* id used to unpack the elements

'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''a=(10,20,30,40,50)
print(a)
print(*a)'''

'''a={10,20,30,40,50}
print(a)
print(*a)'''

'''a={"year":2026,"month":"may"}
print(a)
print(*a)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''


'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''#error

'''*a,b,c=2,3,4,5,6,7,8,9
print(*a)
print(b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error


'''a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''


'''a,b,c="cod"
print(a)
print(b)
print(c)'''


'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''



'''def cal(a,b):
    a=int(input())
    b=int(input())
    c=int(input("choose options
                      1.add
                      2.subtract
                     3.multiply"))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    else:
        print("choose valid option")
cal("a","b")'''



'''def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)
def cal(a,b):
    a=int(input())
    b=int(input())
    c=int(input("choose options
                      1.add
                      2.subtract
                     3.multiply"))
    if c==1:
        print(add(a,b))
    elif c==2:
        print(sub(a,b))
    elif c==3:
        print(mul(a,b))
    else:
        print("choose valid option")
cal("a","b")'''



'''def split(m,a):
    m=int(input())
    a=int(input())
    bill=a//m
    print("Bill per person:",bill)
split("a","b")'''

'''def split(m,a):
    m=int(input())
    a=int(input())
    bill=a//m
    print("Bill per person:{}".format(bill))
split("a","b")'''

'''def split(m,a):
    m=int(input())
    a=int(input())
    bill=a//m
    print(f"Bill per person:{bill}")
split("a","b")'''

'''def split(m,a):
    m=int(input())
    a=int(input())
    bill=a//m
    print("Bill per person:{}".format(bill))
split("a","b")'''

'''def split(m,a):
    m=int(input())
    a=int(input())
    print(f"Bill per person:{a//m}")
split("a","b")'''

'''def split(m,a):
    m=int(input())
    a=int(input())
    print("Bill per person:{}".format(a//m))
split("a","b")'''


#variable Length:
            #variable length arguments are automatically stores in tuple and we use * arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[4,5,6,7,8,9]
check(*b)
c=(7,8,9,10)
check(*c)
d={"name":"pooja","city":"vij"}
check(*d)
check(d)'''

'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d,"pooja") 
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,2,3,5,6,7)
check1(4,2,3,5,2,3,4.2,"pooja")'''

'''
#max()
print(max(5,6,7,8,9,10,20))

#min
print(min(3,4,5,6,7,8,9,10))'''

'''a=2,3,4,5,6,7,8,9
print(sum(a))'''


















