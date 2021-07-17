word = 'abacbab'

repeatDict = {}

for value in sorted(set(list(word))):
    repeatDict[value] = list(word).count(value)

values = list(repeatDict.values())
keys = list(repeatDict.keys())
max_count = keys[values.index(max(values))]

l_max = [key for key in repeatDict if repeatDict[key] >= max(values)]

print(l_max)
