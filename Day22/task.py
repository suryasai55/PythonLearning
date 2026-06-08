height=float(input("Height in cm"))
weight=float(input("weight in kg's))
bmi=weight/(height*height)
if bmi<=18.5:
    print("under Weight")
elif 18.5<bmi<=24.5:
    print("Normal")
elif 24.5<bmi<=29.5:
    print("over weight")   
