from Crypto.PublicKey import RSA
p = 3
q = 17
n = p * q
e = 13
d = 5
m = 7
phi_n = (p - 1) * (q - 1)
if m < 0 or m >= n:
    print(f"Error: m must be between 0 and {n-1}")
    exit()

key = RSA.construct((n, e, d))
print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")

c = pow(m, e, n)
print(f"Ciphertext: c = {c}")

decrypted_m = pow(c, d, n)
print(f"Decrypted message: m = {decrypted_m}")

if decrypted_m == m:
    print("Success: Decrypted message matches original m")
else:
    print("Error: Decryption failed")