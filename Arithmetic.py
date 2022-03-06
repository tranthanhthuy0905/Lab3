import JavaIdentifiers
import Numbers
import re


def statementParsing(expression):
    result = ""
    expressionsList = expression.split(" ")

    for elm in expressionsList:
        if "++" in elm or "--" in elm:
            elm = elm[:-2]
            increment = elm[-2:]
            checking = checkingStatement(elm)
            result += checking
            result += " " + increment
        else:
            checking = checkingStatement(elm)
            result += checking
        if expressionsList.index(elm) != len(expressionsList) - 1:
            result += " "
    print('Parsed result: ', result)


def checkingStatement(inputVal):
    patternTerm = "^[a-z][a-zA-Z0-9_]*$"
    patternInt = "^[+-]?[0-9]+$"
    patternFloat = "^[+-]?([0-9]*[.])[0-9]+$"
    patternOperations = "^[+-*/=]+"

    checkingTerm = re.search(patternTerm, inputVal)
    checkingInt = re.search(patternInt, inputVal)
    checkingFloat = re.search(patternFloat, inputVal)
    checkingOperations = re.search(patternOperations, inputVal)

    if checkingTerm:
        x = re.sub(patternTerm, "T", inputVal)
    elif checkingInt:
        x = re.sub(patternInt, "I", inputVal)
    elif checkingFloat:
        x = re.sub(patternFloat, "F", inputVal)
    elif checkingOperations:
        x = re.sub(patternFloat, "O", inputVal)
    else:
        x = re.sub(patternFloat, "", inputVal)
    return x


statementParsing("num1 + 4.2")          # X + F
statementParsing("num1 + w * -2")       # X + X * I
statementParsing(" num1 * num2 – num3")  # X * X - X
