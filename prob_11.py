#wap to check given string is palindrome

s = 'MalayaLam'
s1 = s.lower()
if s1 == s1[::-1]:
    print(f'the string {s} is palindrome.')
else:
    print(f'the string {s} is not a palindrome.')
print()
