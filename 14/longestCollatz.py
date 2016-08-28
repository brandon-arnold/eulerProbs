upperBound = 1000000

C = [0] * upperBound
def countCollatz(n):
    global C; global upperBound
    curN = n
    c = 1
    while curN > 1:
        if curN < upperBound and C[curN] > 0:
            c += C[curN] - 1
            break
        if curN % 2 == 0:
            curN = int(curN // 2)
        else: curN = 3 * curN + 1
        c += 1
    C[n] = c
    return c

# find maximum Collatz number less than upperBound
maxC = 0
maxN = 2
for i in range(2, upperBound):
    curC = countCollatz(i)
    if maxC < curC:
        maxC = curC
        maxN = i

print("Max: %i with a chain of %i" % (maxN, maxC))
