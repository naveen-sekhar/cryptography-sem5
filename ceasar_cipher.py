def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Example usage
plaintext = "ATTACK AT DAWN"
shift_value = 5

encrypted_text = caesar_cipher(plaintext, shift_value, 'encrypt')
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift_value, 'decrypt')
print("Decrypted:", decrypted_text)
