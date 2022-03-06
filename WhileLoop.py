import re

def whileLoop(expression):
    patternInt = "^[+-]?[0-9]+$"
    patternFloat = "^[+-]?([0-9]*[.])[0-9]+$"
    patternWhile = "while"
    
    expressionList = expression.split(" ")
    res, searching, pattern = checking(
        patternInt, patternFloat, expressionList)
    # if res:
    #     if res == "F":
    #         print("YES! It is a float")
    #     else:
    #         print("YES! It is an integer")
    #     print(searching)
    # else:
    #     print("Oops! We got no match")

    label = re.sub(pattern, res, numb)
    return label

def checking(pattern1, pattern2, numb):
    result1 = re.search(pattern1, numb)
    result2 = re.search(pattern2, numb)
    if result2:
        return "F", result2, pattern2
    elif result1:
        return "I", result1, pattern1
    else:
        return numb, "", ""
