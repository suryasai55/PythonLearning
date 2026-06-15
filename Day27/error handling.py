'''
Error Handling:
1)syntax error -> compile error
2)runtime error ->During Execution time
3)logical error ->error in logic (invisible)
'''

#Exception handling:

try:
    a=int(input())
    b=int(input())
    c=a//b
    print(c)
except:
    print("Invalid please choose again")
else:
    print("No exceptions")
finally:
    print("end")



 
