Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
>>> a,b=b,a
>>> print("before swapping ",a,b)
before swapping  20 10
>>> peint("after swapping: %d %d" % (a,b))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    peint("after swapping: %d %d" % (a,b))
NameError: name 'peint' is not defined. Did you mean: 'print'?
>>> print("after swapping: %d %d" % (a,b))
after swapping: 20 10
>>> a=5.6
>>> b=6.5
>>> print("before swapping ",a,b)
before swapping  5.6 6.5
>>> print("after swapping: %f %f" % (a,b))
after swapping: 5.600000 6.500000
>>> print("after swapping: %f.2f %f.2f" % (a,b))
after swapping: 5.600000.2f 6.500000.2f
>>> print("after swapping: %.2f %.2f" % (a,b))
after swapping: 5.60 6.50
>>> a="python"
>>> b="java"
>>> a,b=b,a
>>> print("after swapping: %s %s" % (a,b))
after swapping: java python
