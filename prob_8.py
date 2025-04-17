#.WAF to convert upper case into lower case and vice versa

str = input('Enter a char : ')
s1 = ''
for i in str:
    if 'a' <= i <= 'z':
        s1 += chr(ord(i)-32)
    else:
        s1 += chr(ord(i)+32)
print(s1)



# if 97 <= ord(ch) <= 122:
#     print(chr(ord(ch)-32))
# else:
#     print(chr(ord(ch)+32))