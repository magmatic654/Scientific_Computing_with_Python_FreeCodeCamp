# Step 44
# Try to assign the string 'Hello Zaira' to your text variable and see what happens in the terminal.

# You'll see a string index out of range exception. Don't worry, you'll figure out how to fix it soon!

text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char
    else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)