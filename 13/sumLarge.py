# copy-paste the input into in.txt
largeNs = [line.strip() for line in open(".\in.txt", 'r')]
nLens = [len(n) for n in largeNs]
maxLen = max(nLens)

# sum the first 11 digits of each
outSumList = []
sumCarry = 0
for i in range(maxLen - 10, maxLen + 1):
    for j in range(len(largeNs)):
        curLen = nLens[j]
        if curLen >= i:
            curN = largeNs[j]
            sumCarry += int(curN[curLen - i])
    outSumList.append(sumCarry % 10)
    sumCarry //= 10

# output the first ten digits
outString = str(sumCarry)
for i in range(10 - len(outString)):
    outString += str(outSumList.pop())
print("%s..." % outString)
