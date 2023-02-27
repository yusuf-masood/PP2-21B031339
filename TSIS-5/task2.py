

import re

my_string= str(input("enter a string   "))
p = re.compile('ab{2,3}?')
m = p.search(my_string)


if m:
    print(m.group())
else:
    print("no match  ")
