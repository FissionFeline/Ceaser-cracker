def get_input(msg = "Enter something"):
    print(msg)
    str_input = input(">")
    if(len(str_input) < 3 or str_input.isspace()):
        return get_input("This requires valid input")
    return str_input

def main():
    get_input("Please enter a pharse to decrypt")


if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        pass