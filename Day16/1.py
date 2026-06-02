#print vs return

#Print:
'''print just shows the human user output in a console'''
#return:
'''return is used to retminate the function and gives back a value from the function'''

'''def cal(a,b):
    print(a+b)
cal(3,4)'''

'''def cal(a,b):
    return a+b
print(cal(5,6))'''
        

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,7)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(add(2,4))'''

#keyword and positional arguments:

'''def details(id,name,mail):
    id=10
    name="surya"
    mail="suryasaiofficial@gmail.com"
    print(id,name,mail)
details(id="id",name="name",mail="mail")'''

'''def details(id,name,mail):
    print(id,name,mail)
details(id=20,name="surya",mail="s@gmail.com")
details(id=30,name="sai",mail="ss@gmail.com")
details(40,"surya","surya@gmail.com")
details("abhishek","a@gmail.com",50)
details(mail="\nss@gmail.com\n",id="40\n",name="surya\n")'''

#default arguments

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice")'''


'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''


'''def Grocery(item="ghee",price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(1500)'''

#cake,price,qty

'''def cake(cake,price,qty):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cake("vanilla",2000,2)'''


'''def cake(cake="chocolate",price=4000,qty=2):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cake()'''

'''def cake(cake="strawberry",price,qty):
    print("item is %s" %cake)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cake(2000,2)'''
































