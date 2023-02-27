

import re

def replace(s):
    
    pattern = r'[ ,.]'

   
    s = re.sub(pattern, ':', s)

    return s


theString= str(input("enter a string  " ))

matched= replace(theString)

print(matched)
