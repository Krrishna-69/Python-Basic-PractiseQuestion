#3. WAP to replace one string with another.
#eg: hello world---> hello Universe.

s = 'hello world'
u = 'universe'
r = ''
for i in s.split():
    if i == 'world':
        r = r + u

    else:
        r = i + ' '

print(r)

#another way.
if 'world' in s:
    s1 = s.replace('world', 'Universe')
    print(s1)
else:
    print('Check question once')
print()

