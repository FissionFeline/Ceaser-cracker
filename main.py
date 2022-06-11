def get_input(msg = "Enter something"):
    print(msg)
    str_input = input(">")
    if(len(str_input) < 3 or str_input.isspace()):
        return get_input("This requires valid input")
    return str_input
    
get_input("Please enter a pharse to decrypt")
