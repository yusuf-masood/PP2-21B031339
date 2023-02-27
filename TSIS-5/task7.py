

import re

def snakeToRegex(s):
    # define the regular expression pattern
    pattern = r'_([a-z])'

    # use the sub() method to replace matches with the capitalized letter
    s = re.sub(pattern, lambda m: m.group(1).upper(), s)

    # return the modified string
    return s
theString = "the_quick_brown_fox_jumps_over_the_lazy_dog"

matched= snakeToRegex(theString)
print(matched)