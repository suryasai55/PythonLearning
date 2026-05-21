#conditions
#if condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")
'''

'''a=10
b=20
if a>b:
    print("true")'''

'''a=2
b=4
if a<=b:
    print("less")'''

'''a=6
b=9
if b>=a:
    print("greater")'''

'''a=7
b=10
if a!=b:
    print("not equal")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b:
    print("less")'''

'''a=int(input("a value:"))
if a>30:
    print("greater")'''

'''a="python"
if a=="python":
    print("true")'''

'''a=input("data:")
if a=="java":
    print("true")'''

#_______________________________________________________________________________________________________________________

#if condition using logical operators
#and,or,not
'''a=4
b=8
if a<b and b>a:
    print("true")'''

'''a=3
b=6
if a!=b and b>=a:
    print("true")'''


'''a=9
b=12
if a<=b or b>=a:
    print("true")'''

'''a=4
b=8
if a!=b or b==a:
    print("true")'''

'''a=4
b=8
if a<b or b>a:
    print("true")'''

'''a=7
b=9
if not a<b:
    print("less")'''

'''a=7
b=9
if not a>b:
    print("less")'''

'''a=7
b=9
if not a==b and b==a:
    print("less")'''

'''a=int(input())
b=int(input())
if not a==b and b==a:
    print("less")'''
#____________________________________________________________________________________________________________________________

#if condition by using identify operators
#is,is not

'''a=5
if type(a) is int:
    print("true")'''

'''a=5.0
if type(a) is float:
    print("true")'''

'''a="surya"
if type(a) is str:
    print("true")'''

'''a=5+4j
if type(a) is complex:
    print("true")'''

'''a=5
if type(a) is not bool:
    print("true")'''

'''a=5.1
if type(a) is not int:
    print("true")'''

#________________________________________________________________________________________________________________________

#if-condition by using membership operators

'''a=[10,20,30,40,50,60]
if 60 in a:
    print("true")'''

'''a=[10,20,30,40,50,60]
if 60 not in a:
    print("true")'''

'''a=[10,20,30,40,50,60]
if 70 in a:
    print("true")'''

'''a=input()
if 10 in a:
    print("true")'''#error

'''a=[1,2,3,4,5,6,7,8,9,10]
b=int(input())
if b  in a:
    print("true")'''

'''a=[1,2,3,4,5,6,7,8,9,10]
b=int(input())
if b not in a:
    print("true")'''
#_________________________________________________________________________________________________________________________

#if-else
#if-else conditions by using comparision operator

'''a=4
b=9
if a<b:
    print("true")
else:
    print("false")'''


'''a=4
b=9
if a>b:
    print("true")
else:
    print("false")'''

'''a=4
b=9
if a==b:
    print("true")
else:
    print("false")'''

'''a=int(input())
b=int(input())
if a!=b:
    print("true")
else:
    print("false")'''
#__________________________________________________________________________________________________________________

#if-else conditions by using logical operators
'''a=10
b=15
if a<b and b>a:
    print("true")
else:
    print("False")'''

'''a=10
b=15
if a!=b or b==a:
    print("true")
else:
    print("False")'''

'''a=10
b=15
if not a<=b and b>=a:
    print("true")
else:
    print("False")'''
#_______________________________________________________________________________________________________________________

#if-else conditions by using identify operators

'''a=4
if type(a) is int:
    print("true")
else:
    print("false")'''

'''a=int(input()
if type(a) is not int:
    print("true")
else:
    print("false")'''

'''a=int(input())
if type(a) is not int:
    print("true")
else:
    print("false")'''
#_______________________________________________________________________________________________________________________

#if-else conditions by using membership operators

'''a=[3,4,5,6,7,8,9]
b=int(input("a value"))
if b in a:
    print("true")
else:
    print("false")'''


'''a=[3,4,5,6,7,8,9]
b=int(input("a value"))
if b not in a:
    print("true")
else:
    print("false")'''
#____________________________________________________________________________________________________________________________


















