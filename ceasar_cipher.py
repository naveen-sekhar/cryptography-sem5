def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'e':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'd':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

text = input("Enter the text to encrypt/decrypt: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter 'encrypt (e)' or 'decrypt (d)': ")

print("text:", caesar_cipher(text, shift, mode))