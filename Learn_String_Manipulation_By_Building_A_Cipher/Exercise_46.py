# Step 46
# If you wish to incorporate additional characters into the alphabet string, such as digits or special characters, you'll find it's necessary to manually modify the right operand of the modulo operation.

# Replace 26 with len(alphabet) to avoid this issue.

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)