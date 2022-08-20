import functions as fun
import art
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

fun.cipher(direction, text, shift)

fun.restarter()

