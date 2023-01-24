# Linting is the process of checking code for best practice formatting issues
# If a code fails a lint test / check, it is not rejected by default
# pylint - linting tool for python


""" Module docstring saying what this module this"""
# */ multi line comment in other spaces
#  /*
 
longandcoolnameofavariablethatisimportant="abc"

def printtext(x):
    ''' Telling you what this module does
    lots of things to say
    blah
    '''
    
    print("hello world")
    return f"text added is {x}"

print(printtext('howdy'))
print(printtext(longandcoolnameofavariablethatisimportant))
