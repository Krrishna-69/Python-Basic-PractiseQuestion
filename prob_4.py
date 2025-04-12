
#4.WAP to convert string into list and vice versa.

s = 'hello world'
# print(s.split())
# print(''.join(s.split()))
l = ['tumchi',' ', 'vahini']
st = ''
for i in s:
    if i != ' ':
        st += i
    else:
        l += [st]
        st = ''

l += [st]
print(l)

#Another way string to list
for i in s:
    l += [i]
print(l)

#converting from list to string
for i in l:
    st += i

print(st)
