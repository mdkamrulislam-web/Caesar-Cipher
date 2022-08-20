import alphabets as alpha
def cipher(mode, text, shift):
    index = 0
    temp_str = ""
    temp_index = 0
    for i in text:
        for j in alpha.alphabet:
            if(i == j):
                index = alpha.alphabet.index(j)
                if(mode == "encode"):
                    if((index + shift) > 25):
                        temp_index = (index + shift) - 26
                        temp_str += alpha.alphabet[temp_index]
                    else:
                        temp_str += alpha.alphabet[index + shift]
                if(mode == "decode"):
                    if((index - shift) < 0):
                        temp_index = (index - shift) + 26
                        temp_str += alpha.alphabet[temp_index]
                    else:
                        temp_str += alpha.alphabet[index - shift]
                break
    if(mode == "encode"):
        print(f"Your Encoded Message is: {temp_str}")
    else:
        print(f"Your Decoded Message is: {temp_str}")
                    
'''
def encrypt(t, s):
    index = 0
    encrypted_str = ""
    encode_index = 0
    for i in t:
        for j in alpha.alphabet:
            if(i == j):
                index = alpha.alphabet.index(j)
                if((index + s) > 25):
                    encode_index = (index + s) - 26
                    encrypted_str += alpha.alphabet[encode_index]
                else:
                    encrypted_str += alpha.alphabet[index + s]
                break
    print(encrypted_str)

def decrypt(t, s):
    index = 0
    decrypted_str = ""
    decode_index = 0
    for i in t:
        for j in alpha.alphabet:
            if(i == j):
                index = alpha.alphabet.index(j)
                if((index - s) < 0):
                    decode_index = (index - s) + 26
                    decrypted_str += alpha.alphabet[decode_index]
                else:
                    decrypted_str += alpha.alphabet[index - s]
                break
    print(decrypted_str)
    
def encodeOrDecode(mode, text, shift):
    if(mode == "encode"):
        encrypt(t = text, s = shift)
    elif(mode == "decode"):
        decrypt(t = text, s = shift)
'''