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
# Get the input from the userr
text = input("Enter the text to encrypt: ")
print("Ciphertext:", rail_fence_encrypt(text))
