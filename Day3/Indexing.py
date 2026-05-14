Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[5]
'a'
a[8]
'd'
a[0,6]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[0,6]
TypeError: string indices must be integers, not 'tuple'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="I am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a="simple is better than complex"
a[22]
'c'
a[22]+a[23]+a[24]+a[25]+a[26]+a{27]+a[28]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
b="vijayawada is a royal city"
a[22]
'c'
a[22]+a[23]+a[24]+a[25]
'comp'
b[22]+b[23]+b[24]+b[25]
'city'
>>> b[16]
'r'
>>> b[16]+b[17]+b[18]+b[19]+b[20]
'royal'
>>> b[11]
'i'
>>> b[11]+b[12]
'is'
>>> a="codegnan it solutions"
>>> a[-1]+a[-2]+a[-3]+a[-4]+a[-5]+a[-6]+a[-7]+a[-8]+a[-9]
'snoitulos'
>>> a[-9]+[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[-9]+[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
TypeError: can only concatenate str (not "list") to str
>>> a[-9]+[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a[-9]+[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
TypeError: can only concatenate str (not "list") to str
>>> a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
>>> a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'codegnan'
