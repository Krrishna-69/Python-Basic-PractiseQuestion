#2.WAP to reverse a string without using inbuilt function
s = 'hello pyhton'
s.reverse()
print(s[::-1])

res = ''
for i in s:
    res = i + res
print(res)
print()

s1 = reversed(s)
print(list(s1))

