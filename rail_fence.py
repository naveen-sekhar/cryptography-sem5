def rail_fence_encrypt(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()

    # Create two rails
    rail1 = ""
    rail2 = ""

    # Distribute characters between rails
    for i in range(len(text)):
        if i % 2 == 0:
            rail1 += text[i]
        else:
            rail2 += text[i]

    # Combine rails to get ciphertext
    return rail1 + rail2


# Example usage
plaintext = "Hello World"
ciphertext = rail_fence_encrypt(plaintext)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
