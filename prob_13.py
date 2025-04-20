# wap to get below o/p
sentence = 'hello world welcome to python programming hi there'
#{'h':['hello', 'hai'], 'w':['world', 'welcome']......}

d = {}
for word in sentence.split():
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]

print(d)
