def print_string(string):
    if type(string) == str:
        print(string)
    else:
        raise TypeError("'string' must be a str type")

def analyze_string(string):
    if type(string) == str:
        raise TypeError("'string' must be a str type")
    else:
        if string.isupper():
            print(f"String '{string}' is uppercase")
        elif string.islower():
            print(f"String '{string}' is lowercase")
        else:
            print(f"String '{string}' is mixedcase")

def to_uppercase(string):
    if type(string) is not str:
        raise TypeError("'string' must be a str type")
    else:
        return string.upper()