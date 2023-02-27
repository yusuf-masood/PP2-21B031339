import re

def split(s):
 
    
    words = re.findall('[A-Z][^A-Z]*', s)
    return words

theString= str(input("enter a String   "))


matched= split(theString)
print(matched)