insert_key = int(input())
number_of_lines = int(input())

encrypted_text = []
for number in range(number_of_lines):
    encrypted_letters = input()
    letter_dec = ord(encrypted_letters) + insert_key
    encrypted_text.append(letter_dec)

decrypted_text = ''.join(chr(index) for index in encrypted_text)

print(decrypted_text)
