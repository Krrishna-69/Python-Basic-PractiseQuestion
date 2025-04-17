# WAP to swap 2 numbers without using third variable

a = 45
b = 55

# a , b = b, a

# a = a + b
# b = a - b
# a = a - b

# print(a, b)

l = [2, 8]
for i in range(len(l)-1):
    l[i], l[i+1] = l[i+1], l[i]

print(l)


