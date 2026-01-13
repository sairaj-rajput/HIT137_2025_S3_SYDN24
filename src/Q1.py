# USER INPUT
first_shift = int(input("Enter shift1: "))
second_shift = int(input("Enter shift2: "))

# READ RAW TEXT
with open("raw_text.txt", "r") as file:
    original_text = file.read()

# ENCRYPTION LOGIC
cipher_text = ""

# LOOP & CONDITIONS CHECKS FOR ENCRYPTION
for char in original_text:
    if char.islower(): # lowercase condition
        if char <= 'm':
            cipher_text += chr((ord(char) - 97 + first_shift * second_shift) % 26 + 97)
        else:
            cipher_text += chr((ord(char) - 97 - (first_shift + second_shift)) % 26 + 97)
    elif char.isupper(): # uppercase condition
        if char <= 'M':
            cipher_text += chr((ord(char) - 65 - first_shift) % 26 + 65)
        else:
            cipher_text += chr((ord(char) - 65 + second_shift ** 2) % 26 + 65)
    else:
        cipher_text += char # ignore spaces, punctuation, numbers

# SAVE ENCRYPTED TEXT
with open("encrypted_text.txt", "w") as file:
    file.write(cipher_text)

print("\nEncrypted text saved to 'encrypted_text.txt'")

# DECRYPTION LOGIC
plain_text = ""

# LOOP & CONDITIONS CHECKS FOR DECRYPTION (REVERSE LOGIC)
for index in range(len(original_text)):
    original_char = original_text[index]
    encrypted_char = cipher_text[index]

    if original_char.islower(): # lowercase condition
        if original_char <= 'm':
            plain_text += chr((ord(encrypted_char) - 97 - first_shift * second_shift) % 26 + 97)
        else:
            plain_text += chr((ord(encrypted_char) - 97 + (first_shift + second_shift)) % 26 + 97)
    elif original_char.isupper(): # uppercase condition
        if original_char <= 'M':
            plain_text += chr((ord(encrypted_char) - 65 + first_shift) % 26 + 65)
        else:
            plain_text += chr((ord(encrypted_char) - 65 - second_shift ** 2) % 26 + 65)
    else:
        plain_text += encrypted_char  # ignore spaces, punctuation, numbers

# SAVE DECRYPTED TEXT
with open("decrypted_text.txt", "w") as file:
    file.write(plain_text)

print("Decrypted text saved to 'decrypted_text.txt'")

# VERIFY BOTH FILES ARE SAME
with open("raw_text.txt", "r") as file:
    original_file_text = file.read()

with open("decrypted_text.txt", "r") as file:
    decrypted_file_text = file.read()

# CONDITIONS CHECK AND GIVING RESPONSE
if original_file_text == decrypted_file_text: 
    print("\n Decryption completed Files is match.")
else:
    print("\n Decryption fail Files do not match.")
