#every list com can be rewritten as a for loop but every for loop cant written as list
#list comprehension
#a=["surya","yeswanth","sourabh"]

'''b=str(a)
print(b.upper())
'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[exp for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''


'''a=[2,3,4,5,6,8,12,13]
a=[a*a for a in a]
print(a)'''

'''a=["surya","yeswanth","sourabh"]
a=[a.title() for a in a]
print(a)'''

'''a=[1,2,3,4,5]
a=[a for a in range(1,16)]
print(a)'''

#IF USAGE IN LIST COMPREHENSION
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i*i for i in range(16) if i%2==0]
print(a)'''


'''fruits=["banana","kiwi","dragon","berry","mango","apple"]
a=[i for i in fruits if "a" in i]
print(a)'''

#IF-ELSE USAGE IN LIST COMPREHENSION

'''a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
a1=str(a)
b1=str(b)
c=[a[i]+b[i] for i in range(len(a))]
print(c)





























