from pyDes import des, ECB, PAD_PKCS5
import base64

# Key must be exactly 8 bytes
key = b"filekey1"

cipher = des(key, ECB, padmode=PAD_PKCS5)


# === Encrypt File ===
def encrypt_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    encrypted_data = cipher.encrypt(data)
    encrypted_base64 = base64.b64encode(encrypted_data)

    with open(output_file, 'wb') as f:
        f.write(encrypted_base64)

    print(f"Encrypted content written to {output_file}")


# === Decrypt File ===
def decrypt_file(encrypted_file, decrypted_output_file):
    with open(encrypted_file, 'rb') as f:
        encrypted_base64 = f.read()

    encrypted_data = base64.b64decode(encrypted_base64)
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(decrypted_output_file, 'w') as f:
        f.write(decrypted_data.decode())

    print(f"Decrypted content written to {decrypted_output_file}")


# === Example Usage ===
encrypt_file("plain.txt", "encrypted.txt")
decrypt_file("encrypted.txt", "decrypted.txt")
