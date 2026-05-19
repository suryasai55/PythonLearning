Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"name":"surya","place":"vja","id":05}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
a={"name":"surya","place":"vja","id":"05"}
type(a)
<class 'dict'>
a.fromkeys()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.fromkeys()
TypeError: fromkeys expected at least 1 argument, got 0
a.fromkeys(id)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.fromkeys(id)
TypeError: 'builtin_function_or_method' object is not iterable
a.fromkeys("id")
{'i': None, 'd': None}
a.fromkeys(1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.fromkeys(1)
TypeError: 'int' object is not iterable
a.get("name")
'surya'
a.keys()
dict_keys(['name', 'place', 'id'])
a.values()
dict_values(['surya', 'vja', '05'])
a.setdefault(course,python)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.setdefault(course,python)
NameError: name 'course' is not defined
a.setdefault(name,sai)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.setdefault(name,sai)
NameError: name 'name' is not defined
a.setdefault("name","sai")
'surya'
a
{'name': 'surya', 'place': 'vja', 'id': '05'}
a.setdefault("course","python")
'python'
a
{'name': 'surya', 'place': 'vja', 'id': '05', 'course': 'python'}
a.update("name":"sai")
SyntaxError: invalid syntax
a.update(name="sai")
a
{'name': 'sai', 'place': 'vja', 'id': '05', 'course': 'python'}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop(name)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop(name)
NameError: name 'name' is not defined
>>> a.pop("name")
'sai'
>>> a
{'place': 'vja', 'id': '05', 'course': 'python'}
>>> a.popitem()
('course', 'python')
>>> sa
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    sa
NameError: name 'sa' is not defined. Did you mean: 'a'?
>>> a
{'place': 'vja', 'id': '05'}
>>> a.clear()
>>> a
{}
>>> a={"name":"surya","place":"vja","id":"05"}
>>> a.items()
dict_items([('name', 'surya'), ('place', 'vja'), ('id', '05')])
>>> a.fromkeys(a)
{'name': None, 'place': None, 'id': None}
>>> a.copy()
{'name': 'surya', 'place': 'vja', 'id': '05'}
