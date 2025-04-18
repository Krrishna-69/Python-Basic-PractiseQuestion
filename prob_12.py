#wap to search for the character in a string and return the corresponding index.

s = 'hello world'
ch = 'l'
for index, element in enumerate(s):
    if element == ch:
        print(f'The char {ch} is at number {index}')
