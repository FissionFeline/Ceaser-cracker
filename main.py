def get_input():
    str_input = input()
    if(len(str_input) < 3 or str_input.isspace()):
        print("Please enter something valid")
        return get_input()
    return str_input

get_input()
