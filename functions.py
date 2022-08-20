import alphabets as alpha
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