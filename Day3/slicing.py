Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Slicing
a="SuryaSai"
a[0:6]
'SuryaS'
a[0:4]
'Sury'
a[0:5]
'Surya'
a[:4]
'Sury'
a[4:]
'aSai'
a="work hard until you succeed"
a[20:26]
'succee'
a[20:27]
'succeed'
a[16:18]
'yo'
a[16:19]
'you'
a[10:15]
'until'
a[5:9]
'hard'
a[0:4]
'work'
a="the art of code"
a[-4:-1]
'cod'
>>> a[-4:0]
''
>>> a[-5:-1]
' cod'
>>> a[-7:-5]
'of'
>>> a[-11:-8]
'art'
>>> [-15:-12]
SyntaxError: invalid syntax
>>> a[-15:-12]
'the'
>>> a[-4:1]
''
>>> a[-4:]
'code'
>>> a="time is very precious"
>>> a[-8:]
'precious'
>>> a[-13:-7]
'very p'
>>> a[-13:-9]
'very'
>>> a[-21:-17]
'time'
