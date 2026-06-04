def ticket(gender,age):
    price=1000
    age=int(input("enter your age"))
    gender=input("enter Gender as m or f")
    if gender=="m" and age>60:
        print("Discount is 30% amount is",price*0.7)
    elif gender=="m" and age<60:
        print("amount is ",price)
    elif gender=="f" and age<60:
        print("amount is ",price*0.7)
    elif gender=="m" and age>60:
        print("amount is ",price*0.5)
ticket("gender","age")
        
