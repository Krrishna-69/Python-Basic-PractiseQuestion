#6.WAP to print alternate characters from a given string
s = 'hello python'
#o/p-->'hlopto'

t=s[0::2]
print(t)

for i in range(0, len(s), 2):
     print(s[i], end= '')
