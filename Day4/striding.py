Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Striding
a="data science"
a[::]
'data science'
a[::2]
'dt cec'
>>> a[::1]
'data science'
>>> a="machine learning"
>>> a[1:10:3]
'ai '
>>> a[::]
'machine learning'
>>> a[1:14:3]
'ai ai'
>>> a="python course"
>>> a[-2:-12:-4]
'sch'
>>> a[-3:-13:-2]
'ro ot'
>>> a[-1:-1:-3]
''
>>> a[-1:-9:-3]
'eu '
>>> a[9:4:3]
''
>>> #IN POSITIVE STRIDING HIGHEST TO LOWEST NOT POSSIBLE
>>> a[-6:-4:-2]
''
>>> #IN negative Striding lowest to highest not possible
