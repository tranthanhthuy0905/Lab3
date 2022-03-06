import re

'''
TEST CASES:
    1. 23423wefwe2323 => We got no match (wrong unsigned int)
    2. -2323wsefefw => We got no match (wrong signed int)
    3. -23234.23423dwe => We got no match (wrong float)
    4. 234235235 => It is an (unsigned) integer
    5. -252232354 => It is a (signed) integer
    6. -23423.2353 => It is a float
'''

def numberCheck(numb):
    patternInt = "^[+-]?[0-9]+$"
    patternFloat = "^[+-]?([0-9]*[.])[0-9]+$"

    res, searching, pattern = checking(
        patternInt, patternFloat, numb)
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

numberCheck('23423wefwe2323')       # 23423wefwe2323
numberCheck('-2323wsefefw')         # -2323wsefefw
numberCheck('-23234.23423dwe')      # -23234.23423dwe
numberCheck('234235235')            # I
numberCheck('-252232354')           # I
numberCheck('-23423.2353')          # F
