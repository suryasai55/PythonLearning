#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["pooja","ravali","appu"],
         "status":["p","a","p"]}

check(**details)'''


'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)

check()
details={"idnos":[10,20,30],
         "names":["pooja","ravali","appu"],
         "status":["p","a","p"]}
check(**details)'''


'''def check1(*a,**b):
    d=2
    print(a)
    print(b)
    for i in a:
            d=d+i
            print(d)
    print(a)
    for i,j in b.items():
        print(i)
check1(2,3,4,5,6)
details={"idnos":[10,20,30],
         "names":["pooja","ravali","appu"],
         "status":["p","a","p"]}
check1(2,3,**details)'''

#both * and **
def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,4,3,2,5,"python",5+9j,True,False)
final(*data)
details={"idnos":[10,20,30],
         "names":["pooja","ravali","appu"],
         "status":["p","a","p"]}
final(**details)
final(*data,**details)

