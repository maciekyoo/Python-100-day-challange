alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_direction_true = False
while is_direction_true == False:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        is_direction_true = True
    else:
        print("wrong direction! Try Again\n")

shift = shift % 26

cipher_text_encode = ""
cipher_text_decode = ""


def Encrypt(string, number):
    global cipher_text_encode
    for char in string:
        position = alphabet.index(char)
        new_position = position + number
        new_char = alphabet[new_position]
        cipher_text_encode = cipher_text_encode + new_char
    print(f"Text encoded is {cipher_text_encode}")


def Decrypt(string, number):
    global cipher_text_decode
    for char in string:
        position = alphabet.index(char)
        new_position = position - number
        new_char = alphabet[new_position]
        cipher_text_decode = cipher_text_decode + new_char
    print(f"Text decoded is {cipher_text_decode}")


if direction == 'encode':
    Encrypt(string=text, number=shift)
elif direction == 'decode':
    Decrypt(string=text, number=shift)
else:
    print("Wrong direction!")
