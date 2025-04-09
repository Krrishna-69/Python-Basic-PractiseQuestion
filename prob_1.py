#1.WAP to find the length of the string without using inbuilt funct.

s = 'hello python'
print(len(s))
length = 0
for _ in s:       #when we are not changing ref var--> _(throw away var)
    length += 1
print(f'The length of the string {s}---> {length}')
#print()
