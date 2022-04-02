import re
from BaseParse import BaseParser

def parsingArithmetic(inputVal):
    arithmetic_pattern = "((\+\+)|(\+=))"
    expression_pattern = "[NX](AOp[NX])*;"

    check_arithmetic = re.sub(arithmetic_pattern, "AOp", BaseParser(inputVal))
    check_expression = re.sub(expression_pattern, "E", check_arithmetic)
    print(check_expression)

parsingArithmetic("i++;")   # XAOp;
parsingArithmetic("i+=45;") # E
