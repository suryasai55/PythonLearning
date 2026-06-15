'''Regular Expressions are powerful tools(module) embedded in python which is mainly used to find a pattern
with in a given string or statements or files and mainly used for text manipulation.'''

'''
a="codegnan\nis\tin\nvja"
print(a)
'''

#rstring:
'''
a=r"codegnan\nis\tin\nvja"
print(a)
'''

'''In regex we have 5 methods that include:
    compile()
    search()
    findall()
    split()
    sub()'''
#sequence characters
'''
\\w->It matches alphanumericals
\\W->It matches non-alphanumericals
\\d->It matches any digit
\\D->It matches non-digits
\\s->It represents white spaces
\\S->represents non-white spaces
'''

import re
a="11 22 map cat dog maths money cash cap cup mug donkey"

#b=re.compile(r"m\\w\\w")
'''
c=b.search(a)
print(c)

d=re.search(r"m\\w+",a)
print(d)
'''

#findall()
'''
d=re.findall("m\\w+",a)
print(*d)

d=re.findall("d\\w+",a)
print(*d)

d=re.findall("c\\w+",a)
print(*d)
'''
#split()
'''
e=re.sub(r"maths","science",a)
print(e)

f=re.split(r"\s",a)
print(f)
'''

#sub()
'''
x=re.sub(r"maths","science",a)
print(x)
'''

'''
import re
a="year 2026 month 6 date 13"
b=re.findall(r"\d+",a)
print(b)
'''

































