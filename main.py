

def get_input(msg = "Enter something"):
    print(msg)
    str_input = input("> ")
    if(len(str_input) < 3 or str_input.isspace()):
        return get_input("This requires valid input")
    return str_input

def calculate_frequencies(target_str : chr,char_count : dict) -> dict:
    length = len(target_str)
    frequency = (map(lambda char : (char * 100) / length ,char_count.values()))
    freqList = list(frequency)
    return dict(zip(char_count.keys(),freqList))

def shift_char(c : chr, by : int) -> chr :
    if c == ' ': return ' '
    
    #regular to ascii
    rta = lambda num : ord('a') + num

    position = (ord(c) + by) - ord('a')
    
    if position > 25: position -= 26
    return (chr(rta(position)))
    

eng_frequency = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 
'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 
'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 
'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
 'Q': 0.10, 'Z': 0.07}

order = ''.join(eng_frequency.keys())

def calculate_similarities(freq1 : dict, freq2 : dict) -> dict :
    pass

def main():
    str_to_decrypt = get_input("Please enter a pharse to decrypt")

    
    char_count = {char:str_to_decrypt.count(char) for char in str_to_decrypt}

    str_frequency = calculate_frequencies(str_to_decrypt,char_count)

    print(order)
    
if(__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        pass