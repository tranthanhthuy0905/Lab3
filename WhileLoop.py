import re
from unittest.mock import Base
from BaseParse import BaseParser


def whileLoop(loop):
    _WH = "while"
    arithmetic_pattern = "[+\-*/]"
    conditional_pattern = "(<=)|(>=)|(!=)|(==)|(<)|(>)"
    logical_pattern = "(\&\&)|(\|\|)"
    condStatement_pattern = "X(AOp[NX])*COp([NX]AOp)*[NX](LOpX(AOp[NX])*COp([NX]AOp)*[NX])*"
    expression_pattern = "[NX](AOp[NX])*;"
    statement_pattern = "X=E|LOOP|SELECT"
    codeblock_pattern = "[{](S)+"
    while_pattern = "_WH\(CS\)\{CB\}"

    check_while = re.sub(_WH, "_WH", loop)
    check_arithmetic = re.sub(
        arithmetic_pattern, "AOp", BaseParser(check_while))
    check_conditional = re.sub(
        conditional_pattern, "COp", check_arithmetic)
    check_logical = re.sub(logical_pattern, "LOp", check_conditional)
    check_condStatement = re.sub(
        condStatement_pattern, "CS", check_logical)
    check_expression = re.sub(expression_pattern, "E", check_condStatement)
    check_statement = re.sub(statement_pattern, "S", check_expression)
    check_codeblock = re.sub(codeblock_pattern, "{CB", check_statement)
    check_selection = re.sub(while_pattern, "SELECT", check_codeblock)
    print(check_selection)


whileLoop("while (x>5){ x = x + 1; y = x; }")
