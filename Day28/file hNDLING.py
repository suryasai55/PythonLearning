#File Handling
#write()
'''a=open("surya.txt","w")
a.write("python")
a.close()'''

'''a=open("surya.txt","w")
a.write("code")
a.close()'''

'''a=open("surya.txt","a")
a.write("\n codegnan")
a.close()'''

'''a=open("surya.txt","w")
b=input("Data:")
a.close()'''

'''
a=open("surya.txt","a")
a.write(input("data:"))
a.close()
'''

#read()
a=open("surya.txt")
#print(a.read())#reads complete file
#print(a.readline())#only first line
#print(a.read(5))
#print(a.readlines())
a.close()

#writelines()->it makes every object side by side
'''a=["python","java","c","ml","ds"]
b=open("pooja.txt","w")
b.writelines("\n".join(a))
b.close()'''

a=open("E:\surya-portfolio/index.html")
print(a.read())
