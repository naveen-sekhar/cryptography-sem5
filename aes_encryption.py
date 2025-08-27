from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Fixed 32-byte key for AES-256 (store securely in practice)
key = b'Sixteen byte key for AES-256!!!!'

def encrypt_file(input_file, output_file):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while chunk := f_in.read(1024):
            if len(chunk) % AES.block_size != 0:
                chunk = pad(chunk, AES.block_size)
            f_out.write(cipher.encrypt(chunk))

def decrypt_file(input_file, output_file):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        while chunk := f_in.read(1024):
            decrypted = cipher.decrypt(chunk)
            if f_in.peek(1) == b'':
                decrypted = unpad(decrypted, AES.block_size)
            f_out.write(decrypted)

# Example usage
if __name__ == "__main__":
    encrypt_file('input.txt', 'encrypted.bin')
    print("File encrypted as encrypted.bin")
    decrypt_file('encrypted.bin', 'decrypted.txt')
    print("File decrypted as decrypted.txt")
