def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + shift) % 26) + 65)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    text = input("Enter the text to encrypt: ")
    default_shift = 1
    encrypted_text = encrypt(text, default_shift)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
