Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets()
a={4,6,7,"surya",5+9j,True,False}
print(a)
{False, True, (5+9j), 'surya', 4, 6, 7}
type(a)
<class 'set'>
#add()
a={4,5,6,7,8,9,10}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 10, 20}
a.add(5)
a
{4, 5, 6, 7, 8, 9, 10, 20}
a.add(11)

a
{4, 5, 6, 7, 8, 9, 10, 11, 20}
a={2,3,4,5,6,7,8}
b={5,6,7,8}
a.issubset(b)
False
b.issubset(a)
True
a.issuperset(b)
True
b.issuperset(a)
False
a=set(input())
2,3,4,5,6
a
{'3', '2', '5', '4', ',', '6'}
a=tuple(input())
1,2,3,4,5
a
('1', ',', '2', ',', '3', ',', '4', ',', '5')
#Union
a={4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a
{4, 5, 6, 7, 8, 9}
a.intersection(b)
{4, 5, 6}
b.intersection(a)
{4, 5, 6}
#update()
a={1,2,3,4,5}
b={3,4,5,6,7}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7}
a
{1, 2, 3, 4, 5, 6, 7}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7}
b
{1, 2, 3, 4, 5, 6, 7}
a={10,20,30,40,50,60}
b={40,50,60,70,80,90}
a.difference(b)
{10, 20, 30}
b.difference(a)
{80, 90, 70}
#symmetric difference()
a={2,3,4,5,6,7,8,9,10}
b={4,5,6,7,8,9,10,11,12}
a.symmetric_difference(b)
{2, 3, 11, 12}
b.symmetric_difference(a)
{2, 3, 11, 12}
a={3,4,5,6,7,8}
b={1,2,3,4,5,6,7,8,9}
#difference_update()
a.difference_update(b)
a
set()
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a={1,2,3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{1, 2, 3}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10}
a={11,12,13,14,15,16}
b
{4, 5, 6, 7, 8, 9, 10}
#intersection_update()
b={12,13,14,15,16,17}
a.intersection_update(b)
a
{12, 13, 14, 15, 16}
b.intersection_update(a)
b
{12, 13, 14, 15, 16}
a
{12, 13, 14, 15, 16}
b
{12, 13, 14, 15, 16}
#symmetric_difference_update
a.symmetric_difference_update
<built-in method symmetric_difference_update of set object at 0x0000026DA18B51C0>
a.symmetric_difference_update
<built-in method symmetric_difference_update of set object at 0x0000026DA18B51C0>











a.symmetric_difference_update(b)
a
set()
a={5,6,7,8,9,10}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
b.symmetric_difference_update(a)
b
{5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 7, 8, 9, 10}
a={3,4,5,6,7,8}
a.copy()
{3, 4, 5, 6, 7, 8}
a.clear()
A
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
set()
a={4,5,6,7,8,9}
a.pop()
4
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
a
{6, 7, 8, 9}
>>> #discard()
>>> a.discard(8)
>>> a
{6, 7, 9}
>>> b
{5, 6, 7, 8, 9, 10}
>>> #isdisjoint()
>>> a.isdisjoint(b)
False
>>> a={1,2,3,4,5}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
True
>>> b.iadisjoint(a)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    b.iadisjoint(a)
AttributeError: 'set' object has no attribute 'iadisjoint'. Did you mean: 'isdisjoint'?
>>> b.isdisjoint(a)
True
>>> a={3,4,5,6,7,8,9}
>>> len(a)
7
>>> #set object has no attributes 'index'  and  'count'
