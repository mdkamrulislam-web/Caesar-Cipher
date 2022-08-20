import alphabets as alpha
def cipher(mode, text, shift):
    temp_str = ""
    temp_shift = shift % 26
    if(mode == "encode" or mode == "decode"):
        if(mode == "decode"):
            temp_shift *= -1
        for char in text:
            if(char in alpha.alphabet):
                position = alpha.alphabet.index(char)
                new_position = position + temp_shift
                temp_str += alpha.alphabet[new_position]
            else:
                temp_str += char
        print(f"The {mode}d text is :: {temp_str}")
    else:
        print("Enter a Valid Mode")
        
def restarter():
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if(restart == "yes"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher(direction, text, shift)
        restarter()
    elif(restart == "no"):
        print("Thanks for using Caser Chiper.")
    else:
        restarter()