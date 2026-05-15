Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Escape sequences
#\n-> new line
#\t-> tab sapce
a="name\n mobileno \t mailid"
print(a)
name
 mobileno 	 mailid
a="name\nmobileno\t mailid"
print(a)
name
mobileno	 mailid
print("name\nmobileno\t mailid")
name
mobileno	 mailid
b="name:pooja\nmobileno:903432426\tmail:suryasai@gmail.com"
print(b)
name:pooja
mobileno:903432426	mail:suryasai@gmail.com
#Replace
a="wait until you succeed"
a.replace(wait,work)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.replace(wait,work)
NameError: name 'wait' is not defined
a.replace("wait","work")
'work until you succeed'
print(a)
wait until you succeed
b="wait wait until you succeed"
print(b)
wait wait until you succeed
replace("wait","work")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    replace("wait","work")
NameError: name 'replace' is not defined
>>> a.replace("wait","work")
'work until you succeed'
>>> b.replace("wait","work")
'work work until you succeed'
>>> print(b)
wait wait until you succeed
>>> a=a.replace("wait","work")
>>> print(a)
work until you succeed
>>> #strip()
>>> a="          surya             "
>>> a.strip()
'surya'
>>> a
'          surya             '
>>> a=a.lstrip()
>>> a
'surya             '
>>> a=a.rstrip()
>>> a
'surya'
