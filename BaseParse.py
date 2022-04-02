import re 

def BaseParser(inputVal):
    identifier_pattern = "[a-z]{1}[a-zA-Z0-9_]*"
    number_pattern = "[+-]?([0-9]*[.]?)[0-9]+"
    
    check_identifier = re.sub(identifier_pattern, "X", inputVal)
    check_number = re.sub(number_pattern, "N", check_identifier)
    deleting_space = re.sub("\s", "", check_number)
    return deleting_space
    