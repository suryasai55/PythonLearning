Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuples
>>> #immutable
>>> a=(4,4.5,"python",8+9j,True,False)
>>> type(a)
<class 'tuple'>
>>> print(a)
(4, 4.5, 'python', (8+9j), True, False)
>>> a.count(8+9j)
1
>>> len(a)
6
>>> a.index("python")
2
