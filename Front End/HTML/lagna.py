from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def encrypt_des(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return b64encode(ciphertext).decode('utf-8')

def decrypt_des(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(b64decode(ciphertext))
    return unpad(decrypted_text, DES.block_size).decode('utf-8')


# Step 1: Alice sends the text
original_text = """Your original text here..."""

print("Original Text:\n", original_text)

# Generate a random 8-byte (64-bit) key
key = get_random_bytes(8)

# Step 2: Alice encrypts the text using DESA
encrypted_text = encrypt_des(original_text, key)
print("\nEncrypted Text:\n", encrypted_text)

# Step 3: Bob decrypts the text
decrypted_text = decrypt_des(encrypted_text, key)
print("\nDecrypted Text by Bob:\n", decrypted_text)

# Step 4: Image Encryption and Decryption
# You can implement image encryption and decryption here