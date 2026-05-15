Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
>>> a.count(" ")
3
>>> a.count(t)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.count(t)
NameError: name 't' is not defined
>>> a.count(a)
1
>>> a=5
>>> a.count(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.count(a)
AttributeError: 'int' object has no attribute 'count'
>>> #find a String
>>> a="python"
>>> a.find("t")
2
>>> a.find("O")
-1
>>> a.find("P")
-1
>>> a.find("python")
0
