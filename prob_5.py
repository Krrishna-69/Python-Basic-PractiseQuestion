#5.WAP to convert 'hello welcome to python' to comma separated string.

s = 'hello world guys'

words = s.split()
print(words)
t = ','.join(words)
print(t)

for i in s.split():
    print(i, end=',')