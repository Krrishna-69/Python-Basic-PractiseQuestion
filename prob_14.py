# WAP to replace all the characters with '-' if the characters occurs more than
# once in a string.

s = 'hellohai'

for i in s:
    if s.count(i)>1:
        s = s.replace(i, '_')

print(s)
