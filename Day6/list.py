Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List
a=["python","java","c","c++"]
print(a)
['python', 'java', 'c', 'c++']
a.append("R")
a
['python', 'java', 'c', 'c++', 'R']
a.append(["ml,"ai"])
          
SyntaxError: unterminated string literal (detected at line 1)
a.append(["ml","ai"])
          
type(a)
          
<class 'list'>
a
          
['python', 'java', 'c', 'c++', 'R', ['ml', 'ai']]
a=["python","java","c","c++"]
          
a.extend(["ai","ml"])
          
a
          
['python', 'java', 'c', 'c++', 'ai', 'ml']
a.append("ai","ml")
          
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)
#extend
          
a.extend(["rust","cobalt"])
          
a
          
['python', 'java', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
#insert
          
a
          
['python', 'java', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
a.insert(2,"pascal"
         a
         
SyntaxError: '(' was never closed
a.insert(2,"pascal")
         
a
         
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
#index
         
a.index("4")
         
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.index("4")
ValueError: '4' is not in list
a.index(4)
         
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.index(4)
ValueError: 4 is not in list
a.index("c++
        
SyntaxError: unterminated string literal (detected at line 1)
a.index("c++")
        
4
a.index("my")
        
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.index("my")
ValueError: 'my' is not in list
a
        
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
#copy()
        
a.copy()
        
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
b=a.copy()
        
b
        
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
#clear()
        
a.clear()
        
a
        
[]
a=a.copy()
        
a
        
[]
b.copy()
        
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
a=b.copy()
        
b=a.copy()
        
b
        
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
b.clear()
        
b
        
[]
#sort()
        
a
        
['python', 'java', 'pascal', 'c', 'c++', 'ai', 'ml', 'rust', 'cobalt']
a.sort()
        
a
        
['ai', 'c', 'c++', 'cobalt', 'java', 'ml', 'pascal', 'python', 'rust']
b=[3,5,6,2,8,34,56,85,32,22,]
        
b.sort()
        
b
        
[2, 3, 5, 6, 8, 22, 32, 34, 56, 85]
#reverse()
        
a
        
['ai', 'c', 'c++', 'cobalt', 'java', 'ml', 'pascal', 'python', 'rust']
a.reverse()
        
a
        
['rust', 'python', 'pascal', 'ml', 'java', 'cobalt', 'c++', 'c', 'ai']
a.sort().reverse()
        
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.sort().reverse()
AttributeError: 'NoneType' object has no attribute 'reverse'
b=[True,False]
        
b.sort()
        
b
        
[False, True]
b.reverse()
        
b
        
[True, False]
b
        
[True, False]
a
        
['ai', 'c', 'c++', 'cobalt', 'java', 'ml', 'pascal', 'python', 'rust']
#pop()
        
a.pop()
        
'rust'
a
        
['ai', 'c', 'c++', 'cobalt', 'java', 'ml', 'pascal', 'python']
a.pop(2)
        
'c++'
a
        
['ai', 'c', 'cobalt', 'java', 'ml', 'pascal', 'python']
#remove()
        
a.remove("pascal")
        
a
        
['ai', 'c', 'cobalt', 'java', 'ml', 'python']
#count()
        
a.count()
        
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count("c")
...         
1
>>> a.count(" ")
...         
0
>>> a="surya"
...         
>>> len(a)
...         
5
>>> b=["surya"]
...         
>>> a.count(b)
...         
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.count(b)
TypeError: count() argument 1 must be str, not list
>>> a.count("surya")
...         
1
