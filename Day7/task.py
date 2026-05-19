Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a[0:5]
>>> a2=a[6:10]
>>> a1.sort()
>>> a2.sort()
>>> a1.reverse()
>>> a2.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2
[7, 6, 3, 0]
>>> a=a2+a1
>>> a
[7, 6, 3, 0, 9, 8, 5, 2, 1]
>>> a2=[4,6,3,7,0]
>>> a2.sort
<built-in method sort of list object at 0x000001F2FA028680>
>>> a2.reverse
<built-in method reverse of list object at 0x000001F2FA028680>
>>> a=a2+a1
>>> a
[4, 6, 3, 7, 0, 9, 8, 5, 2, 1]
