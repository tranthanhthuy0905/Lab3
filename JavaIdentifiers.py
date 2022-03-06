import re


def javaIdCheck(expression):
    expressionsList = expression.split(" ")
    
    patternTerm = "^[a-z][a-zA-Z0-9_]*$"
    patternInt = "^[+-]?[0-9]+$"
    patternFloat = "^[+-]?([0-9]*[.])[0-9]+$"
    
    searching = re.search(pattern, expression)
    # if searching:
    #     print("It matches well")
    #     print(searching)
    # else:
    #     print("Oops! We got no match")

    x = re.sub(pattern, "X", inputVar)
    print(x)


javaIdCheck("test++")              # X
javaIdCheck("testing123")           # X
javaIdCheck("testing_")             # X
javaIdCheck("@testing")             # @testing
javaIdCheck("testing something")    # testing something
