

def insert_spaces(s):
    import re
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

    return s

theString = 'InsertSpacesBetweenWordsStartingWithCapitalLetters'
matched = insert_spaces(theString)
print(matched)