#WAP to get below o/p

s = 'Hi How are you'

#o/p--> 'iH woH rea uoy

res = ''
for ch in s.split():
    res += ch[::-1] + ' '
print(res)
