# Step 45
# When the loop reaches the letter Z, the sum index + shift exceeds the last index of the string alphabet. Therefore, alphabet[new_index] is trying to use an invalid index, which causes an IndexError to be thrown.

# You can notice that the output in the terminal stops at the space immediately before the Z, the last print before the error is thrown.

# In this case, the modulo operator (%) can be used to return the remainder of the division between two numbers. For example: 5 % 2 is equal to 1, because 5 divided by 2 has a quotient of 2 and a remainder of 1.

# Surround index + shift with parentheses, and modulo the expression with 26, which is the alphabet length.

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = (index + shift) % 26
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)