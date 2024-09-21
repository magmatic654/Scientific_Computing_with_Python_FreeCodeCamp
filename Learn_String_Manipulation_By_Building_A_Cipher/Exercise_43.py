# Step 43
# A conditional statement can also have an else clause. This clause can be added to the end of an if statement to execute alternative code if the condition of the if statement is false:

# Example Code
# if x != 0:
#     print(x)
# else:
#     print('x = 0')
# As you can see in your output, when the loop iterations reach the space, a space is added to the encrypted string. Then the code outside the if block executes and a c is added to the encrypted string.

# To fix it, add an else clause after encrypted_text += char and indent all the subsequent lines of code except the print() call.

text = 'Hello World'
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