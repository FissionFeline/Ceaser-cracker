def get_input(msg = "Enter something"):
    print(msg)
    str_input = input(">")
    if(len(str_input) < 3 or str_input.isspace()):
        return get_input("This requires valid input")
    return str_input

def main():
    str_to_decrypt = get_input("Please enter a pharse to decrypt")
    char_count = {}
    for i in str_to_decrypt:
        if(i in char_count):
            char_count[i] = 1
        else:
            char_count[i] = char_count[i] + 1
    


if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        pass