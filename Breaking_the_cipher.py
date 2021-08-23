import string
import time
def encrypt(text, shift):

    encrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    
    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter    
        else:
            encrypted_text[i] = letter

    return "".join(encrypted_text)

def decrypt(text, shift):
    
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    
    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter 
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)


def brute_force_decrypt(text):
    print("\n\n\tCracking the shift Cipher using The Bruteforce Attack")
    print("\n____________________________________________________________\n")
    time.sleep(1)
    for n in range(26):
        print(f"\nUsing a shift value of {n}")
        print("\n\tPlain text Output:"+ decrypt(text, n))
        print("\n____________________________________________________________\n")
        time.sleep(1)
 
e = encrypt("\tMadhav Singh went to college", 16)

print("\n____________________________________________________________\n")

print("\n\tDecrytping with known Key: 16 \n\n\tThe plain text is: ")
time.sleep(1)

print("\t" + decrypt(e, 16))
print("\n____________________________________________________________\n")
time.sleep(2)

brute_force_decrypt(e)