import re
from BaseParse import BaseParser


def declarationParse(expression):
    datatype_pattern = "((byte)|(short)|(int)|(long)|(float)|(double)|(boolean)|(char)|(String))"
    string_pattern = "((\".+\")|(\'.+\'))"
    boolean_pattern = "(true|false)"
    declaration_pattern = "((DTX(,X)*;)|(DTX(,X)*=[NVB];))"

    check_datatype = re.sub(datatype_pattern, "DT", expression)
    check_boolean = re.sub(boolean_pattern, "B", check_datatype)
    check_string = re.sub(string_pattern, "V", check_boolean)
    check_declaration = re.sub(
        declaration_pattern, "DE", BaseParser(check_string))

    print(check_declaration)


declarationParse(" int number, anotherNumber, yetAnotherNumber; ")
declarationParse(" boolean isFinished = false; ")
declarationParse(" String welcomeMessage = 'Hello!';")
