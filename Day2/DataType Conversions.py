Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DataType Conversions
#integer(int)
int(8)
8
int(4.5)
4
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(4+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#Float
float(8)
8.0
float(8.1)
8.1
float("hi")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(8+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(8+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(Flase)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
float(False)
0.0
#Character(char)
char(8)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    char(8)
NameError: name 'char' is not defined. Did you mean: 'chr'?
#str
str(8)
'8'
str(8.4)
'8.4'
str("Hello")
'Hello'
str(8+4j)
'(8+4j)'
str(True)
'True'
str(False)
'False'
#Complex
complex(8)
(8+0j)
complex(4.3)
(4.3+0j)
complex("hii")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex("hii")
ValueError: complex() arg is a malformed string
>>> complex(4+5j)
(4+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #Boolean
>>> bool(8)
True
>>> bool(8.8)
True
>>> bool("Surya")
True
>>> bool(4j+4)
True
>>> bool("True)
...      
SyntaxError: unterminated string literal (detected at line 1)
>>> bool(True)
...      
True
>>> bool(False)
...      
False
