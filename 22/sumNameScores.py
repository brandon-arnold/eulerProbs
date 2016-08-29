def getValue(name):
    total = 0
    for c in name:
        val = ord(c)
        if val > 64 and val < (65+26):
            total += (val - 64)
    return total

lines = [line.strip() for line in open(".\p022_names.txt", 'r')]

names = []
for line in lines:
    for name in line.split(','):
        names.append(name)
names = sorted(names)
nameValues = [getValue(name) for name in names]
nameScores = [nameValues[i] * (i + 1) for i in range(len(nameValues))]
print(sum(nameScores))

