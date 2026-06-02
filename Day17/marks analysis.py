print("python",end="!")
print("rocks")
a=int(input("enter no. of students"))
l=[]
for i in range(1,a+1):
    students=input(f"marks of student is {i}:")
    l.append(students)
print("total students",a)
print(l)

print(max(*students))
print(min(*students))
print(sum(l))
