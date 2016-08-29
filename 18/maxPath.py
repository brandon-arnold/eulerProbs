T = [[int(t) for t in line.strip().split()] for line in open(".\p067_triangle.txt", 'r')]
lastSums = []
curSums = T[len(T) - 1]
for i in range(len(T) - 2, -1, -1):
    lastSums = curSums
    curSums = []
    for j in range(len(T[i])):
        curSums.append(T[i][j] + max(lastSums[j], lastSums[j + 1]))
print(curSums[0])
