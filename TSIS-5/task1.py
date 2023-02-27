
import re

def hasAFollowedbyB(theString):
    
    pattern= r"a(b*)"

    match= re.match(pattern, theString)

    return match

theString= str(input("enter the string   "))
matched = hasAFollowedbyB(theString)
if matched:
    print(matched.group())
else:
    print("no matched ")