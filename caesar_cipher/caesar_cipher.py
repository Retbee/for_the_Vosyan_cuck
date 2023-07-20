alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_word = ""
    for char in text:
        char_position = alphabet.index(char) + shift
        if char_position > 25:
            char_position -= 26
        encrypted_word += alphabet[char_position]
    print(encrypted_word)

encrypt("hellocoders", 9)