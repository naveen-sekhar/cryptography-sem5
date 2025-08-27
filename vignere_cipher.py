def vigenere_encrypt(plaintext, keyword):
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())
    keyword = ''.join(c for c in keyword.upper() if c.isalpha())

    ciphertext = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p, k in zip(plaintext, keyword_repeated):
        p_num = ord(p) - ord('A')
        k_num = ord(k) - ord('A')
        c_num = (p_num + k_num) % 26
        ciphertext.append(chr(c_num + ord('A')))

    return ''.join(ciphertext)


def vigenere_decrypt(ciphertext, keyword):
    ciphertext = ''.join(c for c in ciphertext.upper() if c.isalpha())
    keyword = ''.join(c for c in keyword.upper() if c.isalpha())

    plaintext = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for c, k in zip(ciphertext, keyword_repeated):
        c_num = ord(c) - ord('A')
        k_num = ord(k) - ord('A')
        p_num = (c_num - k_num) % 26
        plaintext.append(chr(p_num + ord('A')))
    return ''.join(plaintext)

plaintext = "ATTACK"
keyword = "KEY"
encrypted = vigenere_encrypt(plaintext, keyword)
decrypted = vigenere_decrypt(encrypted, keyword)

print(f"Plaintext: {plaintext}")
print(f"Keyword: {keyword}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
