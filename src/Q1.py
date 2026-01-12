# ------------------- USER INPUT -------------------
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

# ------------------- READ ORIGINAL TEXT -------------------
with open("raw_text.txt", "r") as f:
    text = f.read()

# ------------------- ENCRYPTION -------------------
encrypted_text = ""

for ch in text:
    if ch.islower():
        if ch <= 'm':
            encrypted_text += chr((ord(ch) - 97 + shift1 * shift2) % 26 + 97)
        else:
            encrypted_text += chr((ord(ch) - 97 - (shift1 + shift2)) % 26 + 97)
    elif ch.isupper():
        if ch <= 'M':
            encrypted_text += chr((ord(ch) - 65 - shift1) % 26 + 65)
        else:
            encrypted_text += chr((ord(ch) - 65 + shift2**2) % 26 + 65)
    else:
        encrypted_text += ch  # spaces, punctuation, numbers unchanged

# Save encrypted text
with open("encrypted_text.txt", "w") as f:
    f.write(encrypted_text)

print("\nEncrypted text saved to 'encrypted_text.txt'")

# ------------------- DECRYPTION -------------------
decrypted_text = ""

for i in range(len(text)):
    ch_original = text[i]         # original character
    ch_encrypted = encrypted_text[i]  # corresponding encrypted character

    if ch_original.islower():
        if ch_original <= 'm':
            decrypted_text += chr((ord(ch_encrypted) - 97 - shift1 * shift2) % 26 + 97)
        else:
            decrypted_text += chr((ord(ch_encrypted) - 97 + (shift1 + shift2)) % 26 + 97)
    elif ch_original.isupper():
        if ch_original <= 'M':
            decrypted_text += chr((ord(ch_encrypted) - 65 + shift1) % 26 + 65)
        else:
            decrypted_text += chr((ord(ch_encrypted) - 65 - shift2**2) % 26 + 65)
    else:
        decrypted_text += ch_encrypted  # spaces, punctuation, numbers unchanged

# Save decrypted text
with open("decrypted_text.txt", "w") as f:
    f.write(decrypted_text)

print("Decrypted text saved to 'decrypted_text.txt'")

# ------------------- VERIFICATION -------------------
with open("raw_text.txt", "r") as f:
    original = f.read()

with open("decrypted_text.txt", "r") as f:
    decrypted = f.read()

if original == decrypted:
    print("\n Decryption successful! Files match.")
else:
    print("\n Decryption failed! Files do not match.")
 