Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#upper
a="surya"
a=a.upper()
a
'SURYA'
a.lower()
'surya'
a=a.lower()
a.capitalize()
'Surya'
a="i am in the class"
a.title()
'I Am In The Class'
#here we used the methods such as upper() , lower(), capitalize(), title()
#_______________________________________________________________________________
#_______________________________________________________________________________
#true or flase methods in strings
a="code"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="code gnan"
b.isalpha()
False
c="codegnan"
c.isalpha()
True
a.startswith("a")
False
a.startswith("c")
True
a.endswith("e")
True
a="2345"
a.isdigit()
True
a="@suryasai22"
a.isalnum()
False
a="suryasai22"
a.isalnum()
True
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
a=a.split()
b=" i am learning python"
b.split()
['i', 'am', 'learning', 'python']
"\n".join(a)
'python\njava\nc\nc++'
""\n.join(a)
SyntaxError: unexpected character after line continuation character
"".join(a)
'pythonjavacc++'
" ".join(a)
'python java c c++'
a=" ".join(a)
a
'python java c c++'
" \n ".join(a)
'p \n y \n t \n h \n o \n n \n   \n j \n a \n v \n a \n   \n c \n   \n c \n + \n +'
#concatenation

a="python"
b="course"
c=a+b
c
'pythoncourse'
fname="surya"
lname="sai"
full_name=fname+" "+lname
print(full_name)
surya sai
print(full_name.title())
Surya Sai
full_name=(fname+" "+lname).title()
full_name
'Surya Sai'
#formatting
a=2
print("The number is :",a)
The number is : 2
b="vijayawada"
print("The city I live in is :",b)
The city I live in is : vijayawada
a"motu"
SyntaxError: invalid syntax
a="motu"
>>> b="patlu"
>>> print("hello {} \n hello {}").format(a,b)
hello {} 
 hello {}
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print("hello {} \n hello {}").format(a,b)
AttributeError: 'NoneType' object has no attribute 'format'
>>> print("hello {} \n hello {}".format(a,b))
hello motu 
 hello patlu
>>> print("hello {} \nhello {}".format(a,b))
hello motu 
hello patlu
>>> #fstring
>>> a="chota"
>>> b="bheem"
>>> print((f"hello {a}{b}").title)
<built-in method title of str object at 0x0000018890AEE5B0>
>>> print((f"hello {a}{b}").title())
Hello Chotabheem
>>> print((f"hello {a} {b}").title())
Hello Chota Bheem
>>> \n.join(a)
SyntaxError: unexpected character after line continuation character
