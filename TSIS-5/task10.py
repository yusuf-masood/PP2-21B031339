

def camel_to_snake(s):
  
    import re
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


    return s



theString = 'ConvertGivenCamelCaseStringToSnakeCase'
theString = camel_to_snake(theString)
print(theString)  
