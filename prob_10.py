#wap to merge two list
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]
l3 = [3, 6, 9, 12]
l4 = []

for i in zip(l1, l2):
    l4.append(i)
print(l4)

print([*l1, *l2])
print(sum([l1, l2], []))
print(sum([l1, l2, l3], []))

l2.extend(l1)
print(l2)